#!/usr/bin/env python3
"""Reproduce the preregistered descriptive statistics."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import cast, Literal, Mapping


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/trial-outcomes.csv"
ENDPOINTS = ("model_exact_marker", "transcript_input_echo", "model_none")
CONDITIONS = ("canonical", "raw")
EXPECTED_MARKERS = (
    "CANARY_K7M4Q2",
    "CANARY_R9T6V3",
    "CANARY_B2H8P5",
    "CANARY_D5X1N7",
    "CANARY_J3C9L4",
    "CANARY_W6F2S8",
)
REQUIRED_COLUMNS = (
    "condition",
    "trial",
    "marker",
    *ENDPOINTS,
    "clear_before_trial",
)

Condition = Literal["canonical", "raw"]


@dataclass(frozen=True)
class TrialRow:
    condition: Condition
    trial: int
    marker: str
    model_exact_marker: int
    transcript_input_echo: int
    model_none: int
    clear_before_trial: str


def load_rows(path: Path = DATA) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _required_text(row: Mapping[str, str], column: str, row_number: int) -> str:
    value = row.get(column)
    if not isinstance(value, str):
        raise ValueError(f"Row {row_number}: missing value for {column}")
    return value.strip()


def validate_rows(rows: list[Mapping[str, str]]) -> list[TrialRow]:
    """Validate and type the exact preregistered 2 x 6 trial design."""

    if len(rows) != 12:
        raise ValueError(f"Expected 12 rows; found {len(rows)}")

    parsed: list[TrialRow] = []
    seen_trials: set[tuple[str, int]] = set()

    for row_number, row in enumerate(rows, start=2):
        missing = [column for column in REQUIRED_COLUMNS if column not in row]
        if missing:
            raise ValueError(
                f"Row {row_number}: Missing required column(s): {', '.join(missing)}"
            )

        condition_text = _required_text(row, "condition", row_number)
        if condition_text not in CONDITIONS:
            raise ValueError(
                f"Row {row_number}: Unknown condition {condition_text!r}; "
                f"expected canonical or raw"
            )
        condition = cast(Condition, condition_text)

        trial_text = _required_text(row, "trial", row_number)
        try:
            trial = int(trial_text)
        except ValueError as error:
            raise ValueError(
                f"Row {row_number}: trial must be an integer from 1 through 6"
            ) from error
        if trial not in range(1, 7):
            raise ValueError(
                f"Row {row_number}: trial must be from 1 through 6; found {trial}"
            )

        trial_key = (condition, trial)
        if trial_key in seen_trials:
            raise ValueError(f"Duplicate trial: {condition} trial {trial}")
        seen_trials.add(trial_key)

        marker = _required_text(row, "marker", row_number)
        if not marker:
            raise ValueError(f"Row {row_number}: marker must not be blank")

        endpoint_values: dict[str, int] = {}
        for endpoint in ENDPOINTS:
            value = _required_text(row, endpoint, row_number)
            if value not in {"0", "1"}:
                raise ValueError(
                    f"Row {row_number}: {endpoint} must be 0 or 1; found {value!r}"
                )
            endpoint_values[endpoint] = int(value)

        clear_before_trial = _required_text(row, "clear_before_trial", row_number)
        expected_clear = "NA" if trial == 1 else "1"
        if clear_before_trial != expected_clear:
            raise ValueError(
                f"Row {row_number}: clear_before_trial must be {expected_clear!r} "
                f"for trial {trial}; found {clear_before_trial!r}"
            )

        parsed.append(
            TrialRow(
                condition=condition,
                trial=trial,
                marker=marker,
                model_exact_marker=endpoint_values["model_exact_marker"],
                transcript_input_echo=endpoint_values["transcript_input_echo"],
                model_none=endpoint_values["model_none"],
                clear_before_trial=clear_before_trial,
            )
        )

    expected_trials = {
        (condition, trial)
        for condition in CONDITIONS
        for trial in range(1, 7)
    }
    missing_trials = expected_trials - seen_trials
    if missing_trials:
        formatted = ", ".join(
            f"{condition} trial {trial}" for condition, trial in sorted(missing_trials)
        )
        raise ValueError(f"Missing trial(s): {formatted}")

    by_trial = {(row.condition, row.trial): row for row in parsed}
    paired_markers: list[str] = []
    for trial in range(1, 7):
        canonical_marker = by_trial[("canonical", trial)].marker
        raw_marker = by_trial[("raw", trial)].marker
        if canonical_marker != raw_marker:
            raise ValueError(
                f"Marker mismatch for trial {trial}: "
                f"canonical={canonical_marker!r}, raw={raw_marker!r}"
            )
        if canonical_marker in paired_markers:
            raise ValueError("Marker reused across trial pairs")
        expected_marker = EXPECTED_MARKERS[trial - 1]
        if canonical_marker != expected_marker:
            raise ValueError(
                f"Trial {trial}: expected preregistered marker "
                f"{expected_marker!r}; found {canonical_marker!r}"
            )
        paired_markers.append(canonical_marker)

    return parsed


def summarize(rows: list[dict[str, str]]) -> dict[str, dict[str, tuple[int, int]]]:
    validated = validate_rows(rows)
    grouped: dict[str, list[TrialRow]] = {
        condition: [row for row in validated if row.condition == condition]
        for condition in CONDITIONS
    }

    result: dict[str, dict[str, tuple[int, int]]] = {}
    for condition in CONDITIONS:
        condition_rows = grouped[condition]
        result[condition] = {
            endpoint: (
                sum(getattr(row, endpoint) for row in condition_rows),
                len(condition_rows),
            )
            for endpoint in ENDPOINTS
        }
    return result


def main() -> int:
    summary = summarize(load_rows())
    print("BACKSPACE GATE — PREDECLARED DESCRIPTIVE ENDPOINTS")
    for endpoint in ENDPOINTS:
        canonical_yes, canonical_n = summary["canonical"][endpoint]
        raw_yes, raw_n = summary["raw"][endpoint]
        difference = (raw_yes / raw_n) - (canonical_yes / canonical_n)
        print(
            f"{endpoint}: canonical={canonical_yes}/{canonical_n}; "
            f"raw={raw_yes}/{raw_n}; raw-minus-canonical={difference:+.0%}"
        )
    print("Inferential tests: not performed (predeclared single-process boundary).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
