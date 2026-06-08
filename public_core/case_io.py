#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Load public showcase case metadata and OHLCV bars."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from public_core.project_paths import EXAMPLES_DIR


METADATA_PATH = EXAMPLES_DIR / "metadata.csv"
REQUIRED_METADATA_COLUMNS = {
    "case_id",
    "symbol",
    "timeframe",
    "bars_csv",
    "entry_time",
    "entry_price",
    "exit_time",
    "exit_price",
    "outcome_label",
    "exit_kind",
    "max_runup_pct",
    "max_drawdown_pct",
    "realized_return_pct",
    "notes",
}
REQUIRED_BARS_COLUMNS = {
    "trade_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
}


def _ensure_columns(frame: pd.DataFrame, required: Iterable[str], *, label: str) -> None:
    missing = [column for column in required if column not in frame.columns]
    if missing:
        raise ValueError(f"{label} is missing required columns: {missing}")


def load_case_metadata(path: Path = METADATA_PATH) -> pd.DataFrame:
    frame = pd.read_csv(path, encoding="utf-8")
    _ensure_columns(frame, REQUIRED_METADATA_COLUMNS, label=str(path))
    if frame.empty:
        return frame
    frame["case_id"] = frame["case_id"].astype(str).str.strip()
    frame["bars_csv"] = frame["bars_csv"].astype(str).str.strip()
    frame["symbol"] = frame["symbol"].astype(str).str.strip()
    frame["timeframe"] = frame["timeframe"].astype(str).str.strip()
    frame["outcome_label"] = frame["outcome_label"].astype(str).str.strip().str.lower()
    frame["exit_kind"] = frame["exit_kind"].astype(str).str.strip().str.lower()
    frame["entry_time"] = pd.to_datetime(frame["entry_time"], errors="coerce")
    frame["exit_time"] = pd.to_datetime(frame["exit_time"], errors="coerce")
    return frame


def resolve_bars_path(relative_path: str) -> Path:
    return EXAMPLES_DIR / str(relative_path).strip()


def load_case_bars(relative_path: str) -> pd.DataFrame:
    path = resolve_bars_path(relative_path)
    frame = pd.read_csv(path, encoding="utf-8")
    _ensure_columns(frame, REQUIRED_BARS_COLUMNS, label=str(path))
    frame["trade_time"] = pd.to_datetime(frame["trade_time"], errors="coerce")
    frame = frame.dropna(subset=["trade_time"]).copy()
    frame = frame.sort_values("trade_time").reset_index(drop=True)
    numeric_columns = ["open", "high", "low", "close", "volume"]
    for column in numeric_columns:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna(subset=["open", "high", "low", "close"])
    if frame.empty:
        raise ValueError(f"bars file is empty after normalization: {path}")
    return frame
