# Do Abbreviations Save AI Tokens?

## A Gemini experiment: standard initialisms helped, familiar shortenings did not, and concise English won on cost.

<!-- medium-topics: Artificial Intelligence, Large Language Models, Programming, Machine Learning, Software Development -->

Abbreviations reduced Gemini input tokens, but they did **not** produce a reliable overall cost saving in this benchmark. Familiar shortenings such as `config`, `docs`, `repo`, and `app` usually saved nothing; standard initialisms such as `API` and `FAQ` did. Defining an alias took roughly 8–16 reuses to repay. Concise, readable language was the clear winner: it cut input tokens by 30.28% and total cost by 6.47%. The practical conclusion is simple: write clearly and concisely first; abbreviate only a repeated phrase whose exact token saving you have measured.

## The experiment

I tested both isolated terms and complete prompts with Gemini. First, I counted 40 full-form/abbreviation pairs in three contexts, then measured the cost of defining and reusing aliases at 1, 2, 4, 8, 16, and 32 repetitions. That produced 644 token-count inputs, run on Gemini 3.6 Flash and repeated on Gemini 3.5 Flash-Lite. The two models returned the same count on every input.

For the prompt experiment, I created 32 mechanically scored tasks: eight domains crossed with prompts containing 6, 12, 24, or 48 records. Each task asked Gemini to apply three rules and return matching record IDs as JSON. Gold answers came from code, not an LLM judge.

Each task had four versions:

- **Full prose:** `customer support request`, `priority level`, `response deadline`, `escalation status`.
- **Defined abbreviations:** `CSR`, `PL`, `RD`, and `ES`, plus a four-line legend.
- **Undefined abbreviations:** the same aliases without the legend.
- **Concise language:** readable generic fields such as `score`, `day`, and `state`, with no acronym soup.

### A concrete task

Here is one actual six-record support task. The model had to return IDs whose priority was at least 3, response deadline was day 10 or earlier, and escalation status was `required`. The correct answer was `{"answer": ["R01"]}`.

| ID | Priority level | Response deadline | Escalation status |
|---|---:|---:|---|
| R01 | 5 | day 1 | required |
| R02 | 1 | day 30 | not required |
| R03 | 4 | day 4 | pending |
| R04 | 4 | day 28 | pending |
| R05 | 4 | day 20 | pending |
| R06 | 4 | day 21 | required |

Here are the measured totals for that exact task: the mean of its 10 corrected generation calls. Total-token entries are mean ± standard error. The defined version was 23% shorter in characters, but it used **22.7 more total tokens** than full prose.

| Form | **Mean total tokens ± SE** | Change vs. full |
|---|---:|---:|
| Full prose | **446.3 ± 11.2** | baseline |
| Defined abbreviations | **469.0 ± 12.3** | +22.7 (+5.1%) |
| Undefined abbreviations | **436.7 ± 13.8** | -9.6 (-2.2%) |
| Concise language | **350.6 ± 7.9** | -95.7 (-21.4%) |

For each non-full version, I used a two-sided Welch two-sample t-test on total tokens versus the 10 full-prose calls:

- Defined abbreviations: *t*(17.9) = 1.37, *p* = 0.188; not distinguishable from full prose.
- Undefined abbreviations: *t*(17.3) = -0.54, *p* = 0.596; not distinguishable from full prose.
- Concise language: *t*(16.2) = -6.98, *p* = 0.0000029; lower total-token use.

At a 0.05 threshold, only concise language is significant for this task. These are uncorrected exploratory comparisons of repeated runs on one frozen task, not a claim that the effect generalizes to every workload.

These are the exact four request bodies. The records and decision rule are identical; only the wording changes.

#### Full prose — 247 tokens

```text
Review every customer support request. A customer support request qualifies only when all three rules hold:
1. Its priority level is at least 3.
2. Its response deadline is day 10 or earlier.
3. Its escalation status is exactly "required".

Records:
- R01 — priority level: 5; response deadline: day 1; escalation status: required.
- R02 — priority level: 1; response deadline: day 30; escalation status: not required.
- R03 — priority level: 4; response deadline: day 4; escalation status: pending.
- R04 — priority level: 4; response deadline: day 28; escalation status: pending.
- R05 — priority level: 4; response deadline: day 20; escalation status: pending.
- R06 — priority level: 4; response deadline: day 21; escalation status: required.

Return only a JSON object of the form {"answer": ["R01", "R02"]}.
The answer must contain every qualifying record ID in ascending order and no others.
```

