# TDD Doesn't Work on LLM Code. Here's What Does.

## Benchmark-driven development: red is a fraction, green is a bar you pick, and "cannot reproduce" stops being an acceptable resolution.

I've been writing tests the same way for a long time. Red, green, refactor. It's muscle memory at this point, and it has survived every stack I've thrown at it.

Then we shipped a feature with an LLM call in the middle of it, and my muscle memory started lying to me.

## The ticket I closed wrong

A support-triage bot misrouted a customer email. The message was *"my card was charged twice"* — any human files that under billing in half a second. The bot put it in *other*, where it sat in the wrong queue for two days until the customer followed up, angrier.

I did what you do. Copied the exact message into a playground, ran it. Right answer. Ran it again. Right answer again. I stared at it for a minute, wrote *cannot reproduce* on the ticket, and moved on. I want to be honest here: it didn't even feel sloppy at the time. That's the standard procedure for a bug you can't trigger.

Three weeks later it happened again. Different email, same shape.

The thing I eventually had to sit with is that there was never a bug that "happens on this input." There was a prompt that fails on this input maybe forty percent of the time, and production had been quietly rolling that die all month. My two playground runs were two lucky rolls. I closed a ticket on the strength of a coin landing heads twice.

## One run is a sample, not a result

Here's the test I would have written for that bot, back when I still trusted my instincts:

```python
def test_triage():
    assert triage("my card was charged twice") == "billing"
```

For a parser, this is proof. For a model call it's a sample — literally one draw from a distribution. If the true success rate on that input is 70%, the test goes green seven runs out of ten. And if your CI retries flaky tests (ours did), it goes green 91% of the time. Congratulations: you've built a machine for hiding exactly the number you needed to see.

A test that passes seven times out of ten is not a passing test. It's a probability, and your tooling is rounding it to `True`.

## Swapping the instrument

The fix I landed on — after prompt tweaks, temperature 0, and a certain amount of denial — wasn't a better prompt. It was a better instrument. Keep the TDD loop. Change what red and green mean.

- **Red** is a low fraction: `6/10 FLAKY`, not a red cross.
- **Green** is a fraction that clears a bar *you* picked. Maybe that's 10/10. Maybe 95% is fine for your product and your budget. Perfection becomes a decision instead of a default.
- **Refactor** means a new prompt or model, and it has to beat the incumbent on the same cases at the same sample size before it ships.
- The benchmark stays in the suite forever afterward, the way a regression test does.

I've been calling this benchmark-driven development. The loop is TDD's; only the arithmetic changed.

## The same incident, run through the loop

