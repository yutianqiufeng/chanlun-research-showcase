# Methodology

## Public Case Selection

Public cases should be sampled by category rather than by marketing value.

Recommended buckets:

- profitable exits
- stopped-out exits
- flat or weak cases
- failed timing or poor market context cases

## Reporting Rules

- publish aggregate statistics instead of full private signal history
- keep one metadata row per case
- keep chart generation deterministic from exported bars
- avoid embedding private reasons for entry selection

## Suggested Review Process

1. Export candidate cases from the private system.
2. Remove internal scoring and filter explanations.
3. Keep only bars, entry, exit, and high-level outcome fields.
4. Rebuild charts and summaries from the public verifier.

This keeps the public narrative reproducible without revealing the alpha core.
