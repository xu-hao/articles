"""Frozen, deterministic cases for the abbreviation token experiment.

This module contains no API code.  The lexical mappings are hand-authored and
the task corpus is generated from fixed domain templates and fixed random seeds.
Changing this file changes the corpus hash recorded by the runner.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import random
from typing import Iterable


@dataclass(frozen=True)
class Mapping:
    category: str
    full: str
    short: str


LEXICAL_MAPPINGS: tuple[Mapping, ...] = (
    # Widely used initialisms.
    Mapping("standard_initialism", "application programming interface", "API"),
    Mapping("standard_initialism", "central processing unit", "CPU"),
    Mapping("standard_initialism", "service level agreement", "SLA"),
    Mapping("standard_initialism", "quality assurance", "QA"),
    Mapping("standard_initialism", "user interface", "UI"),
    Mapping("standard_initialism", "software development kit", "SDK"),
    Mapping("standard_initialism", "content delivery network", "CDN"),
    Mapping("standard_initialism", "customer relationship management", "CRM"),
    Mapping("standard_initialism", "key performance indicator", "KPI"),
    Mapping("standard_initialism", "frequently asked questions", "FAQ"),
    # Conventional shortenings rather than initialisms.
    Mapping("conventional_shortening", "configuration", "config"),
    Mapping("conventional_shortening", "application", "app"),
    Mapping("conventional_shortening", "documentation", "docs"),
    Mapping("conventional_shortening", "repository", "repo"),
    Mapping("conventional_shortening", "administrator", "admin"),
    Mapping("conventional_shortening", "authentication", "auth"),
    Mapping("conventional_shortening", "authorization", "authz"),
    Mapping("conventional_shortening", "synchronization", "sync"),
    Mapping("conventional_shortening", "request", "req"),
    Mapping("conventional_shortening", "response", "resp"),
    # Intentionally ambiguous initialisms.  Duplicate short forms are useful:
    # token efficiency and semantic safety are different questions.
    Mapping("ambiguous_initialism", "certificate authority", "CA"),
    Mapping("ambiguous_initialism", "pull request", "PR"),
    Mapping("ambiguous_initialism", "public relations", "PR"),
    Mapping("ambiguous_initialism", "multiple sclerosis", "MS"),
    Mapping("ambiguous_initialism", "Microsoft", "MS"),
    Mapping("ambiguous_initialism", "estimated time of arrival", "ETA"),
    Mapping("ambiguous_initialism", "electronic travel authorization", "ETA"),
    Mapping("ambiguous_initialism", "operating system", "OS"),
    Mapping("ambiguous_initialism", "open source", "OS"),
    Mapping("ambiguous_initialism", "human resources", "HR"),
    # Arbitrary aliases have no learned meaning and therefore require a legend.
    Mapping("invented_alias", "customer support representative", "X1"),
    Mapping("invented_alias", "purchase approval request", "X2"),
    Mapping("invented_alias", "quarterly compliance review", "X3"),
    Mapping("invented_alias", "regional distribution center", "X4"),
    Mapping("invented_alias", "incident response coordinator", "X5"),
    Mapping("invented_alias", "supplier onboarding checklist", "X6"),
    Mapping("invented_alias", "customer satisfaction survey", "X7"),
    Mapping("invented_alias", "maintenance scheduling window", "X8"),
    Mapping("invented_alias", "data retention requirement", "X9"),
    Mapping("invented_alias", "payment reconciliation report", "X10"),
)


LEXICAL_CONTEXTS: tuple[tuple[str, str], ...] = (
    ("standalone", "{term}"),
    ("sentence", "The review covers {term} before final approval."),
    ("punctuation", "Requirement: {term}; status: pending."),
)


@dataclass(frozen=True)
class Domain:
    name: str
    entity: str
    entity_short: str
    metric: str
    metric_short: str
    deadline: str
    deadline_short: str
    state: str
    state_short: str
    states: tuple[str, str, str]
    target_state: str

    @property
    def mappings(self) -> tuple[tuple[str, str], ...]:
        return (
            (self.entity, self.entity_short),
            (self.metric, self.metric_short),
            (self.deadline, self.deadline_short),
            (self.state, self.state_short),
        )


DOMAINS: tuple[Domain, ...] = (
    Domain(
        "support",
        "customer support request", "CSR",
        "priority level", "PL",
        "response deadline", "RD",
        "escalation status", "ES",
        ("required", "not required", "pending"), "required",
    ),
    Domain(
        "logistics",
        "shipment exception record", "SER",
        "disruption severity", "DS",
        "resolution deadline", "RD",
        "carrier status", "CS",
        ("confirmed", "delayed", "pending"), "confirmed",
    ),
    Domain(
        "security",
        "security incident report", "SIR",
        "risk level", "RL",
        "remediation deadline", "RD",
        "containment status", "CS",
        ("complete", "incomplete", "pending"), "complete",
    ),
    Domain(
        "finance",
        "expense reimbursement request", "ERR",
        "audit score", "AS",
        "submission deadline", "SD",
        "approval status", "APS",
        ("approved", "denied", "pending"), "approved",
    ),
    Domain(
        "healthcare",
        "patient appointment request", "PAR",
        "urgency level", "UL",
        "appointment deadline", "AD",
        "insurance status", "IS",
        ("verified", "unverified", "pending"), "verified",
    ),
    Domain(
        "manufacturing",
        "quality inspection report", "QIR",
        "defect severity", "DS",
        "correction deadline", "CD",
        "inspection status", "IS",
        ("failed", "passed", "pending"), "failed",
    ),
    Domain(
        "human_resources",
        "employee training record", "ETR",
        "compliance score", "CS",
        "renewal deadline", "RD",
        "completion status", "CTS",
        ("incomplete", "complete", "pending"), "incomplete",
    ),
    Domain(
        "operations",
        "service interruption report", "SIR",
        "impact severity", "IS",
        "recovery deadline", "RD",
        "restoration status", "RS",
        ("unavailable", "degraded", "restored"), "unavailable",
    ),
)


TASK_SIZES: tuple[int, ...] = (6, 12, 24, 48)
CONDITIONS: tuple[str, ...] = (
    "full",
    "abbr_defined",
    "abbr_undefined",
    "concise",
)


@dataclass(frozen=True)
class Record:
    record_id: str
    metric: int
    deadline: int
    state: str


@dataclass(frozen=True)
class TaskCase:
    case_id: str
    domain: Domain
    size: int
    metric_threshold: int
    deadline_threshold: int
    records: tuple[Record, ...]
    answer: tuple[str, ...]


def _case_seed(domain: Domain, size: int) -> int:
    digest = hashlib.sha256(f"abbreviation-v1:{domain.name}:{size}".encode()).digest()
    return int.from_bytes(digest[:8], "big")


def make_cases() -> tuple[TaskCase, ...]:
    cases: list[TaskCase] = []
    for domain_index, domain in enumerate(DOMAINS):
        for size_index, size in enumerate(TASK_SIZES):
            rng = random.Random(_case_seed(domain, size))
            metric_threshold = 3 + ((domain_index + size_index) % 2)
            deadline_threshold = 10 + 5 * ((domain_index + size_index) % 3)
            records: list[Record] = []
            # Two fixed controls guarantee at least one match and one obvious miss.
            records.append(Record("R01", 5, 1, domain.target_state))
            records.append(Record("R02", 1, 30, domain.states[1]))
            for number in range(3, size + 1):
                records.append(
                    Record(
                        f"R{number:02d}",
                        rng.randint(1, 5),
                        rng.randint(1, 30),
                        rng.choice(domain.states),
                    )
                )
            answer = tuple(
                record.record_id
                for record in records
                if record.metric >= metric_threshold
                and record.deadline <= deadline_threshold
                and record.state == domain.target_state
            )
            cases.append(
                TaskCase(
                    case_id=f"{domain.name}-{size:02d}",
                    domain=domain,
                    size=size,
                    metric_threshold=metric_threshold,
                    deadline_threshold=deadline_threshold,
                    records=tuple(records),
                    answer=answer,
                )
            )
    return tuple(cases)


def _full_prompt(case: TaskCase) -> str:
    domain = case.domain
    lines = [
        f"Review every {domain.entity}. A {domain.entity} qualifies only when all three rules hold:",
        f"1. Its {domain.metric} is at least {case.metric_threshold}.",
        f"2. Its {domain.deadline} is day {case.deadline_threshold} or earlier.",
        f'3. Its {domain.state} is exactly "{domain.target_state}".',
        "",
        "Records:",
    ]
    for record in case.records:
        lines.append(
            f"- {record.record_id} — {domain.metric}: {record.metric}; "
            f"{domain.deadline}: day {record.deadline}; {domain.state}: {record.state}."
        )
    lines.extend(
        (
            "",
            'Return only a JSON object of the form {"answer": ["R01", "R02"]}.',
            "The answer must contain every qualifying record ID in ascending order and no others.",
        )
    )
    return "\n".join(lines)


def _abbreviate(text: str, mappings: Iterable[tuple[str, str]]) -> str:
    # Longest-first replacement protects mappings if terms ever overlap.
    for full, short in sorted(mappings, key=lambda pair: len(pair[0]), reverse=True):
        text = text.replace(full, short)
    return text


def _concise_prompt(case: TaskCase) -> str:
    lines = [
        "Select every record satisfying all conditions:",
        f"score >= {case.metric_threshold}; day <= {case.deadline_threshold}; "
        f'state = "{case.domain.target_state}".',
        "",
        "Records:",
    ]
    for record in case.records:
        lines.append(
            f"- {record.record_id}: score={record.metric}; day={record.deadline}; state={record.state}."
        )
    lines.extend(
        (
            "",
            'Return only {"answer": [record IDs]} with qualifying IDs in ascending order.',
        )
    )
    return "\n".join(lines)


def render_prompt(case: TaskCase, condition: str) -> str:
    if condition not in CONDITIONS:
        raise ValueError(f"Unknown condition: {condition}")
    if condition == "full":
        return _full_prompt(case)
    if condition == "concise":
        return _concise_prompt(case)

    abbreviated = _abbreviate(_full_prompt(case), case.domain.mappings)
    if condition == "abbr_undefined":
        return abbreviated

    legend = ["Abbreviation legend:"]
    legend.extend(f"- {short} = {full}" for full, short in case.domain.mappings)
    return "\n".join(legend) + "\n\n" + abbreviated


def corpus_manifest() -> dict[str, object]:
    cases = make_cases()
    serializable = {
        "version": 1,
        "lexical_mappings": [asdict(mapping) for mapping in LEXICAL_MAPPINGS],
        "lexical_contexts": list(LEXICAL_CONTEXTS),
        "conditions": list(CONDITIONS),
        "cases": [
            {
                "case_id": case.case_id,
                "domain": asdict(case.domain),
                "size": case.size,
                "metric_threshold": case.metric_threshold,
                "deadline_threshold": case.deadline_threshold,
                "records": [asdict(record) for record in case.records],
                "answer": list(case.answer),
                "prompts": {
                    condition: render_prompt(case, condition)
                    for condition in CONDITIONS
                },
            }
            for case in cases
        ],
    }
    canonical = json.dumps(serializable, sort_keys=True, separators=(",", ":"))
    serializable["sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return serializable
