# Findings: abbreviations save input tokens, not necessarily money

Experiment date: 2026-08-03
Corpus SHA-256: `60e7a28096726d8200df300e7594bf0716728789de9435f5cd7e8e76b10c7bc9`

## Headline result

Extensive abbreviation reduced Gemini input tokens, but defined abbreviations
did not produce a clear cost saving when every task received equal weight.
Writing concise plain English saved substantially more input and was the only
condition with a statistically clear overall cost reduction.

| Condition | Mean input change | Mean total-token change | Mean cost change (95% case-bootstrap CI) | Correct |
|---|---:|---:|---:|---:|
| Full prose | baseline | baseline | baseline | 320/320 |
| Defined abbreviations | -4.27% | -1.26% | +1.72% [-1.81%, +5.16%] | 320/320 |
| Undefined abbreviations | -10.93% | -5.05% | +0.66% [-2.82%, +4.13%] | 320/320 |
| Concise plain English | -30.28% | -17.92% | -6.47% [-11.19%, -2.06%] | 320/320 |

These are macro results: each of the 32 cases contributes equal weight.  If
token volume is pooled instead, long prompts contribute more observations.  On
that micro basis, the actual experimental bill was 0.7% lower for defined
abbreviations, 1.2% lower for undefined abbreviations, and 10.3% lower for
concise English.  The difference between the two summaries is itself useful:
abbreviations help the long prompts most, while definition overhead makes them
unhelpful on short prompts.

All conditions achieved perfect observed accuracy after configuration
truncations were handled correctly.  This supports only a narrow claim: Gemini
3.6 Flash understood every abbreviation protocol in these objective selection
tasks.  It does not prove that shorthand is harmless on harder or open-ended
work.

## Finding 1: shortenings often shorten characters but not tokens

Forty frozen term pairs were counted in three contexts.  Results were identical
on Gemini 3.6 Flash and Gemini 3.5 Flash-Lite for all 644 complete count jobs,
suggesting that these two models use the same tokenizer for the tested text.

| Category | Context-pairs using fewer tokens | Equal | More | Mean tokens saved |
|---|---:|---:|---:|---:|
| Standard initialisms | 30/30 | 0 | 0 | 1.80 |
| Ambiguous initialisms | 27/30 | 3 | 0 | 1.20 |
| Invented aliases | 27/30 | 3 | 0 | 0.93 |
| Conventional shortenings | 1/30 | 26 | 3 | -0.07 |

Standalone examples make the reason concrete:

- `configuration` and `config` were both two tokens.
- `application` and `app` were both two tokens.
- `documentation` and `docs` were both two tokens.
- `repository` and `repo` were both two tokens.
- `authorization` was two tokens while `authz` was three.
- `synchronization` was three tokens while `sync` was two.
- `frequently asked questions` was five tokens while `FAQ` was two.

Character count is therefore a poor estimator for individual substitutions.
Common long words are already compact vocabulary entries, while an unusual
short string can be split into several tokens.

## Finding 2: a definition has a substantial cover charge

The break-even experiment included the full definition in the abbreviated
prompt and varied reuse from 1 to 32 occurrences.

- Standard initialisms first won after a median of 8 uses.
- Invented aliases first won after a median of 16 uses.
- Nine of ten invented aliases won by 16 uses.
- `X10` never won: it tokenized to the same per-use length as its full phrase,
  leaving the definition as permanent overhead.

Breadth did not rescue lightly reused aliases.  With ten invented definitions,
the abbreviated prompt was 29 tokens larger at eight uses per alias, 43 tokens
smaller at 16 uses, and 187 tokens smaller at 32 uses.  "Use lots of
abbreviations" is the wrong rule.  The relevant variable is repeated token
savings per definition.

## Finding 3: prompt length changes the answer

Mean input tokens by record count were:

| Records | Full | Defined abbreviation | Undefined abbreviation | Concise English |
|---:|---:|---:|---:|---:|
| 6 | 246.4 | 252.1 (+2.3%) | 221.9 (-9.9%) | 158.2 (-35.8%) |
| 12 | 395.1 | 382.9 (-3.1%) | 352.6 (-10.8%) | 271.4 (-31.3%) |
| 24 | 692.6 | 644.4 (-7.0%) | 614.1 (-11.3%) | 498.5 (-28.0%) |
| 48 | 1287.8 | 1167.5 (-9.3%) | 1137.2 (-11.7%) | 952.9 (-26.0%) |

A four-entry legend made the shortest abbreviated prompts larger.  It was
repaid somewhere between 6 and 12 records and became increasingly worthwhile
as the same field names repeated.

