from __future__ import annotations

import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]


class DecisionContractTests(unittest.TestCase):
    def test_shared_requests_responses_and_invalid_payloads(self):
        fixture = json.loads((ROOT / "fixtures/decisions.v1.json").read_text(encoding="utf-8"))
        request = Draft202012Validator(json.loads((ROOT / "schemas/decision-request.v1.schema.json").read_text(encoding="utf-8")))
        response = Draft202012Validator(json.loads((ROOT / "schemas/decision-response.v1.schema.json").read_text(encoding="utf-8")))
        request.validate(fixture["request"])
        for valid in fixture["valid_requests"]:
            request.validate(valid)
        response.validate(fixture["response"])
        for valid in fixture["valid_responses"]:
            response.validate(valid)
        response.validate(fixture["refusal_response"])
        for validator, cases in ((request, fixture["invalid_requests"]), (response, fixture["invalid_responses"])):
            for case in cases:
                with self.assertRaises(ValidationError):
                    validator.validate(case)
        response.validate({"model": "gpt-6-luna", "answers": [{"type": "predicate", "probability": 0}], "usage": {"input_tokens": None, "output_tokens": 0}})


if __name__ == "__main__":
    unittest.main()
