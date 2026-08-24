from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_bundle.py"
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("build_bundle", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load bundle builder: {SCRIPT}")
BUILD_BUNDLE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILD_BUNDLE)


class ContractBundleTests(unittest.TestCase):
    def test_bundle_is_deterministic_and_complete(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = root / "first.zip"
            second = root / "second.zip"
            first_digest = BUILD_BUNDLE.build_bundle(first)
            second_digest = BUILD_BUNDLE.build_bundle(second)
            self.assertEqual(first_digest, second_digest)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with ZipFile(first) as archive:
                self.assertEqual(archive.namelist(), BUILD_BUNDLE.bundle_members())
                self.assertIn("examples/basic-chat-request.json", archive.namelist())
                self.assertIn("README_ZH.md", archive.namelist())


if __name__ == "__main__":
    unittest.main()
