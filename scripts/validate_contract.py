#!/usr/bin/env python3
"""Validate vv-llm-contract schemas, fixtures, manifest, and catalog."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import exceptions, validators
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
FIXTURE_DIR = ROOT / "fixtures"
CATALOG_DIR = ROOT / "catalog"
EXAMPLE_DIR = ROOT / "examples"
EXPECTED_CONSUMER_LOCK_SHA256 = "e2df07c360c71d0b6e2be3c73cef02150885c6a4cdaef5412e1a3ffcd696466d"


class ContractValidationError(RuntimeError):
    """Raised when repository artifacts violate the contract."""


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ContractValidationError(f"cannot load JSON {path.relative_to(ROOT)}: {error}") from error


def schema_documents() -> dict[str, tuple[Path, dict[str, Any]]]:
    documents: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in sorted(SCHEMA_DIR.glob("*.json")):
        value = load_json(path)
        if not isinstance(value, dict):
            raise ContractValidationError(f"schema must be an object: {path.relative_to(ROOT)}")
        validator_type = validators.validator_for(value)
        try:
            validator_type.check_schema(value)
        except exceptions.SchemaError as error:
            raise ContractValidationError(f"invalid schema {path.relative_to(ROOT)}: {error.message}") from error
        schema_id = value.get("$id")
        if not isinstance(schema_id, str) or not schema_id:
            raise ContractValidationError(f"schema has no non-empty $id: {path.relative_to(ROOT)}")
        if schema_id in documents:
            raise ContractValidationError(f"duplicate schema $id: {schema_id}")
        documents[schema_id] = (path, value)
    if not documents:
        raise ContractValidationError("no schemas found")
    return documents


def build_registry(documents: dict[str, tuple[Path, dict[str, Any]]]) -> Registry[Any]:
    registry: Registry[Any] = Registry()
    for schema_id, (path, value) in documents.items():
        resource = Resource.from_contents(value)
        registry = registry.with_resource(schema_id, resource)
        registry = registry.with_resource(path.resolve().as_uri(), resource)
    return registry


def validate_instance(
    instance: Any,
    schema_name: str,
    documents: dict[str, tuple[Path, dict[str, Any]]],
    registry: Registry[Any],
    label: str,
) -> None:
    schema_path = SCHEMA_DIR / schema_name
    matching = next((value for path, value in documents.values() if path == schema_path), None)
    if matching is None:
        raise ContractValidationError(f"missing schema: schemas/{schema_name}")
    validator_type = validators.validator_for(matching)
    validator = validator_type(matching, registry=registry)
    errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path))
    if errors:
        rendered = "; ".join(
            f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
            for error in errors[:8]
        )
        raise ContractValidationError(f"{label} does not satisfy {schema_name}: {rendered}")


def artifact_paths(value: Any) -> Iterable[str]:
    if isinstance(value, str) and value.endswith(".json"):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from artifact_paths(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from artifact_paths(item)


def validate_checksums(expected_paths: Iterable[str]) -> dict[str, str]:
    checksum_path = ROOT / "checksums.sha256"
    entries: dict[str, str] = {}
    for line_number, raw_line in enumerate(checksum_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line:
            continue
        parts = raw_line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64:
            raise ContractValidationError(f"invalid checksum line {line_number}")
        digest, relative = parts
        if relative in entries:
            raise ContractValidationError(f"duplicate checksum path: {relative}")
        entries[relative] = digest
    expected = set(expected_paths)
    if set(entries) != expected:
        missing = sorted(expected - set(entries))
        extra = sorted(set(entries) - expected)
        raise ContractValidationError(f"checksum path mismatch: missing={missing}, extra={extra}")
    for relative, expected_digest in entries.items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected_digest:
            raise ContractValidationError(
                f"checksum mismatch for {relative}: expected {expected_digest}, got {actual}"
            )
    return entries


def validate_repository() -> dict[str, int]:
    documents = schema_documents()
    registry = build_registry(documents)

    manifest = load_json(ROOT / "manifest.json")
    if not isinstance(manifest, dict):
        raise ContractValidationError("manifest.json must contain an object")
    if manifest.get("contract_version") != "1.3.0":
        raise ContractValidationError("manifest contract_version must be 1.3.0")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, (dict, list)):
        raise ContractValidationError("manifest artifacts must be an object or array")
    referenced = sorted(set(artifact_paths(artifacts)))
    if not referenced:
        raise ContractValidationError("manifest does not reference JSON artifacts")
    for relative in referenced:
        candidate = (ROOT / relative).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError as error:
            raise ContractValidationError(f"manifest artifact escapes repository: {relative}") from error
        if not candidate.is_file():
            raise ContractValidationError(f"manifest artifact does not exist: {relative}")
    if manifest.get("checksums") != "checksums.sha256":
        raise ContractValidationError("manifest checksums must reference checksums.sha256")
    checksum_entries = validate_checksums(referenced)

    consumer_lock = load_json(ROOT / "consumer-lock.v1.json")
    if not isinstance(consumer_lock, dict):
        raise ContractValidationError("consumer-lock.v1.json must contain an object")
    consumer_lock_digest = hashlib.sha256((ROOT / "consumer-lock.v1.json").read_bytes()).hexdigest()
    if consumer_lock_digest != EXPECTED_CONSUMER_LOCK_SHA256:
        raise ContractValidationError(
            "consumer-lock.v1.json SHA-256 does not match the release root pin"
        )
    if consumer_lock.get("contract_version") != manifest.get("contract_version"):
        raise ContractValidationError("consumer lock contract version does not match manifest")
    for revision_key in ("schema_version", "fixture_version", "catalog_revision"):
        if consumer_lock.get(revision_key) != manifest.get(revision_key):
            raise ContractValidationError(f"consumer lock {revision_key} does not match manifest")
    manifest_digest = hashlib.sha256((ROOT / "manifest.json").read_bytes()).hexdigest()
    checksums_digest = hashlib.sha256((ROOT / "checksums.sha256").read_bytes()).hexdigest()
    if consumer_lock.get("manifest_sha256") != manifest_digest:
        raise ContractValidationError("consumer lock manifest_sha256 is stale")
    if consumer_lock.get("checksums_sha256") != checksums_digest:
        raise ContractValidationError("consumer lock checksums_sha256 is stale")
    if consumer_lock.get("artifacts") != checksum_entries:
        raise ContractValidationError("consumer lock artifact hashes do not match checksums.sha256")

    openai_fixture = load_json(FIXTURE_DIR / "openai-compatible.v2.json")
    validate_instance(
        openai_fixture,
        "openai-compatible-fixture.v2.schema.json",
        documents,
        registry,
        "OpenAI-compatible fixture",
    )
    validate_instance(
        openai_fixture["request_case"]["canonical_request"],
        "chat-request.v1.schema.json",
        documents,
        registry,
        "canonical chat request",
    )
    validate_instance(
        openai_fixture["completion_case"]["expected_response"],
        "chat-response.v1.schema.json",
        documents,
        registry,
        "normalized chat response",
    )
    for index, delta in enumerate(openai_fixture["stream_case"]["expected_deltas"]):
        validate_instance(
            delta,
            "chat-stream-delta.v1.schema.json",
            documents,
            registry,
            f"normalized stream delta {index}",
        )

    decisions = load_json(FIXTURE_DIR / "decisions.v1.json")
    for key, schema in (("request", "decision-request.v1.schema.json"), ("response", "decision-response.v1.schema.json"), ("refusal_response", "decision-response.v1.schema.json")):
        validate_instance(decisions[key], schema, documents, registry, f"decision {key}")

    retry_fixture = load_json(FIXTURE_DIR / "retry-after.v1.json")
    validate_instance(
        retry_fixture,
        "retry-after.v1.schema.json",
        documents,
        registry,
        "retry-after fixture",
    )

    settings_fixture = load_json(FIXTURE_DIR / "settings-resolution.v1.json")
    validate_instance(
        settings_fixture["settings"],
        "settings.v2.schema.json",
        documents,
        registry,
        "Settings fixture",
    )

    catalog = load_json(CATALOG_DIR / "default-chat-catalog.json")
    validate_instance(
        catalog,
        "model-catalog.v1.schema.json",
        documents,
        registry,
        "default chat catalog",
    )

    for path in sorted(EXAMPLE_DIR.glob("*.json")):
        validate_instance(
            load_json(path),
            "chat-request.v1.schema.json",
            documents,
            registry,
            f"ChatRequest example {path.name}",
        )

    validate_instance(
        {
            "kind": "rate_limited",
            "message": "slow down",
            "status_code": 429,
            "retry_after_seconds": 1.5,
            "request_id": "fixture-request",
        },
        "error-details.v1.schema.json",
        documents,
        registry,
        "structured error details",
    )
    validate_instance(
        {
            "model": "embedding-model",
            "data": [{"index": 0, "embedding": [0.0, 1.0]}],
            "usage": {"prompt_tokens": 0, "total_tokens": 0},
        },
        "embedding.v1.schema.json",
        documents,
        registry,
        "embedding response",
    )
    validate_instance(
        {
            "model": "rerank-model",
            "results": [{"index": 0, "relevance_score": 0.0}],
        },
        "rerank.v1.schema.json",
        documents,
        registry,
        "rerank response",
    )

    return {
        "schemas": len(documents),
        "fixtures": len(list(FIXTURE_DIR.glob("*.json"))),
        "catalogs": len(list(CATALOG_DIR.glob("*.json"))),
        "examples": len(list(EXAMPLE_DIR.glob("*.json"))),
        "manifest_artifacts": len(referenced),
    }


def main() -> int:
    try:
        counts = validate_repository()
    except ContractValidationError as error:
        print(f"contract validation failed: {error}", file=sys.stderr)
        return 1
    print(
        "contract validation passed: "
        + ", ".join(f"{name}={count}" for name, count in counts.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
