#!/usr/bin/env python3
"""Build a deterministic distributable vv-llm-contract ZIP bundle."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate_contract import ROOT, load_json, validate_repository


LOCK_PATH = ROOT / "consumer-lock.v1.json"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
DOCUMENTATION_MEMBERS = (
    "README.md",
    "README_ZH.md",
    "examples/README.md",
    "examples/basic-chat-request.json",
    "examples/multimodal-chat-request.json",
    "examples/tools-chat-request.json",
)


def bundle_members() -> list[str]:
    lock = load_json(LOCK_PATH)
    artifacts = lock.get("artifacts")
    if not isinstance(artifacts, dict):
        raise RuntimeError("consumer lock artifacts must be an object")
    return [
        "manifest.json",
        "checksums.sha256",
        "consumer-lock.v1.json",
        *DOCUMENTATION_MEMBERS,
        *sorted(artifacts),
    ]


def build_bundle(output_path: Path) -> str:
    validate_repository()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in bundle_members():
            source = ROOT / relative
            info = ZipInfo(relative, FIXED_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    return hashlib.sha256(output_path.read_bytes()).hexdigest()


def main() -> int:
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    version = lock["contract_version"]
    output = ROOT / "dist" / f"vv-llm-contract-{version}.zip"
    digest = build_bundle(output)
    digest_path = output.with_suffix(output.suffix + ".sha256")
    digest_path.write_text(f"{digest}  {output.name}\n", encoding="utf-8", newline="\n")
    print(f"built {output.relative_to(ROOT)} sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
