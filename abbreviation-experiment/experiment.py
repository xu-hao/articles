#!/usr/bin/env python3
"""Run and analyze the Gemini abbreviation experiments.

The runner is resumable.  It reads credentials at runtime, never places them in
the process arguments, and never serializes them to the result files.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import random
import statistics
import sys
import time
from typing import Any, Iterable, Iterator

from dotenv import dotenv_values
from google import genai
from google.genai import errors, types

from cases import (
    CONDITIONS,
    LEXICAL_CONTEXTS,
    LEXICAL_MAPPINGS,
    Mapping,
    TaskCase,
    corpus_manifest,
    make_cases,
    render_prompt,
)


ROOT = Path(__file__).resolve().parent
DEFAULT_ENV_FILE = ROOT / ".env"
DEFAULT_RESULTS = ROOT / "results"
REPETITIONS = (1, 2, 4, 8, 16, 32)
SCHEDULE_SEED = 20260803
SDK_VERSION = importlib.metadata.version("google-genai")

# Snapshot from https://ai.google.dev/gemini-api/docs/pricing on 2026-08-03.
# Values are paid standard-tier USD per one million text tokens.  Gemini prices
# output and thinking tokens at the output rate for these models.
PRICE_SNAPSHOT: dict[str, dict[str, float]] = {
    "gemini-3.6-flash": {"input": 1.50, "output": 7.50},
    "gemini-3.5-flash-lite": {"input": 0.30, "output": 2.50},
}


@dataclass(frozen=True)
class CountJob:
    job_id: str
    experiment: str
    unit_id: str
    variant: str
    text: str
    metadata: dict[str, Any]


@dataclass(frozen=True)
class GenerationJob:
    job_id: str
    case: TaskCase
    condition: str
    repetition: int
    text: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def safe_model_name(model: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in model)


def lexical_jobs() -> Iterator[CountJob]:
    category_indexes: dict[str, int] = defaultdict(int)
    pair_ids: list[str] = []
    for mapping in LEXICAL_MAPPINGS:
        category_indexes[mapping.category] += 1
        pair_ids.append(f"{mapping.category}-{category_indexes[mapping.category]:02d}")

    for mapping, pair_id in zip(LEXICAL_MAPPINGS, pair_ids, strict=True):
        for context_name, template in LEXICAL_CONTEXTS:
            unit_id = f"{pair_id}:{context_name}"
            for variant, term in (("full", mapping.full), ("short", mapping.short)):
                text = template.format(term=term)
                yield CountJob(
                    job_id=f"lexical:{unit_id}:{variant}",
                    experiment="lexical",
                    unit_id=unit_id,
                    variant=variant,
                    text=text,
                    metadata={
                        "pair_id": pair_id,
                        "category": mapping.category,
                        "context": context_name,
                        "full_term": mapping.full,
                        "short_term": mapping.short,
                    },
                )


def _repeated_text(term: str, repetitions: int) -> str:
    return "\n".join(
        f"Item {number:02d} references {term} in the final report."
        for number in range(1, repetitions + 1)
    )


def break_even_jobs() -> Iterator[CountJob]:
    selected = [
        mapping
        for mapping in LEXICAL_MAPPINGS
        if mapping.category in {"standard_initialism", "invented_alias"}
    ]
    category_indexes: dict[str, int] = defaultdict(int)
    for mapping in selected:
        category_indexes[mapping.category] += 1
        pair_id = f"{mapping.category}-{category_indexes[mapping.category]:02d}"
        for repetitions in REPETITIONS:
            unit_id = f"{pair_id}:r{repetitions:02d}"
            full_text = _repeated_text(mapping.full, repetitions)
            short_text = (
                f"Definition: {mapping.short} means {mapping.full}.\n"
                + _repeated_text(mapping.short, repetitions)
            )
            common = {
                "pair_id": pair_id,
                "category": mapping.category,
                "full_term": mapping.full,
                "short_term": mapping.short,
                "repetitions": repetitions,
            }
            yield CountJob(
                job_id=f"break_even:{unit_id}:full",
                experiment="break_even",
                unit_id=unit_id,
                variant="full",
                text=full_text,
                metadata=common,
            )
            yield CountJob(
                job_id=f"break_even:{unit_id}:short",
                experiment="break_even",
                unit_id=unit_id,
                variant="short",
                text=short_text,
                metadata=common,
            )


def breadth_jobs() -> Iterator[CountJob]:
    invented = [mapping for mapping in LEXICAL_MAPPINGS if mapping.category == "invented_alias"]
    for breadth in (1, 4, 10):
        selected = invented[:breadth]
        for repetitions in REPETITIONS:
            unit_id = f"k{breadth:02d}:r{repetitions:02d}"
            full_sections = [
                _repeated_text(mapping.full, repetitions) for mapping in selected
            ]
            legend = "\n".join(
                f"Definition: {mapping.short} means {mapping.full}."
                for mapping in selected
            )
            short_sections = [
                _repeated_text(mapping.short, repetitions) for mapping in selected
            ]
            common = {"breadth": breadth, "repetitions": repetitions}
            yield CountJob(
                job_id=f"breadth:{unit_id}:full",
                experiment="breadth",
                unit_id=unit_id,
                variant="full",
                text="\n".join(full_sections),
                metadata=common,
            )
            yield CountJob(
                job_id=f"breadth:{unit_id}:short",
                experiment="breadth",
                unit_id=unit_id,
                variant="short",
                text=legend + "\n" + "\n".join(short_sections),
                metadata=common,
            )


def prompt_count_jobs() -> Iterator[CountJob]:
    for case in make_cases():
        for condition in CONDITIONS:
            yield CountJob(
                job_id=f"prompt:{case.case_id}:{condition}",
                experiment="prompt",
                unit_id=case.case_id,
                variant=condition,
                text=render_prompt(case, condition),
                metadata={
                    "case_id": case.case_id,
                    "domain": case.domain.name,
                    "records": case.size,
                },
            )


def all_count_jobs() -> list[CountJob]:
    return list(
        _chain(
            lexical_jobs(),
            break_even_jobs(),
            breadth_jobs(),
            prompt_count_jobs(),
        )
    )


def _chain(*iterables: Iterable[Any]) -> Iterator[Any]:
    for iterable in iterables:
        yield from iterable


def generation_jobs(runs: int) -> list[GenerationJob]:
    jobs = [
        GenerationJob(
            job_id=f"generate:{case.case_id}:{condition}:r{repetition:03d}",
            case=case,
            condition=condition,
            repetition=repetition,
            text=render_prompt(case, condition),
        )
        for case in make_cases()
        for condition in CONDITIONS
        for repetition in range(1, runs + 1)
    ]
    random.Random(SCHEDULE_SEED).shuffle(jobs)
    return jobs


def create_client(args: argparse.Namespace) -> tuple[genai.Client, str | None]:
    env_path = Path(args.env_file).expanduser().resolve()
    values = dotenv_values(env_path)
    if args.backend == "developer":
        key = values.get("GOOGLE_API_KEY") or values.get("GEMINI_API_KEY")
        if not key:
            raise SystemExit(f"No GOOGLE_API_KEY or GEMINI_API_KEY in {env_path}")
        return genai.Client(api_key=key), key

    project = args.project or values.get("GOOGLE_CLOUD_PROJECT")
    location = args.location or values.get("GOOGLE_CLOUD_LOCATION") or "us-central1"
    if not project:
        raise SystemExit("Vertex backend requires --project or GOOGLE_CLOUD_PROJECT")
    return genai.Client(vertexai=True, project=project, location=location), None


def redact_error(exc: BaseException, secret: str | None) -> str:
    message = f"{type(exc).__name__}: {exc}"
    if secret:
        message = message.replace(secret, "<redacted>")
    return message


def load_terminal_ids(path: Path, statuses: set[str]) -> set[str]:
    terminal: set[str] = set()
    if not path.exists():
        return terminal
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
            if row.get("status") in statuses:
                terminal.add(row["job_id"])
    return terminal


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        json.dump(row, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")
        handle.flush()


def retry_call(function: Any, attempts: int) -> Any:
    for attempt in range(1, attempts + 1):
        try:
            return function()
        except errors.APIError as exc:
            status = getattr(exc, "code", None) or getattr(exc, "status_code", None)
            if status not in {429, 500, 502, 503, 504} or attempt == attempts:
                raise
            time.sleep(min(2 ** (attempt - 1), 20))
    raise AssertionError("unreachable")


def common_row(model: str, manifest_hash: str) -> dict[str, Any]:
    return {
        "model": model,
        "sdk_version": SDK_VERSION,
        "corpus_sha256": manifest_hash,
        "timestamp": utc_now(),
    }


def run_counts(args: argparse.Namespace) -> int:
    manifest = corpus_manifest()
    jobs = all_count_jobs()
    if args.limit is not None:
        jobs = jobs[: args.limit]
    output = Path(args.output) if args.output else (
        DEFAULT_RESULTS / f"counts-{safe_model_name(args.model)}.jsonl"
    )
    completed = load_terminal_ids(output, {"ok"})
    pending = [job for job in jobs if job.job_id not in completed]
    print(
        f"count jobs: total={len(jobs)} completed={len(jobs) - len(pending)} "
        f"pending={len(pending)} output={output}"
    )
    if not pending:
        return 0

    client, secret = create_client(args)
    errors_seen = 0
    try:
        for index, job in enumerate(pending, 1):
            started = time.perf_counter()
            try:
                response = retry_call(
                    lambda: client.models.count_tokens(model=args.model, contents=job.text),
                    args.attempts,
                )
                row = {
                    **common_row(args.model, str(manifest["sha256"])),
                    "status": "ok",
                    "job_id": job.job_id,
                    "experiment": job.experiment,
                    "unit_id": job.unit_id,
                    "variant": job.variant,
                    "text": job.text,
                    "text_sha256": text_sha256(job.text),
                    "characters": len(job.text),
                    "utf8_bytes": len(job.text.encode()),
                    "words": len(job.text.split()),
                    "token_count": response.total_tokens,
                    "cached_token_count": response.cached_content_token_count,
                    "latency_ms": round((time.perf_counter() - started) * 1000, 3),
                    **job.metadata,
                }
            except Exception as exc:  # saved so infrastructure misses remain visible
                errors_seen += 1
                row = {
                    **common_row(args.model, str(manifest["sha256"])),
                    "status": "error",
                    "job_id": job.job_id,
                    "experiment": job.experiment,
                    "unit_id": job.unit_id,
                    "variant": job.variant,
                    "text_sha256": text_sha256(job.text),
                    "error": redact_error(exc, secret),
                    "latency_ms": round((time.perf_counter() - started) * 1000, 3),
                    **job.metadata,
                }
            append_jsonl(output, row)
            if index == 1 or index % args.progress_every == 0 or index == len(pending):
                print(f"[{index}/{len(pending)}] {job.job_id} status={row['status']}", flush=True)
            if errors_seen >= args.max_errors:
                print(f"Stopped after {errors_seen} errors; rerun resumes successful jobs.", file=sys.stderr)
                return 2
            if args.delay:
                time.sleep(args.delay)
    finally:
        client.close()
    return 0


def _response_usage(response: Any) -> dict[str, int | None]:
    usage = getattr(response, "usage_metadata", None)
    return {
        "input_tokens": getattr(usage, "prompt_token_count", None),
        "output_tokens": getattr(usage, "candidates_token_count", None),
        "thought_tokens": getattr(usage, "thoughts_token_count", None),
        "cached_tokens": getattr(usage, "cached_content_token_count", None),
        "total_tokens": getattr(usage, "total_token_count", None),
    }


def _enum_value(value: Any) -> Any:
    return getattr(value, "value", value)


def score_response(text: str, expected: tuple[str, ...]) -> tuple[bool, str, Any]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return False, "invalid_json", None
    if not isinstance(payload, dict) or set(payload) != {"answer"}:
        return False, "invalid_schema", payload
    answer = payload["answer"]
    if not isinstance(answer, list) or not all(isinstance(item, str) for item in answer):
        return False, "invalid_schema", payload
    if len(answer) != len(set(answer)):
        return False, "duplicate_ids", payload
    if set(answer) != set(expected):
        return False, "wrong_answer", payload
    return True, "correct", payload


def run_generation(args: argparse.Namespace) -> int:
    manifest = corpus_manifest()
    jobs = generation_jobs(args.runs)
    if args.case_id:
        jobs = [job for job in jobs if job.case.case_id in set(args.case_id)]
    if args.condition:
        jobs = [job for job in jobs if job.condition in set(args.condition)]
    if args.limit is not None:
        jobs = jobs[: args.limit]
    output = Path(args.output) if args.output else (
        DEFAULT_RESULTS / f"generation-{safe_model_name(args.model)}.jsonl"
    )
    completed = load_terminal_ids(output, {"ok", "truncated"})
    pending = [job for job in jobs if job.job_id not in completed]
    print(
        f"generation jobs: total={len(jobs)} completed={len(jobs) - len(pending)} "
        f"pending={len(pending)} output={output}"
    )
    if not pending:
        return 0

    client, secret = create_client(args)
    thinking = types.ThinkingConfig(thinking_level=args.thinking_level.upper())
    config = types.GenerateContentConfig(
        temperature=args.temperature,
        max_output_tokens=args.max_output_tokens,
        response_mime_type="application/json",
        response_json_schema={
            "type": "object",
            "properties": {
                "answer": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["answer"],
            "additionalProperties": False,
        },
        thinking_config=thinking,
    )
    errors_seen = 0
    try:
        for index, job in enumerate(pending, 1):
            started = time.perf_counter()
            try:
                response = retry_call(
                    lambda: client.models.generate_content(
                        model=args.model,
                        contents=job.text,
                        config=config,
                    ),
                    args.attempts,
                )
                response_text = response.text or ""
                candidate = response.candidates[0] if response.candidates else None
                finish_reason = _enum_value(getattr(candidate, "finish_reason", None))
                if finish_reason == "MAX_TOKENS":
                    status = "truncated"
                    correct, score_reason, parsed = None, "max_tokens", None
                else:
                    status = "ok"
                    correct, score_reason, parsed = score_response(response_text, job.case.answer)
                row = {
                    **common_row(args.model, str(manifest["sha256"])),
                    "status": status,
                    "job_id": job.job_id,
                    "case_id": job.case.case_id,
                    "domain": job.case.domain.name,
                    "records": job.case.size,
                    "condition": job.condition,
                    "repetition": job.repetition,
                    "text": job.text,
                    "text_sha256": text_sha256(job.text),
                    "expected": list(job.case.answer),
                    "response_text": response_text,
                    "parsed_response": parsed,
                    "correct": correct,
                    "score_reason": score_reason,
                    "finish_reason": finish_reason,
                    "model_version": getattr(response, "model_version", None),
                    "latency_ms": round((time.perf_counter() - started) * 1000, 3),
                    "temperature": args.temperature,
                    "thinking_level": args.thinking_level.upper(),
                    "max_output_tokens": args.max_output_tokens,
                    **_response_usage(response),
                }
            except Exception as exc:
                errors_seen += 1
                row = {
                    **common_row(args.model, str(manifest["sha256"])),
                    "status": "error",
                    "job_id": job.job_id,
                    "case_id": job.case.case_id,
                    "domain": job.case.domain.name,
                    "records": job.case.size,
                    "condition": job.condition,
                    "repetition": job.repetition,
                    "text_sha256": text_sha256(job.text),
                    "error": redact_error(exc, secret),
                    "latency_ms": round((time.perf_counter() - started) * 1000, 3),
                }
            append_jsonl(output, row)
            if index == 1 or index % args.progress_every == 0 or index == len(pending):
                detail = (
                    f" correct={row.get('correct')}"
                    if row["status"] in {"ok", "truncated"}
                    else ""
                )
                print(
                    f"[{index}/{len(pending)}] {job.case.case_id} {job.condition} "
                    f"status={row['status']}{detail}",
                    flush=True,
                )
            if errors_seen >= args.max_errors:
                print(f"Stopped after {errors_seen} errors; rerun resumes successful jobs.", file=sys.stderr)
                return 2
            if args.delay:
                time.sleep(args.delay)
    finally:
        client.close()
    return 0


def read_jsonl_files(paths: Iterable[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if line.strip():
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError as exc:
                        raise SystemExit(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return rows


def mean(values: Iterable[float]) -> float:
    materialized = list(values)
    return statistics.mean(materialized) if materialized else math.nan


def median(values: Iterable[float]) -> float:
    materialized = list(values)
    return statistics.median(materialized) if materialized else math.nan


def percent(numerator: float, denominator: float) -> float:
    return 100.0 * numerator / denominator if denominator else math.nan


def paired_count_rows(rows: list[dict[str, Any]], experiment: str) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in rows:
        if row.get("status") == "ok" and row.get("experiment") == experiment:
            grouped[(row["model"], row["unit_id"])][row["variant"]] = row
    pairs = []
    for (model, unit_id), variants in grouped.items():
        if "full" not in variants or "short" not in variants:
            continue
        full = variants["full"]
        short = variants["short"]
        pairs.append(
            {
                "model": model,
                "unit_id": unit_id,
                "full": full,
                "short": short,
                "token_delta": full["token_count"] - short["token_count"],
                "character_delta": full["characters"] - short["characters"],
                "saving_pct": percent(
                    full["token_count"] - short["token_count"], full["token_count"]
                ),
            }
        )
    return pairs


def cost_for_row(row: dict[str, Any]) -> float | None:
    prices = PRICE_SNAPSHOT.get(row.get("model"))
    if not prices or row.get("input_tokens") is None:
        return None
    output = (row.get("output_tokens") or 0) + (row.get("thought_tokens") or 0)
    return (
        row["input_tokens"] * prices["input"] + output * prices["output"]
    ) / 1_000_000


def percentile(sorted_values: list[float], q: float) -> float:
    if not sorted_values:
        return math.nan
    position = (len(sorted_values) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def clustered_accuracy_interval(
    rows: list[dict[str, Any]], model: str, condition: str, samples: int = 5000
) -> tuple[float, float, float]:
    by_case_condition: dict[tuple[str, str], list[bool]] = defaultdict(list)
    for row in rows:
        if row.get("status") == "ok" and row.get("model") == model:
            by_case_condition[(row["case_id"], row["condition"])].append(bool(row["correct"]))
    case_ids = sorted(
        case_id
        for case_id, candidate_condition in by_case_condition
        if candidate_condition == "full"
        and (case_id, condition) in by_case_condition
    )
    if not case_ids:
        return math.nan, math.nan, math.nan
    differences = {
        case_id: mean(by_case_condition[(case_id, condition)])
        - mean(by_case_condition[(case_id, "full")])
        for case_id in case_ids
    }
    observed = mean(differences.values())
    rng = random.Random(SCHEDULE_SEED + 17)
    bootstrapped = []
    for _ in range(samples):
        sampled = [rng.choice(case_ids) for _ in case_ids]
        bootstrapped.append(mean(differences[case_id] for case_id in sampled))
    bootstrapped.sort()
    return observed, percentile(bootstrapped, 0.025), percentile(bootstrapped, 0.975)


def format_float(value: float, digits: int = 2) -> str:
    return "NA" if math.isnan(value) else f"{value:.{digits}f}"


def analyze(args: argparse.Namespace) -> int:
    results_dir = Path(args.results_dir)
    count_paths = sorted(results_dir.glob("counts-*.jsonl"))
    generation_paths = sorted(results_dir.glob("generation-*.jsonl"))
    count_rows = read_jsonl_files(count_paths)
    generation_rows = read_jsonl_files(generation_paths)
    lines = [
        "# Abbreviation experiment results",
        "",
        f"Generated: {utc_now()}",
        "",
        f"Count rows: {len(count_rows)}; generation rows: {len(generation_rows)}.",
        "",
    ]

    lexical = paired_count_rows(count_rows, "lexical")
    if lexical:
        lines.extend(("## Lexical audit", ""))
        by_model_category: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for pair in lexical:
            by_model_category[(pair["model"], pair["full"]["category"])].append(pair)
        lines.extend(
            (
                "| Model | Category | Pairs | Fewer | Equal | More | Mean token delta | Median saving |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            )
        )
        for (model, category), pairs in sorted(by_model_category.items()):
            deltas = [pair["token_delta"] for pair in pairs]
            lines.append(
                f"| {model} | {category} | {len(pairs)} | "
                f"{sum(delta > 0 for delta in deltas)} | {sum(delta == 0 for delta in deltas)} | "
                f"{sum(delta < 0 for delta in deltas)} | {format_float(mean(deltas))} | "
                f"{format_float(median(pair['saving_pct'] for pair in pairs))}% |"
            )
        lines.append("")

    break_even = paired_count_rows(count_rows, "break_even")
    if break_even:
        lines.extend(("## Definition break-even", ""))
        by_model_pair: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for pair in break_even:
            by_model_pair[(pair["model"], pair["full"]["pair_id"])].append(pair)
        by_model_category_values: dict[tuple[str, str], list[int | None]] = defaultdict(list)
        for (model, _pair_id), pairs in by_model_pair.items():
            ordered = sorted(pairs, key=lambda pair: pair["full"]["repetitions"])
            first = next(
                (pair["full"]["repetitions"] for pair in ordered if pair["token_delta"] > 0),
                None,
            )
            by_model_category_values[(model, ordered[0]["full"]["category"])].append(first)
        lines.extend(
            (
                "| Model | Category | Aliases | Break even by 32 | Median first winning repetition |",
                "|---|---:|---:|---:|---:|",
            )
        )
        for (model, category), values in sorted(by_model_category_values.items()):
            finite = [value for value in values if value is not None]
            lines.append(
                f"| {model} | {category} | {len(values)} | {len(finite)} | "
                f"{format_float(median(finite), 1) if finite else 'NA'} |"
            )
        lines.append("")

    prompt_rows = [
        row for row in count_rows if row.get("status") == "ok" and row.get("experiment") == "prompt"
    ]
    if prompt_rows:
        lines.extend(("## Complete prompt counts", ""))
        grouped: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
        for row in prompt_rows:
            grouped[(row["model"], row["unit_id"])][row["variant"]] = row
        effects: dict[tuple[str, str], list[float]] = defaultdict(list)
        for (model, _case_id), variants in grouped.items():
            if "full" not in variants:
                continue
            baseline = variants["full"]["token_count"]
            for condition, row in variants.items():
                if condition != "full":
                    effects[(model, condition)].append(percent(baseline - row["token_count"], baseline))
        lines.extend(
            (
                "| Model | Condition | Cases | Mean input saving | Median input saving |",
                "|---|---:|---:|---:|---:|",
            )
        )
        for (model, condition), values in sorted(effects.items()):
            lines.append(
                f"| {model} | {condition} | {len(values)} | {format_float(mean(values))}% | "
                f"{format_float(median(values))}% |"
            )
        lines.append("")

    ok_generation = [row for row in generation_rows if row.get("status") == "ok"]
    truncated_generation = [
        row for row in generation_rows if row.get("status") == "truncated"
    ]
    errored_generation = [row for row in generation_rows if row.get("status") == "error"]
    if generation_rows:
        lines.extend(("## End-to-end generation", ""))
        lines.append(
            f"Scorable responses: {len(ok_generation)}; truncations: "
            f"{len(truncated_generation)}; infrastructure errors: {len(errored_generation)}."
        )
        lines.append("")
    if ok_generation:
        grouped_generation: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        for row in ok_generation:
            grouped_generation[(row["model"], row["condition"])].append(row)
        lines.extend(
            (
                "| Model | Condition | Runs | Accuracy | Mean input | Mean visible output | Mean thoughts | Mean total | Total cost | Cost/correct |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
            )
        )
        for (model, condition), rows in sorted(grouped_generation.items()):
            costs = [cost for row in rows if (cost := cost_for_row(row)) is not None]
            correct_count = sum(bool(row["correct"]) for row in rows)
            total_cost = sum(costs) if costs else math.nan
            cost_per_correct = total_cost / correct_count if costs and correct_count else math.nan
            lines.append(
                f"| {model} | {condition} | {len(rows)} | "
                f"{format_float(percent(correct_count, len(rows)))}% | "
                f"{format_float(mean((row.get('input_tokens') or 0) for row in rows), 1)} | "
                f"{format_float(mean((row.get('output_tokens') or 0) for row in rows), 1)} | "
                f"{format_float(mean((row.get('thought_tokens') or 0) for row in rows), 1)} | "
                f"{format_float(mean((row.get('total_tokens') or 0) for row in rows), 1)} | "
                f"${format_float(total_cost, 4)} | ${format_float(cost_per_correct, 6)} |"
            )
        lines.append("")
        for model in sorted({row["model"] for row in ok_generation}):
            lines.append(f"Accuracy differences from full for `{model}` (case-clustered 95% CI):")
            lines.append("")
            for condition in CONDITIONS:
                if condition == "full":
                    continue
                observed, low, high = clustered_accuracy_interval(ok_generation, model, condition)
                lines.append(
                    f"- `{condition}`: {format_float(100 * observed)} percentage points "
                    f"[{format_float(100 * low)}, {format_float(100 * high)}]"
                )
            lines.append("")

    summary = "\n".join(lines).rstrip() + "\n"
    output = Path(args.output) if args.output else results_dir / "summary.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(summary, encoding="utf-8")
    print(summary)
    print(f"Wrote {output}")
    return 0


def show_manifest(args: argparse.Namespace) -> int:
    manifest = corpus_manifest()
    count_jobs = all_count_jobs()
    generations = generation_jobs(args.runs)
    counts_by_experiment: dict[str, int] = defaultdict(int)
    for job in count_jobs:
        counts_by_experiment[job.experiment] += 1
    print(f"corpus_sha256: {manifest['sha256']}")
    print(f"lexical_mappings: {len(LEXICAL_MAPPINGS)}")
    print(f"task_cases: {len(make_cases())}")
    print(f"conditions: {', '.join(CONDITIONS)}")
    for experiment, count in sorted(counts_by_experiment.items()):
        print(f"count_jobs.{experiment}: {count}")
    print(f"count_jobs.total: {len(count_jobs)}")
    print(f"generation_jobs at {args.runs} runs/cell: {len(generations)}")
    if args.write:
        output = Path(args.write)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote: {output}")
    return 0


def add_connection_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--env-file", default=str(DEFAULT_ENV_FILE))
    parser.add_argument("--backend", choices=("developer", "vertex"), default="developer")
    parser.add_argument("--project")
    parser.add_argument("--location")
    parser.add_argument("--model", default="gemini-3.6-flash")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--max-errors", type=int, default=3)
    parser.add_argument("--delay", type=float, default=0.0)
    parser.add_argument("--progress-every", type=int, default=25)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--output")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    manifest_parser = subparsers.add_parser("manifest", help="Show the frozen corpus without API calls")
    manifest_parser.add_argument("--runs", type=int, default=20)
    manifest_parser.add_argument("--write")
    manifest_parser.set_defaults(function=show_manifest)

    count_parser = subparsers.add_parser("count", help="Run deterministic token counts")
    add_connection_arguments(count_parser)
    count_parser.set_defaults(function=run_counts)

    generate_parser = subparsers.add_parser("generate", help="Run repeated objective tasks")
    add_connection_arguments(generate_parser)
    generate_parser.add_argument("--runs", type=int, default=20)
    generate_parser.add_argument("--case-id", action="append")
    generate_parser.add_argument("--condition", action="append", choices=CONDITIONS)
    generate_parser.add_argument("--temperature", type=float, default=0.2)
    generate_parser.add_argument(
        "--thinking-level", choices=("minimal", "low", "medium", "high"), default="low"
    )
    generate_parser.add_argument("--max-output-tokens", type=int, default=2048)
    generate_parser.set_defaults(function=run_generation)

    analyze_parser = subparsers.add_parser("analyze", help="Build a Markdown result summary")
    analyze_parser.add_argument("--results-dir", default=str(DEFAULT_RESULTS))
    analyze_parser.add_argument("--output")
    analyze_parser.set_defaults(function=analyze)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.function(args))


if __name__ == "__main__":
    raise SystemExit(main())
