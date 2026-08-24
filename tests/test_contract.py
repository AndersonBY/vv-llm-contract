from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

from jsonschema import exceptions, validators


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_contract.py"
SPEC = importlib.util.spec_from_file_location("validate_contract", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load validator: {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ContractRepositoryTests(unittest.TestCase):
    def test_repository_validates(self) -> None:
        counts = VALIDATOR.validate_repository()
        self.assertGreaterEqual(counts["schemas"], 8)
        self.assertGreaterEqual(counts["fixtures"], 3)
        self.assertEqual(counts["catalogs"], 1)
        self.assertEqual(counts["examples"], 3)

    def test_retry_fixture_is_a_single_source(self) -> None:
        retry = json.loads((ROOT / "fixtures" / "retry-after.v1.json").read_text(encoding="utf-8"))
        openai = json.loads((ROOT / "fixtures" / "openai-compatible.v2.json").read_text(encoding="utf-8"))
        self.assertGreater(len(retry["cases"]), 0)
        self.assertNotIn("retry_after_cases", openai)

    def test_openai_fixture_exercises_canonical_request_mapping_edges(self) -> None:
        fixture = json.loads((ROOT / "fixtures" / "openai-compatible.v2.json").read_text(encoding="utf-8"))
        canonical = fixture["request_case"]["canonical_request"]
        expected = fixture["request_case"]["expected_wire_request"]

        self.assertIn("max_tokens_details", canonical["options"])
        content = canonical["messages"][0]["content"]
        self.assertTrue(any(part.get("url") for part in content if isinstance(part, dict)))
        self.assertTrue(any(part.get("image_url") for part in content if isinstance(part, dict)))
        self.assertIn("name", canonical["messages"][1]["tool_calls"][0])
        self.assertIn("function", expected["messages"][1]["tool_calls"][0])

    def test_canonical_json_files_use_utf8_and_trailing_newline(self) -> None:
        for directory in ("schemas", "fixtures", "catalog", "examples"):
            for path in (ROOT / directory).glob("*.json"):
                content = path.read_text(encoding="utf-8")
                self.assertTrue(content.endswith("\n"), path.relative_to(ROOT))
                json.loads(content)

    def test_chat_contract_preserves_zero_and_rejects_invalid_extensions(self) -> None:
        schema = json.loads((ROOT / "schemas" / "chat-response.v1.schema.json").read_text(encoding="utf-8"))
        validator = validators.validator_for(schema)(schema)
        valid = {
            "content": "",
            "tool_calls": [],
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
            },
            "x_runtime_note": "preserved",
        }
        validator.validate(valid)
        with self.assertRaises(exceptions.ValidationError):
            validator.validate({**valid, "unknown_field": True})
        with self.assertRaises(exceptions.ValidationError):
            validator.validate({**valid, "usage": {"total_tokens": -1}})

    def test_tool_arguments_are_strings_and_done_only_stream_is_valid(self) -> None:
        request_schema = json.loads((ROOT / "schemas" / "chat-request.v1.schema.json").read_text(encoding="utf-8"))
        request_validator = validators.validator_for(request_schema)(request_schema)
        invalid_request = {
            "model": "model",
            "messages": [
                {
                    "role": "assistant",
                    "content": [],
                    "tool_calls": [{"id": "call", "name": "lookup", "arguments": {}}],
                }
            ],
        }
        with self.assertRaises(exceptions.ValidationError):
            request_validator.validate(invalid_request)
        with self.assertRaises(exceptions.ValidationError):
            request_validator.validate({"model": "   ", "messages": []})

        delta_schema = json.loads((ROOT / "schemas" / "chat-stream-delta.v1.schema.json").read_text(encoding="utf-8"))
        validators.validator_for(delta_schema)(delta_schema).validate({"done": True})


if __name__ == "__main__":
    unittest.main()
