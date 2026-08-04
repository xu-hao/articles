# Abbreviation experiment results

Generated: 2026-08-03T20:11:40.132118+00:00

Count rows: 1288; generation rows: 1280.

## Lexical audit

| Model | Category | Pairs | Fewer | Equal | More | Mean token delta | Median saving |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite | ambiguous_initialism | 30 | 27 | 3 | 0 | 1.20 | 10.00% |
| gemini-3.5-flash-lite | conventional_shortening | 30 | 1 | 26 | 3 | -0.07 | 0.00% |
| gemini-3.5-flash-lite | invented_alias | 30 | 27 | 3 | 0 | 0.93 | 9.09% |
| gemini-3.5-flash-lite | standard_initialism | 30 | 30 | 0 | 0 | 1.80 | 18.18% |
| gemini-3.6-flash | ambiguous_initialism | 30 | 27 | 3 | 0 | 1.20 | 10.00% |
| gemini-3.6-flash | conventional_shortening | 30 | 1 | 26 | 3 | -0.07 | 0.00% |
| gemini-3.6-flash | invented_alias | 30 | 27 | 3 | 0 | 0.93 | 9.09% |
| gemini-3.6-flash | standard_initialism | 30 | 30 | 0 | 0 | 1.80 | 18.18% |

## Definition break-even

| Model | Category | Aliases | Break even by 32 | Median first winning repetition |
|---|---:|---:|---:|---:|
| gemini-3.5-flash-lite | invented_alias | 10 | 9 | 16.0 |
| gemini-3.5-flash-lite | standard_initialism | 10 | 10 | 8.0 |
| gemini-3.6-flash | invented_alias | 10 | 9 | 16.0 |
| gemini-3.6-flash | standard_initialism | 10 | 10 | 8.0 |

## Complete prompt counts

| Model | Condition | Cases | Mean input saving | Median input saving |
|---|---:|---:|---:|---:|
| gemini-3.5-flash-lite | abbr_defined | 32 | 4.27% | 4.99% |
| gemini-3.5-flash-lite | abbr_undefined | 32 | 10.93% | 11.05% |
| gemini-3.5-flash-lite | concise | 32 | 30.28% | 29.30% |
| gemini-3.6-flash | abbr_defined | 32 | 4.27% | 4.99% |
| gemini-3.6-flash | abbr_undefined | 32 | 10.93% | 11.05% |
| gemini-3.6-flash | concise | 32 | 30.28% | 29.30% |

## End-to-end generation

Scorable responses: 1280; truncations: 0; infrastructure errors: 0.

| Model | Condition | Runs | Accuracy | Mean input | Mean visible output | Mean thoughts | Mean total | Total cost | Cost/correct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.6-flash | abbr_defined | 320 | 100.00% | 611.7 | 23.7 | 349.1 | 984.6 | $1.1884 | $0.003714 |
| gemini-3.6-flash | abbr_undefined | 320 | 100.00% | 581.5 | 22.6 | 353.7 | 957.7 | $1.1821 | $0.003694 |
| gemini-3.6-flash | concise | 320 | 100.00% | 470.2 | 21.8 | 331.6 | 823.7 | $1.0739 | $0.003356 |
| gemini-3.6-flash | full | 320 | 100.00% | 655.5 | 22.4 | 345.2 | 1023.0 | $1.1968 | $0.003740 |

Accuracy differences from full for `gemini-3.6-flash` (case-clustered 95% CI):

- `abbr_defined`: 0.00 percentage points [0.00, 0.00]
- `abbr_undefined`: 0.00 percentage points [0.00, 0.00]
- `concise`: 0.00 percentage points [0.00, 0.00]
