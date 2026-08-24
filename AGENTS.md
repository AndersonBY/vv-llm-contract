# AGENTS.md

`vv-llm-contract` contains language-neutral JSON contracts and deterministic
fixtures only. Do not add provider clients, credentials, live tests, or
language-specific runtime types.

Before changing an artifact:

1. Read `README.md` and `manifest.json`.
2. Keep canonical JSON fields in `snake_case`.
3. Update the matching schema, fixture, manifest revision, changelog, and
   `checksums.sha256` together.
4. Regenerate `consumer-lock.v1.json` whenever `manifest.json`,
   `checksums.sha256`, or a pinned artifact changes.
5. Update every runtime's external consumer-lock SHA pin when intentionally
   adopting a new lock; the lock must not be trusted only by its own contents.
6. Preserve the difference between a missing value and an explicit zero.
7. Keep provider wire payloads open, but use the documented `x_` prefix for
   extensions on closed canonical chat/error envelopes.

Required verification:

```text
python scripts/validate_contract.py
python -m unittest discover -s tests -v
```

Changing a field name, type, requiredness, enum meaning, or normalization rule
requires a new schema version and a contract major release.
