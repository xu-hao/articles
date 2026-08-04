# Gemini abbreviation experiment

Reproducible companion experiment for an article asking whether extensive use
of abbreviations actually saves LLM tokens.

The study separates lexical token compression, definition break-even, complete
prompt compression, model accuracy, and end-to-end cost.  The frozen hypotheses
and exclusion rules are in [preregistration.md](preregistration.md).

## Safety

Credentials are loaded at runtime from an env file and are never copied into
this directory or serialized to results.  Raw result files contain only the
synthetic prompts, model outputs, token metadata, and errors with the active
credential redacted.

## Corpus

```bash
cd abbreviation-experiment
python experiment.py manifest
python -m unittest -v
```

The corpus contains 40 lexical pairs, 20 definition break-even mappings, a
breadth/repetition grid, and 32 mechanically scored tasks under four prompt
conditions.  `manifest` performs no API calls.

## Token-count experiments

```bash
python experiment.py count \
  --env-file /path/to/your/.env \
  --model gemini-3.6-flash
```

The command is resumable.  Successful job IDs already present in the JSONL are
skipped.  Use `--limit 3 --output /tmp/count-smoke.jsonl` for a credential and
schema smoke test before the full run.

## End-to-end experiment

```bash
python experiment.py generate \
  --env-file /path/to/your/.env \
  --model gemini-3.6-flash \
  --runs 20
```

The default schedule contains 2,560 calls, shuffled across cases and
conditions.  Use a separate output file when piloting with `--limit`, so the
fixed full-run schedule remains easy to audit.

The confirmatory protocol uses a 2,048-token output allowance.  A 512-token
pilot showed that Gemini's hidden thinking could consume nearly the entire
allowance before JSON was emitted; see protocol amendment 1 in the
preregistration.  Responses ending with `MAX_TOKENS` are reported as
truncations, not semantic errors.

For Vertex AI with application-default credentials:

```bash
python experiment.py count \
  --backend vertex \
  --env-file /path/to/your/.env \
  --model gemini-3.6-flash
```

## Analysis

```bash
python experiment.py analyze
```

This writes `results/summary.md`.  The analysis pairs exact prompts for token
comparisons and uses a case-clustered bootstrap for accuracy differences.
