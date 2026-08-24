#!/usr/bin/env python3
"""Ensure a release tag exactly matches manifest contract_version."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    tag = os.environ.get("GITHUB_REF_NAME") or (sys.argv[1] if len(sys.argv) > 1 else "")
    version = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["contract_version"]
    expected = f"v{version}"
    if tag != expected:
        print(f"release tag mismatch: expected {expected}, got {tag or '<empty>'}", file=sys.stderr)
        return 1
    print(f"release tag matches contract version: {tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
