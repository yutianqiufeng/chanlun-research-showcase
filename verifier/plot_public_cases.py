#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Plot exported public cases without generating any new signal."""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from public_core.case_io import load_case_bars, load_case_metadata
from public_core.plotting import plot_public_case
from public_core.project_paths import OUTPUTS_DIR


CASE_IDS: list[str] = []
OUTPUT_DIR = OUTPUTS_DIR / "public_case_plots"


def _selected_cases(frame: pd.DataFrame) -> pd.DataFrame:
    if not CASE_IDS:
        return frame
    wanted = {str(case_id).strip() for case_id in CASE_IDS if str(case_id).strip()}
    return frame.loc[frame["case_id"].isin(wanted)].copy()


def main() -> None:
    metadata = load_case_metadata()
    selected = _selected_cases(metadata)
    if selected.empty:
        print("No public cases selected.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for row in selected.itertuples(index=False):
        bars = load_case_bars(row.bars_csv)
        title = f"{row.case_id} | {row.symbol} | {row.timeframe} | {row.outcome_label}"
        output_path = OUTPUT_DIR / f"{row.case_id}.png"
        plot_public_case(
            bars,
            title=title,
            entry_time=pd.Timestamp(row.entry_time),
            entry_price=float(row.entry_price),
            exit_time=pd.Timestamp(row.exit_time),
            exit_price=float(row.exit_price),
            output_path=output_path,
        )
        print(f"Plotted: {output_path}")


if __name__ == "__main__":
    main()
