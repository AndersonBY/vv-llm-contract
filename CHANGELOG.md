# Changelog

## Unreleased

- Add `gpt-6-astra` with a 1,050,000-token context window, 128,000-token output,
  tool calling, structured output, and image input in catalog revision 3.

- Add the documented `glm-5.3-flash` model capabilities to catalog revision 2.

## 1.0.1 - 2026-08-24

- Use Settings as the user-facing name for the shared runtime configuration.

## 1.0.0 - 2026-08-24

- Define language-neutral schemas for chat, streaming, errors, retrieval,
  Settings, and the model catalog.
- Publish canonical `ChatRequest` examples for text, tools, and multimodal
  input.
- Provide deterministic OpenAI-compatible, retry-header, and settings fixtures.
- Publish default chat catalog revision 1.
