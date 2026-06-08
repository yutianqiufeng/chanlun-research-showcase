# Public Case Format

## Metadata File

`metadata.csv` contains one row per public case.

Required columns:

- `case_id`
- `symbol`
- `timeframe`
- `bars_csv`
- `entry_time`
- `entry_price`
- `exit_time`
- `exit_price`
- `outcome_label`
- `exit_kind`
- `max_runup_pct`
- `max_drawdown_pct`
- `realized_return_pct`
- `notes`

## Bars File

Each case points to one OHLCV csv file stored under `examples/cases/`.

Required columns:

- `trade_time`
- `open`
- `high`
- `low`
- `close`
- `volume`

The verifier does not generate signals. It only consumes exported public cases.