I maintain a small pytest plugin, [pytest-probability](https://pypi.org/project/pytest-probability/), that exists mostly so this loop costs nothing to adopt. A benchmark is a pytest test body with a `bench_` prefix. That's the whole learning curve.

*(Disclosure: I'm the creator of pytest-probability — this article describes the methodology I built it for, so read the tooling recommendations with that bias in mind. The plugin is MIT-licensed and free, with no dependencies beyond pytest; the methodology itself works with any harness that can repeat a test and count.)*

**Step one: the incident becomes a case.** The production message goes in verbatim, next to cases we already believed were fine. Then you sample instead of running once:

```python
# bench_triage.py
import pytest

@pytest.mark.parametrize("text,expected", [
    # the production incident, verbatim
    pytest.param("my card was charged twice", "billing", id="refund"),
    pytest.param("i cannot reset my password", "account", id="password"),
    pytest.param("the box arrived two weeks late", "shipping", id="late_box"),
])
def bench_triage(text, expected):
    assert triage(text) == expected
```

```
$ pytest bench_triage.py --prob-runs=10

  triage::refund     6/10  FLAKY
  triage::password   8/10  FLAKY
  triage::late_box  10/10

  Overall: 24/30 passed (80%)
```

There's my unreproducible bug, reproducing four times out of ten. Note the second line, too — `password` at 8/10 was a liability nobody had filed a ticket for yet. Sampling finds the bugs you weren't looking for, which single runs basically never do.

**Step two: candidates fight the incumbent.** The classic failure mode of prompt work is replacing the prompt because the new one "felt better" in three manual tries. Sample size of three, no control group. Instead, the candidate goes on a parametrize axis next to the current prompt, so both face identical cases:

```python
@pytest.mark.parametrize("prompt", ["v1", "v2"])
@pytest.mark.parametrize("text,expected", CASES)
def bench_triage(text, expected, prompt):
    response = llm.complete(PROMPTS[prompt].format(text=text))
    record_usage(model=response.model, cost=response.cost,
                 input_tokens=response.input_tokens,
                 output_tokens=response.output_tokens)
    assert response.category == expected
```

```
  triage::refund-v1     6/10  $0.0002  FLAKY
  triage::refund-v2    10/10  $0.0006
  triage::password-v1   8/10  $0.0002  FLAKY
  triage::password-v2   9/10  $0.0006  FLAKY
  triage::late_box-v1  10/10  $0.0002
  triage::late_box-v2  10/10  $0.0006
```

This table settled, in one screenshot, an argument that had been going in circles for two days. The new prompt fixes the incident case outright, lifts the weak one to 9/10, holds the strong one, and costs three times as much per call. Is 9/10 good enough? That's a product question, and reasonable people disagreed. But we were finally disagreeing about a number.

(One detail I appreciate more than I expected: `record_usage` keeps its numbers even when the assert after it fails. Wrong answers cost money too, and they don't get to hide the bill.)

**Step three: the case never leaves.** Promote v2, delete the v1 arm, keep the benchmark. The incident case is now a permanent sentinel; every future prompt tweak reruns it ten times. In CI we gate on the fraction rather than on perfection, off the plugin's JSON report:

```bash
pytest benchmarks/ --prob-runs=10 --prob-json=report.json || true
jq -e '.rows[] | select(.case == "triage::refund") | .pass_rate >= 95' \
  report.json || { echo "incident case regressed"; exit 1; }
```

## Wrong answer and broken harness are different bugs

One more thing repetition surfaces. Once you run cases ten times, some misses turn out not to be the model's fault at all. The plugin splits every run into three classes, and they fall straight out of Python: a clean return passes, an `AssertionError` fails (the model answered wrong), anything else errors (the harness broke — rate limit, timeout, expired key).

```
  triage::refund   6/10  FLAKY        <- nondeterminism: go do prompt work
  api::summarize   7/10  3 ERRORED    <- model never answered wrong; infra ate 3 runs
```

A normal test suite collapses both into the same red X. I have personally spent an afternoon "improving" a prompt whose only problem was a rate limit. The word `ERRORED` would have saved me that afternoon.

## Writing the cases first

Everything above starts from an incident, because that's where most teams meet this. The better version, which I manage maybe half the time, is writing the cases before the prompt exists. The case list is the behavior spec — the thing TDD always claimed tests should be. Your first run comes back `0/10` everywhere, which is an honest red, and then prompts climb the fractions while the cost column keeps score of what each point of accuracy costs you.

Half the time. I'm working on it.

## Try it on one test

The tooling stays out of the way on purpose: cases are `@pytest.mark.parametrize`, outcomes are plain `assert` (with pytest's assertion introspection intact), selection is `-k` and `-m`. The plugin adds the one thing pytest can't say on its own — run it N times, report the fraction, the class of every miss, and the bill.

```bash
pip install pytest-probability
```

Rename one flaky-ish test to `bench_`, run it with `--prob-runs=10`, and meet your actual pass rate. Docs, including a longer version of this workflow, live at [pytest-probability.readthedocs.io](https://pytest-probability.readthedocs.io/en/latest/bdd.html).

You might not like the number. It was always the number, though. The only thing you get to choose is whether you find out before your users do.