#### Defined abbreviations — 252 tokens

```text
Abbreviation legend:
- CSR = customer support request
- PL = priority level
- RD = response deadline
- ES = escalation status

Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 3.
2. Its RD is day 10 or earlier.
3. Its ES is exactly "required".

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 4; RD: day 4; ES: pending.
- R04 — PL: 4; RD: day 28; ES: pending.
- R05 — PL: 4; RD: day 20; ES: pending.
- R06 — PL: 4; RD: day 21; ES: required.

Return only a JSON object of the form {"answer": ["R01", "R02"]}.
The answer must contain every qualifying record ID in ascending order and no others.
```

#### Undefined abbreviations — 222 tokens

```text
Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 3.
2. Its RD is day 10 or earlier.
3. Its ES is exactly "required".

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 4; RD: day 4; ES: pending.
- R04 — PL: 4; RD: day 28; ES: pending.
- R05 — PL: 4; RD: day 20; ES: pending.
- R06 — PL: 4; RD: day 21; ES: required.

Return only a JSON object of the form {"answer": ["R01", "R02"]}.
The answer must contain every qualifying record ID in ascending order and no others.
```

#### Concise language — 158 tokens

```text
Select every record satisfying all conditions:
score >= 3; day <= 10; state = "required".

Records:
- R01: score=5; day=1; state=required.
- R02: score=1; day=30; state=not required.
- R03: score=4; day=4; state=pending.
- R04: score=4; day=28; state=pending.
- R05: score=4; day=20; state=pending.
- R06: score=4; day=21; state=required.

Return only {"answer": [record IDs]} with qualifying IDs in ascending order.
```

The concise version made the task both shorter and readable. [The appendix](abbreviation-experiment-appendix.html) contains all 32 frozen tasks and all 128 exact prompt variants.

The variants were exact string substitutions: no condition lost a rule, changed a value, or reordered a record. Model, temperature, thinking level, output schema, and scorer stayed fixed. I ran each case-condition combination 10 times, for 1,280 corrected generation calls.

## Discussion

### Most familiar shortenings saved zero tokens

The lexical result split cleanly by abbreviation type:

| Type | Uses fewer tokens | Equal | Uses more | Mean tokens saved |
|---|---:|---:|---:|---:|
| Standard initialisms | 30/30 | 0 | 0 | 1.80 |
| Ambiguous initialisms | 27/30 | 3 | 0 | 1.20 |
| Invented aliases | 27/30 | 3 | 0 | 0.93 |
| Conventional shortenings | 1/30 | 26 | 3 | -0.07 |

Each row covers ten terms in three contexts. `Frequently asked questions` became three tokens cheaper as `FAQ`, and `application programming interface` saved two as `API`. But the programmer-style shortenings mostly did nothing:

| Full form | Short form | Token difference |
|---|---|---:|
| configuration | config | 0 |
| application | app | 0 |
| documentation | docs | 0 |
| repository | repo | 0 |
| authentication | auth | 0 |
| request | req | 0 |
| response | resp | 0 |
| synchronization | sync | 1 saved |
| authorization | authz | 1 extra |

Character count is the wrong proxy. Common full words can already be single vocabulary units; an awkward abbreviation such as `authz` can split into more tokens.

### Definitions are an upfront cost

An unexplained `API` may be fine. An invented `X4` needs a definition, and that definition must be repaid before the alias saves anything. Standard initialisms first became cheaper after a median of **8 uses**; invented aliases needed **16 uses**.

One alias, `X10`, never broke even: its short form used the same number of tokens as the full phrase, so the definition remained permanent overhead. With ten invented aliases, the compressed prompt was still 29 tokens larger at eight uses per alias; it became 43 tokens smaller at 16 uses and 187 smaller at 32.

### Prompt compression was real; cheaper total use was not

The complete prompts showed why a legend is costly on short tasks:

