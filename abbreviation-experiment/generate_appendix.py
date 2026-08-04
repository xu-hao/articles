#!/usr/bin/env python3
"""Generate the public appendix containing every frozen task and prompt."""

import argparse
import html
import json
from pathlib import Path

from cases import CONDITIONS, make_cases, render_prompt


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT.parent / "abbreviation-experiment-appendix.md"
RESULTS = ROOT / "results" / "counts-gemini-3.6-flash.jsonl"
LABELS = {
    "full": "Full prose",
    "abbr_defined": "Defined abbreviations",
    "abbr_undefined": "Undefined abbreviations",
    "concise": "Concise language",
}


def token_counts() -> dict[tuple[str, str], int]:
    counts: dict[tuple[str, str], int] = {}
    for line in RESULTS.read_text().splitlines():
        row = json.loads(line)
        if row.get("experiment") == "prompt" and row.get("status") == "ok":
            counts[(row["case_id"], row["variant"])] = row["token_count"]
    return counts


def details(summary: str, body: str, *, open_by_default: bool = False) -> str:
    attr = " open" if open_by_default else ""
    return f"<details{attr}><summary>{summary}</summary>\n\n{body}\n\n</details>"


def prompt_block(prompt: str) -> str:
    return f"<pre><code>{html.escape(prompt)}</code></pre>"


def render() -> str:
    counts = token_counts()
    sections = [
        "# Appendix: Every benchmark task and prompt",
        "",
        "This appendix contains the frozen corpus used in the article: all 32 "
        "tasks and all 128 exact request bodies. Each task has the same four "
        "conditions: full prose, defined abbreviations, undefined abbreviations, "
        "and concise language. Token counts are Gemini 3.6 Flash count-token results.",
        "",
        "The tasks are closed by default because this is a reference document. "
        "Expand a task to inspect its expected JSON answer and all four prompts.",
        "",
    ]
    for case in make_cases():
        prompt_details = []
        for condition in CONDITIONS:
            tokens = counts[(case.case_id, condition)]
            summary = f"{LABELS[condition]} — {tokens} input tokens"
            prompt_details.append(details(summary, prompt_block(render_prompt(case, condition))))
        answer = html.escape(json.dumps({"answer": list(case.answer)}))
        summary = (
            f"<strong>{html.escape(case.case_id)}</strong> — {case.size} records; "
            f"expected <code>{answer}</code>"
        )
        sections.append(details(summary, "\n\n".join(prompt_details)))
        sections.append("")
    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.write_text(render())


if __name__ == "__main__":
    main()
