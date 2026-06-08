#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repository paths for the public showcase edition."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = PROJECT_ROOT / "docs"
EXAMPLES_DIR = PROJECT_ROOT / "examples"
CASES_DIR = EXAMPLES_DIR / "cases"
REPORTS_DIR = PROJECT_ROOT / "reports"
GENERATED_REPORTS_DIR = REPORTS_DIR / "generated"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
