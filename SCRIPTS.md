# Script Index

## Verifier Scripts

- `verifier/plot_public_cases.py`
  - Reads `examples/metadata.csv`
  - Loads exported OHLCV bars for each public case
  - Generates 5m case charts with entry and exit markers

- `verifier/evaluate_public_cases.py`
  - Reads `examples/metadata.csv`
  - Normalizes outcome labels and return metrics
  - Produces aggregate csv summaries for showcase reporting

## Public Core

- `public_core/project_paths.py`
  - Centralized repository paths

- `public_core/case_io.py`
  - Metadata loading and bar-file loading helpers

- `public_core/plotting.py`
  - Simple candlestick plotting for public case verification
