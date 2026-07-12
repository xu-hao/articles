# TDD Doesn't Work on LLM Code. Here's What Does.

## Benchmark-Driven Development: red is a fraction, green is a probability bar, and "cannot reproduce" stops being a resolution.

Test-driven development is the best feedback loop our industry ever built. Write a failing test, make it pass, refactor with a safety net, keep the test forever. Red, green, refactor — a metronome you can build a career on.

Then you add one LLM call to your codebase, and the metronome quietly breaks.

Not loudly. That's the problem. The tests still run. The checkmarks still turn green. But the instrument underneath — the `assert`, which reads *true or false* — is now pointed at something that doesn't have a true-or-false answer. It has a **distribution**. A prompt that classifies support emails correctly 70% of the time will pass your test on Monday, fail it on Tuesday, and pass again after someone hits re-run. So your team does what every team does: adds a retry to CI, mutters "flaky," and merges.

You didn't test the feature. You sampled it once and rounded to `True`.

## The incident every LLM team eventually has

Here's how the broken loop actually bites. A support-triage bot misroutes a real customer email — *"my card was charged twice"* lands in the wrong queue for two days. An engineer grabs the exact message, pastes it into the playground, runs it.

It answers correctly.

Runs it again. Correct again. Ticket closed: **cannot reproduce.**

Three weeks later it happens again — because there was never a bug that "happens on this input." There was a prompt that's a *coin flip* on this shape of input, and production kept sampling until it hit the bad side. The playground retry wasn't a verification; it was two lucky coin flips.

That's the moment TDD's instrument fails completely. A semantic bug — a bug in code whose behavior is a model call — won't reproduce in one run. **The reproduction of a semantic bug is a fraction, not a red test.**

## The instrument swap

Benchmark-driven development keeps TDD's loop and swaps the instrument. The unit of feedback stops being the boolean and becomes the **pass fraction**:

- **Red** is a low fraction: `6/10 FLAKY` — not a red cross.
- **Green** is a fraction meeting a bar *you chose*: `10/10`, or ≥95% by policy. Perfection is a product decision, not a default.
- **Refactor** means changing the prompt or model — and proving it against the incumbent on the same cases, the same sample size, with the cost of the improvement printed next to it.
- The benchmark **stays forever**, exactly like the regression test you keep after fixing a classical bug. Every future prompt tweak re-samples it.

Same discipline. Same rhythm. One honest number instead of one lucky boolean.

## The loop, on a real incident

I maintain a small pytest plugin, [pytest-probability](https://pypi.org/project/pytest-probability/), built so this loop costs nothing to adopt — a benchmark is a pytest test body with a `bench_` prefix. Here's BDD applied to the misrouted email, end to end.

*(Disclosure: I'm the creator of pytest-probability — this article describes the methodology I built it for, so read the tooling recommendations with that bias in mind. The plugin is MIT-licensed and free, with no dependencies beyond pytest; the methodology itself works with any harness that can repeat a test and count.)*

**Step 1 — Reproduce: the incident becomes a case.** Take the production input verbatim, pin the expected label, and *sample* it instead of running it once:

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

Reproduced — four times out of ten. And the sampling caught a *second* liability (`password`, 8/10) nobody had filed a ticket for yet. This is the red state, and unlike a red test, it tells you how red.

**Step 2 — Fix: candidates fight the incumbent on an axis.** The failure mode of prompt engineering is swapping in a new prompt because it "felt better" in three manual tries. BDD forbids vibes: the candidate goes on a parametrize axis *next to* the current prompt, so both face identical cases at identical sample sizes:

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

This table is the entire prompt-review meeting. The candidate fixes the incident outright, lifts the second weak case, holds the strong one — at three times the token cost. Whether 9/10 clears your bar is a product call. The point is you're making it with numbers, and the numbers have prices.

**Step 3 — Guard: the case becomes a sentinel.** Promote v2, delete the v1 arm, keep the benchmark. In CI, gate on the fraction you care about rather than on perfection:

```bash
pytest benchmarks/ --prob-runs=10 --prob-json=report.json || true
jq -e '.rows[] | select(.case == "triage::refund") | .pass_rate >= 95' \
  report.json || { echo "incident case regressed"; exit 1; }
```

Your pass rate just became a monitored metric — measured before your users measure it for you.

## Red has three colors now

One more thing repetition surfaces that single-shot testing structurally cannot: not every miss means your prompt is bad. In BDD, every run lands in one of three classes, falling straight out of Python — a clean return **passes**, an `AssertionError` **fails** (your code answered wrong), any other exception **errors** (your harness broke):

```
  triage::refund   6/10  FLAKY        ← nondeterminism: do prompt work
  api::summarize   7/10  3 ERRORED    ← the model never answered wrong; infra dropped 3 runs
```

`FLAKY` sends you to the prompt. `ERRORED` sends you to whoever owns the API gateway. Conventional suites collapse both into one red X — and engineers fix the wrong thing.

## Greenfield BDD: cases before prompts

Everything above started from an incident, because that's where most teams meet the loop. But run it from the start and it gets better: **write the cases before the prompt.** The case list *is* the behavior spec — the thing TDD always promised tests would be. Your first run is `0/10` across the board; that's your honest red. Then prompts climb the fractions, the cost column keeps score of what each point of accuracy costs, and by the time you ship, "how good is it?" has had a numeric answer for weeks.

## You don't need permission to start

The tooling is deliberately boring: cases are `@pytest.mark.parametrize`, outcomes are `assert` (with pytest's full assertion introspection), selection is `-k` and `-m`, and the plugin adds only what pytest can't say — *run it N times; report the probability, the class of every miss, and the cost.* One dependency: pytest.

```bash
pip install pytest-probability
```

Rename one test to `bench_`, run it with `--prob-runs=10`, and meet your real pass rate. Docs at [pytest-probability.readthedocs.io](https://pytest-probability.readthedocs.io) — the [benchmark-driven development guide](https://pytest-probability.readthedocs.io/en/latest/bdd.html) walks the full loop.

You might not like the number. But it was always the number. TDD taught us that feedback beats hope — benchmark-driven development is just that lesson, restated for code that answers in probabilities: **a semantic bug won't reproduce in one run, and can't hide from ten.**

*Companion piece: the incident-response runbook — [Your LLM Broke in Production. Do These 7 Things Before You Touch the Prompt.](before-you-touch-the-prompt.html)*
