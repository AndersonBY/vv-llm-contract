# Changelog

## 1.2.1 - 2026-10-03

- Release catalog revision 16 with the single public model ID
  `qwen3.8-flash-next` and documented DashScope endpoint mapping.

## Catalog revision 16 - 2026-10-03

- Use `qwen3.8-flash-next` as the sole public catalog key and model ID.
  DashScope can map it to `qwen3.8-flash` through endpoint `model_id`.

## Catalog revision 15 - 2026-10-03

- Add `Qwen/Qwen3.8-Flash-Next` with a 262,144 native context window,
  text/image/video input, tools, configurable thinking, and low/medium/xhigh
  effort choices. Output limits and structured-output support remain unspecified
  for the open-weight model.

## Catalog revision 14 - 2026-09-30

- Add `gpt-6.1-sol` with a 1,050,000 context window, 128,000 max output
  tokens, text/image input, tools, structured output, and the `low`,
  `medium`, `high`, `xhigh`, `max` effort choices.

## Catalog revision 13 - 2026-09-29

- Add `claude-sonnet-5-5` with the 1,000,000 context window, 128,000 max
  output tokens, tool use, image input, and the `low`, `medium`, `high`,
  `xhigh`, `max` effort choices.

## Catalog revision 12 - 2026-09-29

- Add `gpt-6-sol` and `gpt-6-luna` with a 1,050,000 context window, 128,000
  max output tokens, text/image input, tools, structured output, and the
  `none`, `low`, `medium`, `high`, `xhigh`, `max` effort choices.

## Catalog revision 11 - 2026-09-29

- Add `claude-opus-5-5` with the limits, capabilities, and effort choices of
  `claude-opus-5`.
- Add `gemini-3.8-flash` with the limits and capabilities of `gemini-3.7-flash`.

## 1.2.0 - 2026-09-29

- Add optional model `reasoning_efforts` metadata: omitted/null means unknown,
  an empty list means unsupported, and a non-empty list declares effective choices.
- Add partial capability overrides on model-to-endpoint bindings.
- Add shared reasoning-effort validation fixtures and catalog revision 10.
- Add `reasoning_effort_aliases` for documented compatibility inputs; effective
  choices remain separate from aliases and requests preserve the original input.
- Record per-model official evidence, explicit unsupported entries and unknown
  values in `docs/reasoning-effort-sources.md`. DeepSeek has low/high/max and none
  for off; minimal maps to low, medium/xhigh to high and ultra to max.
- Align `deepseek-v4.1-flash` effort choices and compatibility aliases with `deepseek-flash`.
- Declare GLM-5.2 thinking as configurable; retain its off/high/max choices and
  aliases separately from GLM-5.3/FLASH low/high/max.
- Exclude the Gemini 3.1 Pro minimal alias after the official live route rejected
  it, despite the compatibility table mapping it to low.

## Catalog revision 4 - 2026-09-10

- Add `deepseek-v4.1-flash` and `deepseek-flash` with the same limits and
  capabilities as `deepseek-v4-flash-vision-exp`.

## 1.1.0 - 2026-09-08

- Add optional Settings `EndpointBinding.priority`, defaulting to 1 and
  requiring an integer value greater than or equal to 1.

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
