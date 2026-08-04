# Preregistration: Do abbreviations save Gemini tokens?

Status: frozen before the first successful Gemini experiment request.

## Research questions

1. Do common and invented abbreviations reduce Gemini input-token counts?
2. How many repetitions are needed to repay the token cost of a definition?
3. In complete prompts, do abbreviations reduce input tokens, total usage, and
   dollar cost?
4. Does aggressive abbreviation reduce task accuracy?

The phrase "save tokens" will not be treated as one outcome.  Input tokens,
visible output tokens, thinking tokens, total tokens, dollar cost, and cost per
correct answer will be reported separately.

## Frozen conditions

- `full`: unabbreviated natural language.
- `abbr_defined`: every eligible domain term is replaced and a four-entry
  definition legend is prepended.
- `abbr_undefined`: the same replacements without a legend.
- `concise`: short readable instructions with generic field names and no
  initialisms.  This is a practical control, not part of the causal
  full-versus-abbreviation comparison.

All causal variants come from deterministic string substitutions.  They do not
delete rules, change record values, or reorder records.

## Experiment 1: lexical audit

The corpus contains 40 hand-authored pairs in four equally sized categories:
standard initialisms, conventional shortenings, ambiguous initialisms, and
invented aliases.  Each pair is counted standalone, in a sentence, and beside
punctuation.  The list is frozen before token counts are observed.

Primary measures:

- paired token difference, `full_tokens - short_tokens`;
- percentage of pairs for which shorthand uses fewer, equal, or more tokens;
- relationship between character reduction and token reduction.

Token counts are deterministic for a fixed request and model, so unique inputs
are counted once.  Models are analyzed separately.

## Experiment 2: definition break-even

For each standard initialism and invented alias, compare a full-form prompt to
a shorthand prompt containing an explicit definition.  Repeat the term 1, 2,
4, 8, 16, and 32 times.  The primary measure is the smallest repetition count
where the complete shorthand prompt uses fewer tokens.

A breadth arm combines 1, 4, or 10 invented aliases, each repeated 1, 2, 4, 8,
16, or 32 times.  This tests whether introducing many lightly used aliases has
the same economics as repeatedly using one alias.

## Experiment 3: realistic prompt counts

The deterministic corpus contains 32 cases: eight domains crossed with 6, 12,
24, and 48 records.  Count the complete prompt under all four conditions.

Primary measure: paired percentage change in input tokens from `full`, with the
case—not the API request—as the sampling unit.

## Experiment 4: end-to-end generation

Every case has a mechanically computed gold set of record IDs.  Gemini must
return one JSON object with an `answer` array.  Scoring ignores array ordering
but rejects missing IDs, extra IDs, invalid JSON, safety blocks, and malformed
schemas.  Transport errors and truncations are reported separately rather than
scored as semantic failures.

Initial sample size: 20 independent calls for every case-condition cell on the
primary model (2,560 calls).  Conditions are interleaved using a fixed shuffled
schedule, calls have no prior conversation state, and the generation settings
are identical across conditions.  A second model is a replication and will not
be pooled with the primary model.

Primary quality comparison: `abbr_defined` versus `full`.

Practical non-inferiority margin: abbreviation accuracy may be at most five
percentage points lower than full prose.  An abbreviation protocol will be
called practically beneficial only if it is non-inferior on accuracy and has a
lower observed cost per correct response.

## Generation controls

- Temperature and thinking level are explicitly fixed and recorded.
- No tools, search, cache, files, or previous interaction are used.
- Output schema and maximum output tokens are identical across conditions.
- Requests are randomly interleaved rather than run condition-by-condition.
- Exact requests, responses, model version, SDK version, timestamps, latency,
  usage metadata, errors, and scorer outcomes are retained as JSONL.
- API keys and authorization headers are never written to results.

## Analysis

Report both micro-averages over calls and macro-averages over cases.  Confidence
intervals for condition differences use a case-clustered bootstrap: sample
cases with replacement and retain all repetitions belonging to each sampled
case.  Repeated calls to one case are not presented as independent task
coverage.

Prices are snapshotted from the official Gemini price page on the execution
date.  Input, cached input, visible output, and thinking are costed according to
that snapshot.  Because token prices can differ, raw total-token count is not
used as a substitute for dollars.

No model, condition, mapping, prompt, threshold, or exclusion rule may be
changed after successful API results are inspected without incrementing the
corpus version and labeling the new run exploratory.

## Protocol amendment 1: output budget

Recorded 2026-08-03 after a 1,280-call configuration pilot and before the
confirmatory run.

The pilot used `max_output_tokens=512`.  Although the requested JSON responses
were short, Gemini 3.6 Flash shared this allowance with hidden thinking.  All
238 apparent wrong answers ended with `MAX_TOKENS`; most contained empty or
partial JSON and used approximately 489 thought tokens.  Eight otherwise
correct responses also ended at the cap.  There were no complete, valid JSON
answers with an incorrect record selection.

This is a configuration truncation, not evidence about abbreviation
comprehension.  In accordance with the pre-existing rule that truncations are
reported separately from semantic failures:

- the 512-token pilot is retained under a `pilot-` result filename but excluded
  from confirmatory accuracy analysis;
- the confirmatory output allowance is 2,048 tokens for every condition;
- any response ending in `MAX_TOKENS` is recorded as `truncated`, excluded from
  semantic accuracy, and reported as a separate completion outcome;
- the corpus, conditions, prompts, gold answers, temperature, thinking level,
  model, scorer, and planned 20 repetitions are unchanged.

This amendment was triggered solely by the finish reason and partial output,
not by a condition comparison.  The pilot's uncorrected apparent accuracies
were: full 81.56%, defined abbreviation 84.06%, undefined abbreviation 80.31%,
and concise 79.69%.  Those figures are disclosed to make the amendment fully
auditable and must not be presented as semantic accuracy results.

## Protocol amendment 2: confirmatory repetitions

Recorded 2026-08-03 after 10 corrected repetitions per case-condition cell.

The original plan called for 20 repetitions.  The invalid 512-token pilot used
the inference budget that had been estimated for the entire study.  Ten
corrected repetitions cost $4.64 at paid standard list rates; together with the
preserved pilot and configuration checks, generation usage reached $8.99, the
previously communicated $9 target.  Runs 11–20 were therefore not executed.

This stop was decided after inspecting the 10-run checkpoint, so the corrected
generation study must be described as an amended, budget-limited study rather
than a fully preregistered 20-run study.  At the checkpoint:

- all 1,280 corrected responses were scorable and correct;
- there were zero truncations and zero API errors;
- cost effects varied more between the 32 cases than between repeated calls to
  the same case, so additional repetitions would not add task diversity; and
- another 1,280 calls were projected to cost approximately $4.64.

All observed estimates and case-clustered confidence intervals are reported;
no threshold or scorer was changed as part of this stopping decision.
