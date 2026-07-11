# Your LLM Broke in Production. Do These 7 Things Before You Touch the Prompt.

## A benchmark-driven incident runbook — because "cannot reproduce" is a sample size of one, and hotfixed prompts are how you get next month's incident.

It's 4:40 on a Thursday. Your LLM feature just did something wrong in front of a real user — misrouted a ticket, hallucinated a refund policy, mangled an extraction. Every instinct you have says the same thing: *open the prompt, make it better, ship.*

That instinct is how LLM systems rot. You'll change the prompt, try the failing input twice, see two right answers, and declare victory — without ever knowing whether you fixed a 40% failure or just rolled dice until they came up sixes. Worse: you'll have no idea what your "fix" broke, because nothing measured the cases that used to work.

There's a better runbook, and it fits in the time you'd have spent arguing in Slack. It's benchmark-driven development applied to incidents: **the reproduction of a semantic bug is a fraction, not a red test** — so every step below exists to get you from *anecdote* to *fraction* before any prompt gets edited.

*(Disclosure: I'm the creator of [pytest-probability](https://pypi.org/project/pytest-probability/), the pytest plugin used below — read the tooling with that bias in mind. It's MIT-licensed and free, with no dependencies beyond pytest; the runbook works with any harness that can repeat a test and count.)*

## Step 1: Capture the input before it evaporates

Pull the *exact* input from your logs or traces — verbatim, whitespace and all — plus the configuration that served it: model, temperature, prompt version, any context that was stuffed alongside it.

Do not paraphrase. Semantic bugs live in the *shape* of an input — a phrasing, a length, an odd token — and a cleaned-up summary of the input is a different input. Paraphrase the repro and you'll spend the afternoon investigating a case that doesn't exist.

## Step 2: Do NOT retry it in the playground

This is the step everyone skips, which is why it's a step.

Pasting the input into a playground and running it once tells you *nothing*. If the true failure rate on this input is 40%, a single retry shows the right answer six times out of ten — and "works for me" plus a closed ticket is exactly how this incident becomes a recurring series. One run is not a reproduction attempt. It's a coin flip you're planning to make load-bearing.

Skip the playground. Go to step 3.

## Step 3: Turn the incident into a case — named after the ticket

A benchmark case is a pytest parameter. Put the production input in verbatim, pin the expected output, and use the ticket number as the id so the lineage survives forever:

```python
# bench_triage.py
import pytest

@pytest.mark.parametrize("text,expected", [
    # production incident, verbatim from trace 7f3a…
    pytest.param("my card was charged twice", "billing", id="INC-4213"),
    # the cases you already believe in ride along as a control group
    pytest.param("i cannot reset my password", "account", id="password"),
    pytest.param("the box arrived two weeks late", "shipping", id="late_box"),
])
def bench_triage(text, expected):
    assert triage(text) == expected
```

Note the control group. The incident case tells you if you've reproduced the bug; the cases that currently work tell you — later — whether your fix broke anything. Both matter.

## Step 4: Sample it, then read the fraction like a diagnosis

```
$ pytest bench_triage.py --prob-runs=10

  triage::INC-4213-v1   6/10  $0.0002  FLAKY
  triage::password-v1   8/10  $0.0002  FLAKY
  triage::late_box-v1  10/10  $0.0002

  Overall: 24/30 passed (80%)
```

The fraction is a differential diagnosis. Read it like one:

- **`0/10`** — deterministic failure. Good news, weirdly: this is a classical bug. Use classical tools.
- **`1–9/10 FLAKY`** — distributional failure. This is prompt/model work, and you now know the base rate you have to beat.
- **`N ERRORED`** — the model never answered wrong; your *harness* is failing (rate limits, timeouts, expired keys). Page the platform team, not the prompt engineer.
- **`10/10`** — your capture is wrong. The bug is real (a user saw it), so if the verbatim input passes every time, something differs between your bench and production: temperature, truncated context, a stale prompt version. Go back to step 1 and diff the configs.

Notice the collateral finding above: `password` at `8/10` was quietly broken too, and nobody had filed a ticket. Sampling finds the incidents you haven't had yet.

## Step 5: Set the bar before you experiment

Before you write prompt v2, write the acceptance criteria — while you're still objective:

> Ship the fix if: `INC-4213` ≥ 95%, no control case regresses, cost ≤ 3× current.

This is pre-registration, borrowed from science, and it exists for the same reason: once you've spent two hours on a candidate prompt, "8/10 is probably fine" starts sounding reasonable. Decide what fine means before you're emotionally invested in the answer.

## Step 6: Make the fix fight the incumbent

Never edit the prompt in place. The candidate goes on a parametrize axis *next to* the current prompt, so both face identical cases at identical sample sizes, with cost attached:

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
  triage::INC-4213-v1   6/10  $0.0002  FLAKY
  triage::INC-4213-v2  10/10  $0.0006
  triage::password-v1   8/10  $0.0002  FLAKY
  triage::password-v2   9/10  $0.0006  FLAKY
  triage::late_box-v1  10/10  $0.0002
  triage::late_box-v2  10/10  $0.0006
```

Check it against the bar from step 5: incident case fixed outright, control cases held or improved, cost 3× — inside the ceiling. Ship it. If it hadn't cleared the bar, you'd iterate v3 against the same table instead of arguing about whose three manual tries felt better.

## Step 7: Promote, plant the sentinel, close the ticket with numbers

Promote v2 and delete the v1 arm — but the benchmark stays forever. `INC-4213` is now a permanent regression sentinel: every future prompt tweak re-runs it ten times, whether or not anyone remembers the original incident. Gate it in CI off the JSON report:

```bash
pytest benchmarks/ --prob-runs=10 --prob-json=report.json || true
jq -e '.rows[] | select(.case == "triage::INC-4213") | .pass_rate >= 95' \
  report.json || { echo "INC-4213 regressed"; exit 1; }
```

Then close the ticket the way this methodology teaches you to close every ticket — with fractions, not adjectives:

> **INC-4213 resolved.** Reproduced at 6/10 on prompt v1. Fixed by v2: 10/10 on the incident case, password 8/10→9/10, late_box held at 10/10, cost 3× (within budget). Guarded in CI at ≥95%.

Compare that to *"cannot reproduce"* and you'll understand why this runbook exists.

## The checklist

1. **Capture** the input verbatim, plus model/params/prompt version.
2. **Don't** retry it once in a playground.
3. **Case** it — `pytest.param(..., id="INC-XXXX")` — with a control group.
4. **Sample** ×10 and diagnose: `0/10` debugger · `k/10` prompt work · `ERRORED` infra · `10/10` bad capture.
5. **Pre-register** the bar: target fraction, no regressions, cost ceiling.
6. **Fight** candidate vs incumbent on an axis; judge by the table.
7. **Sentinel** forever; gate CI on the fraction; close the ticket with numbers.

```bash
pip install pytest-probability
```

The whole thing is ordinary pytest — cases are `parametrize`, outcomes are `assert`, and the plugin adds what pytest can't say alone: run it ten times, and report the probability, the class of every miss, and the bill. Docs at [pytest-probability.readthedocs.io](https://pytest-probability.readthedocs.io/en/latest/bdd.html).

Next time production breaks at 4:40 on a Thursday, you'll have a fraction by 5:00, a measured fix by 5:30, and a sentinel by 5:31 — and you will never again close a semantic bug with the words "cannot reproduce."
