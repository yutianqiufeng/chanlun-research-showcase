# ChanLun Research Showcase

[中文说明](README.zh-CN.md)

This repository is a public showcase edition of a larger trading research system.

It is intentionally scoped to demonstrate:

- data organization and research workflow
- case-based verification
- 5m K-line plotting for selected examples
- report generation from pre-exported public cases
- engineering boundaries between reusable infrastructure and private alpha logic

It does not publish the private alpha core. The following remain outside the open-source scope:

- buy-point recognition logic
- signal filtering conditions
- parameter combinations and execution thresholds
- live execution and risk-control details

## Why This Repo Exists

The goal is to contribute useful research infrastructure to the community while protecting the parts that create trading edge.

This repo follows a verifier-style design:

- public artifacts show how cases are organized, visualized, and evaluated
- private artifacts generate the original signals and execution decisions

## Repository Layout

```text
docs/                   architecture, methodology, and scope notes
examples/               public case schema and case metadata templates
public_core/            reusable plotting and case-loading helpers
reports/                generated or hand-written summary reports
verifier/               scripts that plot and evaluate public cases only
```

## Quick Start

1. Create or export a curated public case set into `examples/cases/`.
2. Fill `examples/metadata.csv`.
3. Run the verifier scripts directly after editing the file-level config variables.

```powershell
python verifier/plot_public_cases.py
python verifier/evaluate_public_cases.py
```

The scripts follow the original project convention:

- no `argparse`
- file-level configuration
- direct IDE run support

## Public Case Contract

Each public case contains:

- one OHLCV csv file
- one row in `examples/metadata.csv`
- optional notes for report generation

The verifier accepts pre-exported bars and produces:

- 5m case charts
- per-case evaluation rows
- aggregate summary csv files

## Live Verification

This repository is not the live trading system itself.

For due-diligence or interview verification, contact:

- `1625059268@qq.com`

The live strategy service runs privately. Verification can be handled through curated case exports, runtime screenshots, and redacted logs without disclosing the alpha core.

## Documentation

- [Open/Private Boundary](docs/open-private-boundary.md)
- [Architecture](docs/architecture.md)
- [Methodology](docs/methodology.md)
- [Live Trading Note](docs/live-trading-note.md)

## License

MIT. See [LICENSE](LICENSE).
