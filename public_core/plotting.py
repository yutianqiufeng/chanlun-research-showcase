#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple candlestick plotting for public cases."""

from __future__ import annotations

from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd


def plot_public_case(
    bars: pd.DataFrame,
    *,
    title: str,
    entry_time: pd.Timestamp,
    entry_price: float,
    exit_time: pd.Timestamp,
    exit_price: float,
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    x_values = np.arange(len(bars), dtype=float)
    opens = bars["open"].to_numpy(dtype=float)
    highs = bars["high"].to_numpy(dtype=float)
    lows = bars["low"].to_numpy(dtype=float)
    closes = bars["close"].to_numpy(dtype=float)
    trade_time = pd.to_datetime(bars["trade_time"], errors="coerce")

    fig, ax = plt.subplots(figsize=(15, 8), dpi=180)
    candle_width = 0.6

    for index, x_pos in enumerate(x_values):
        color = "#0f9d58" if closes[index] >= opens[index] else "#db4437"
        ax.vlines(x_pos, lows[index], highs[index], color=color, linewidth=0.8, alpha=0.9)
        body_low = min(opens[index], closes[index])
        body_height = max(abs(closes[index] - opens[index]), 1e-9)
        ax.add_patch(
            Rectangle(
                (x_pos - candle_width / 2.0, body_low),
                candle_width,
                body_height,
                facecolor=color,
                edgecolor=color,
                linewidth=0.8,
                alpha=0.8,
            )
        )

    entry_idx = _nearest_index(trade_time, entry_time)
    exit_idx = _nearest_index(trade_time, exit_time)

    if entry_idx is not None:
        ax.scatter([entry_idx], [entry_price], color="#1a73e8", s=70, marker="^", label="entry", zorder=5)
    if exit_idx is not None:
        ax.scatter([exit_idx], [exit_price], color="#f29900", s=70, marker="v", label="exit", zorder=5)

    ax.set_title(title)
    ax.set_xlabel("bars")
    ax.set_ylabel("price")
    ax.grid(alpha=0.18, linestyle="--")
    if entry_idx is not None or exit_idx is not None:
        ax.legend(frameon=False)

    tick_count = min(len(bars), 12)
    tick_idx = np.unique(np.linspace(0, max(len(bars) - 1, 0), tick_count, dtype=int))
    tick_labels = trade_time.dt.strftime("%m-%d %H:%M").iloc[tick_idx].tolist()
    ax.set_xticks(tick_idx)
    ax.set_xticklabels(tick_labels, rotation=25, ha="right")

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def _nearest_index(times: pd.Series, target: pd.Timestamp) -> int | None:
    if pd.isna(target):
        return None
    deltas = (times - pd.Timestamp(target)).abs()
    if deltas.isna().all():
        return None
    return int(deltas.idxmin())