| Records | Full | Defined | Undefined | Concise |
|---:|---:|---:|---:|---:|
| 6 | 246.4 | 252.1 (+2.3%) | 221.9 (-9.9%) | 158.2 (-35.8%) |
| 12 | 395.1 | 382.9 (-3.1%) | 352.6 (-10.8%) | 271.4 (-31.3%) |
| 24 | 692.6 | 644.4 (-7.0%) | 614.1 (-11.3%) | 498.5 (-28.0%) |
| 48 | 1287.8 | 1167.5 (-9.3%) | 1137.2 (-11.7%) | 952.9 (-26.0%) |

Across all 32 tasks, weighted equally, defined abbreviations reduced input tokens by **4.27%**; undefined abbreviations reduced them by **10.93%**; concise language reduced them by **30.28%**. Abbreviations can compress a prompt, but concise writing did far more.

Input tokens were also the cheap part. At the time of the experiment, Gemini 3.6 Flash listed input at $1.50 per million tokens and output—including thinking—at $7.50 per million. ([Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [token usage fields](https://ai.google.dev/gemini-api/docs/tokens)) Saving input can disappear if the model uses a few extra thought tokens.

| Condition | Input | Visible output | Thinking | Total | Cost per call |
|---|---:|---:|---:|---:|---:|
| Full prose | 655.5 | 22.4 | 345.2 | 1023.0 | $0.003740 |
| Defined abbreviations | 611.7 | 23.7 | 349.1 | 984.6 | $0.003714 |
| Undefined abbreviations | 581.5 | 22.6 | 353.7 | 957.7 | $0.003694 |
| Concise language | 470.2 | 21.8 | 331.6 | 823.7 | $0.003356 |

Pooling all tokens makes defined abbreviations look 0.7% cheaper and undefined abbreviations 1.2% cheaper. But that overweights the largest prompts. With each task weighted equally and a case bootstrap:

| Condition | Mean cost change | 95% case-bootstrap interval |
|---|---:|---:|
| Defined abbreviations | +1.72% | -1.81% to +5.16% |
| Undefined abbreviations | +0.66% | -2.82% to +4.13% |
| Concise language | **-6.47%** | **-11.19% to -2.06%** |

Both abbreviation intervals cross zero, so this experiment cannot distinguish either from no overall cost change. Concise language is the only condition with a clear saving.

### A measurement trap worth avoiding

My first 1,280-call pilot looked like a quality tradeoff: full prose was 81.56% correct, defined abbreviations 84.06%, undefined abbreviations 80.31%, and concise language 79.69%. That result was false. I had set `max_output_tokens` to 512; hidden thinking used the allowance before the visible JSON could finish. Every scored miss ended with `MAX_TOKENS`.

I preserved the pilot, raised the uniform allowance to 2,048, and reran it. The corrected result was **1,280 correct, zero incorrect, zero truncated, and zero API errors**. There was no abbreviation-quality tradeoff in these tasks—only an output-budget bug. Check finish reasons and thinking usage before treating malformed output as a comprehension failure.

## Actions

1. **Write concise, readable instructions first.** It delivered the largest input reduction and the only clear overall cost reduction.
2. **Count the exact request.** Use the model's token-count endpoint; do not estimate from characters or word length.
3. **Abbreviate repeated multi-token phrases, not familiar-looking long words.** `FAQ` helped; `config`, `docs`, and `repo` did not.
4. **Charge the legend to the optimization.** In this corpus, a defined alias needed roughly 8–16 uses before it won.
5. **Measure total usage and dollars.** Input, output, thinking, and cached tokens can have different prices.
6. **Log finish reasons.** A truncated response is not evidence that the model misunderstood the prompt.

I would not turn a production prompt into `cfg usr req resp` because it looks compact. I would generate both versions, count both exact requests, and keep the shorthand only if it reduces measured cost on the actual workload without moving the quality distribution.

Everything is reproducible—the frozen corpus, prompts, runner, protocol amendments, result checksums, and discarded pilot—at [github.com/xu-hao/articles/tree/main/abbreviation-experiment](https://github.com/xu-hao/articles/tree/main/abbreviation-experiment). I planned 20 corrected repetitions per cell but stopped at 10 after the invalid pilot consumed the original budget; the amendment and its implications are documented there. Total generation usage was $8.99 at paid list prices, including the discarded pilot.
