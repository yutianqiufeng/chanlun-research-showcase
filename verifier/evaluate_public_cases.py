#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Evaluate exported public cases and write aggregate showcase reports."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from public_core.case_io import load_case_metadata
from public_core.project_paths import GENERATED_REPORTS_DIR


ROUND_DIGITS = 4


def _coerce_numeric(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    output = frame.copy()
    for column in columns:
        output[column] = pd.to_numeric(output[column], errors="coerce")
    return output


def main() -> None:
    metadata = load_case_metadata()
    if metadata.empty:
        print("No public case metadata found.")
        return

    GENERATED_REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    normalized = _coerce_numeric(
        metadata,
        ["entry_price", "exit_price", "max_runup_pct", "max_drawdown_pct", "realized_return_pct"],
    )
    normalized["entry_month"] = normalized["entry_time"].dt.strftime("%Y-%m")

    summary_by_outcome = (
        normalized.groupby("outcome_label", dropna=False)
        .agg(
            case_count=("case_id", "count"),
            avg_realized_return_pct=("realized_return_pct", "mean"),
            avg_max_runup_pct=("max_runup_pct", "mean"),
            avg_max_drawdown_pct=("max_drawdown_pct", "mean"),
        )
        .reset_index()
    )

    summary_by_month = (
        normalized.groupby("entry_month", dropna=False)
        .agg(
            case_count=("case_id", "count"),
            avg_realized_return_pct=("realized_return_pct", "mean"),
            avg_max_runup_pct=("max_runup_pct", "mean"),
            avg_max_drawdown_pct=("max_drawdown_pct", "mean"),
        )
        .reset_index()
        .sort_values("entry_month")
    )

    detail_path = GENERATED_REPORTS_DIR / "public_case_detail.csv"
    outcome_path = GENERATED_REPORTS_DIR / "summary_by_outcome.csv"
    month_path = GENERATED_REPORTS_DIR / "summary_by_month.csv"

    normalized.round(ROUND_DIGITS).to_csv(detail_path, index=False, encoding="utf-8")
    summary_by_outcome.round(ROUND_DIGITS).to_csv(outcome_path, index=False, encoding="utf-8")
    summary_by_month.round(ROUND_DIGITS).to_csv(month_path, index=False, encoding="utf-8")

    print(f"Wrote: {detail_path}")
    print(f"Wrote: {outcome_path}")
    print(f"Wrote: {month_path}")


if __name__ == "__main__":
    main()