## Finding 4: input savings were diluted by thinking tokens

Gemini 3.6 Flash pricing at execution time was $1.50 per million input tokens
and $7.50 per million output tokens, with thinking billed at the output rate.
That five-to-one price ratio means a few extra thought tokens can erase many
saved input tokens.  See the official [Gemini pricing page](https://ai.google.dev/gemini-api/docs/pricing)
and [token usage documentation](https://ai.google.dev/gemini-api/docs/tokens).

Across all calls, average usage was:

| Condition | Input | Visible output | Thinking | Total | Paid-list cost per call |
|---|---:|---:|---:|---:|---:|
| Full prose | 655.5 | 22.4 | 345.2 | 1023.0 | $0.003740 |
| Defined abbreviations | 611.7 | 23.7 | 349.1 | 984.6 | $0.003714 |
| Undefined abbreviations | 581.5 | 22.6 | 353.7 | 957.7 | $0.003694 |
| Concise English | 470.2 | 21.8 | 331.6 | 823.7 | $0.003356 |

The volume-weighted table makes abbreviations look slightly cheaper, but the
case-level effects were heterogeneous.  Observed cost changes by prompt size
were:

| Records | Defined abbreviation | Undefined abbreviation | Concise English |
|---:|---:|---:|---:|
| 6 | +8.6% | +1.7% | -6.3% |
| 12 | +4.7% | +3.0% | +2.3% |
| 24 | -3.4% | +3.7% | +0.5% |
| 48 | -3.7% | -6.9% | -23.5% |

Only some of these size-specific differences are distinguishable from
case-to-case variation.  The robust conclusion is not that one exact threshold
applies universally.  It is that input-token reduction is insufficient to
predict cost: definition overhead, prompt length, thinking, and the output/input
price ratio all matter.

## The configuration failure that almost became a false result

The first generation pilot capped output at 512 tokens.  The requested JSON was
tiny, so the cap looked generous.  It was not: hidden thinking shared the same
allowance.  Every apparent wrong answer ended at `MAX_TOKENS`; most contained
empty or partial JSON after using about 489 thought tokens.  The resulting fake
accuracies ranged from 79.69% to 84.06% by condition.

After the uniform allowance was raised to 2,048:

- 1,280/1,280 confirmatory responses were correct;
- 0 responses were truncated;
- 0 API calls errored; and
- the same prompts and mechanical scorer were used.

The pilot is retained and checksummed, not deleted.  Its lesson belongs in the
article: a token cap can masquerade as a model comprehension failure, and the
finish reason must be inspected before scoring malformed output.

## Execution accounting

- Deterministic counts: 644 requests on each of two models, all successful.
- Corrected generation: 32 cases × 4 conditions × 10 repetitions = 1,280 calls.
- Corrected generation paid-list equivalent: $4.641240.
- Preserved 512-token pilot paid-list equivalent: $4.312432.
- Generation smoke and stress checks: $0.040478.
- Total generation paid-list equivalent incurred: **$8.994150**.

Actual billing can be lower or zero depending on tier.  `count_tokens` requests
are not included in the generation-cost total.  Raw JSONL files remain local;
their hashes are in `results/checksums.sha256`.

## Limitations

- Generation quality was tested on synthetic, mechanically scored selection
  tasks, not prose writing, coding, or ambiguous instructions.
- Generation used one model; tokenizer counts were replicated on two models.
- All corrected outputs were right, so the study found no semantic tradeoff to
  estimate.  Harder tasks may behave differently.
- The confirmatory run stopped at 10 rather than the planned 20 repetitions
  after the invalid pilot consumed the original budget.  This is disclosed as
  protocol amendment 2 rather than presented as fully preregistered.
- The 40 lexical pairs illustrate several abbreviation classes but are not a
  representative sample of every language or domain.
- Prices are a dated snapshot, and batch, cached, free-tier, or future pricing
  can change the economic conclusion.

## Article thesis

The defensible thesis is:

> Abbreviations can save Gemini input tokens, but most everyday shortenings save
> nothing, definitions need roughly 8–16 reuses to break even, and input savings
> do not reliably become cost savings because thinking is both variable and
> more expensive.  If the goal is efficiency, concise plain English beat an
> acronym-heavy protocol.

The clean article structure is:

1. Open with the fake 80% accuracy result caused by the 512-token cap.
2. Show that character shortening and token shortening are different.
3. Introduce the definition break-even curve.
4. Compare full, defined, undefined, and concise prompts end to end.
5. Reveal that thinking tokens erase most acronym savings.
6. End with the practical rule: count the exact request, abbreviate only heavily
   repeated multi-token phrases, and prefer concise readable language first.
