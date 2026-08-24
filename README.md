# vv-llm-contract

[中文文档](README_ZH.md)

Language-neutral contracts shared by the Python `vv-llm`, Rust `vv-llm-rs`,
and TypeScript `vv-llm-ts` runtimes.

This repository is the source of truth for serializable JSON shapes,
conformance fixtures, and the default model catalog.

## Contents

- `schemas/` — JSON Schema 2020-12 definitions for normalized chat, stream,
  error, retrieval, Settings, and model catalog data.
- `fixtures/` — provider-wire input and normalized-output examples that every
  runtime must pass without credentials or network calls.
- `examples/` — valid canonical `ChatRequest` documents.
- `catalog/` — the versioned default chat catalog snapshot.
- `manifest.json` — contract, schema, fixture, and catalog revisions.
- `checksums.sha256` — release-artifact integrity pins.
- `consumer-lock.v1.json` — the exact version and hashes copied into runtimes.
- `scripts/validate_contract.py` — repository integrity and schema validator.

Canonical JSON uses `snake_case`. Runtime APIs may use language-native names,
with explicit conversion at the contract boundary.

Canonical chat and error envelopes are closed: unknown fields are rejected
unless they use the `x_` extension prefix. Provider wire payloads, Settings,
catalog entries, and retrieval responses remain open for transport metadata
and provider fields.

## Canonical ChatRequest

`schemas/chat-request.v1.schema.json` defines the portable request shape.
Start with [the examples](examples/README.md).

| Canonical field | Adapter responsibility |
| --- | --- |
| `options` | Remain nested until the transport adapter builds a provider request. |
| `tools` | Use the canonical tool shape; provider adapters add their wire envelope. |
| `tool_choice` | Preserve both the named string choices and opaque object form. |
| `extra_body` | Remains opaque until the provider request is built. |
| `x_*` | Round-trips through canonical encoding and decoding. Its own specification defines transport behavior. |

Each runtime exposes a typed `ChatRequest` API and an explicit canonical JSON
codec. Method names and streaming return types remain language-specific.

## Validation

```text
python -m pip install -r requirements-dev.txt
python scripts/validate_contract.py
python -m unittest discover -s tests -v
python scripts/build_bundle.py
```

Pushing `v<contract_version>` runs these gates and builds the release ZIP.

Validation is local and deterministic. It never reads credentials or calls a
provider API.

## Consumer workflow

Runtime packages ship a pinned contract copy. Installed applications do not
need this repository.

To update a runtime:

1. Download and verify a tagged release bundle.
2. Pass the extracted release directory to the runtime's sync command.
3. Update the runtime's external consumer-lock pin and run its package tests.

## Versioning

- The repository uses independent SemVer.
- Each schema and fixture declares an explicit version.
- Adding optional fields is a minor contract release.
- Changing names, types, requiredness, enum meaning, or normalization semantics
  is a major release and creates a new schema version.
- Catalog changes increment `catalog_revision` independently of schema SemVer.
- Python, Rust, and TypeScript packages continue to release independently and
  should pin a contract release plus artifact SHA-256.

Consumers must pin the consumer-lock file itself outside the vendored tree.
Its SHA-256 is published with the release and recorded by each runtime.

## Non-goals

HTTP clients, authentication, retries, middleware, fallback, tokenizers,
provider SDKs, live tests, and application messages belong to the runtimes.
