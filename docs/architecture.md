# Architecture

## Goal

This repository exposes the research infrastructure around a private trading system without publishing the alpha core.

## Layers

```mermaid
flowchart TD
    A["Private signal generator"] --> B["Curated public case export"]
    B --> C["Metadata registry"]
    B --> D["OHLCV bar files"]
    C --> E["Public verifier scripts"]
    D --> E
    E --> F["Case charts"]
    E --> G["Aggregate reports"]
```

## Public Components

- `examples/metadata.csv`
  - one row per public case
- `examples/cases/*.csv`
  - exported OHLCV bars for charting
- `verifier/plot_public_cases.py`
  - visual verification
- `verifier/evaluate_public_cases.py`
  - reporting and summary generation

## Private Components

The private system generates the original signals and selects what can be safely exported into the public case set.

That boundary is intentional. The verifier should never generate new signals on its own.
