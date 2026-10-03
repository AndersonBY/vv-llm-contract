# Reasoning effort catalog evidence

Verified against official documentation on 2026-09-28; BigModel conditions rechecked on 2026-09-29; GPT-6.1 Sol checked on 2026-09-30; Qwen 3.8 Flash-Next checked on 2026-10-03. Catalog revision: 16.

The catalog contains 216 models: 47 with documented effort choices, 35 explicitly unsupported, and 134 without verified model-specific values. Unknown entries remain omitted/null; they are not guessed from a model name or from thinking support.

`reasoning_efforts` lists effective choices for display and validation. `none`, when present, is an explicit off control, not a reasoning intensity. `reasoning_effort_aliases` records additional documented inputs and their effective target. Aliases are accepted only while their target is in the effective list. Requests preserve the original input for the provider to map. Lists and alias maps on endpoint bindings replace the corresponding model fields.

These defaults describe official model/API combinations. A deployment alias, proxy, Coding Plan, Bedrock or Vertex route can differ and should use binding capabilities. HTTP 200 proves that a request was accepted; it does not prove that a parameter was honored. See the Python runtime live report for response observations and unavailable routes.

## Sources

- `openai`: [OpenAI reasoning/model documentation](https://developers.openai.com/api/docs/guides/reasoning).
- `anthropic`: [Anthropic effort support table (official indexed documentation; direct access redirects to a regional availability page)](https://platform.claude.com/docs/en/build-with-claude/effort).
- `deepseek`: [DeepSeek thinking mode and Chat Completion API](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion).
- `qwen`: [Alibaba Cloud OpenAI-compatible API](https://help.aliyun.com/zh/model-studio/qwen-api-via-openai-chat-completions).
- `qwen-flash-next`: [Official open-weight model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next). Native context is 262,144 tokens; extending it to 1M requires deployment configuration. No fixed hosted output limit or structured-output guarantee is inferred for this model.
- `moonshot`: [Kimi thinking-mode parameter comparison](https://platform.kimi.com/docs/guide/use-kimi-k2-thinking-model).
- `zhipuai`: [BigModel ordinary API thinking guide](https://docs.bigmodel.cn/cn/guide/capabilities/thinking).
- `minimax`: [MiniMax OpenAI-compatible API](https://platform.minimax.io/docs/api-reference/text-openai-api).
- `gemini`: [Google OpenAI compatibility and thinking documentation](https://ai.google.dev/gemini-api/docs/openai).
- `xai`: [xAI reasoning documentation](https://docs.x.ai/developers/model-capabilities/text/reasoning).
- `mistral`: [Mistral reasoning documentation](https://docs.mistral.ai/studio/conversations/reasoning).
- `groq`: [Groq official generated SDK parameter documentation](https://github.com/groq/groq-python/blob/main/src/groq/types/chat/completion_create_params.py).
- `stepfun`: [StepFun Chat Completion and model variant documentation](https://platform.stepfun.com/docs/zh/api-reference/chat).
- `xiaomi`: [MiMo documentation (JavaScript shell; parameter documentation unavailable to this fetch)](https://platform.xiaomimimo.com/docs).
- `yi`: [Yi API documentation (JavaScript shell; model-specific effort documentation unavailable)](https://platform.lingyiwanwu.com/docs/api-reference).
- `baichuan`: [Baichuan documentation (model-specific effort documentation unavailable)](https://platform.baichuan-ai.com/docs/api).
- `ernie`: [Baidu Qianfan documentation (model-specific effort documentation unavailable in fetched page)](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/ylikwm8wt).
- `openai-gpt5`: [OpenAI GPT-5 guide](https://developers.openai.com/api/docs/guides/gpt-5).
- `openai-gpt51`: [OpenAI GPT-5.1 guide](https://developers.openai.com/api/docs/guides/gpt-5.1).
- `openai-model`: [OpenAI model reference (model-specific pages linked below)](https://developers.openai.com/api/docs/models).
- `azure-reasoning`: [Azure OpenAI reasoning support table](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reasoning?view=foundry-classic).
- [DeepSeek Flash 4.1 release](https://api-docs.deepseek.com/updates/2026-09-10) identifies Flash 4.1 and its API name `deepseek-flash`.
- [Google native thinking configuration](https://ai.google.dev/gemini-api/docs/thinking?hl=en) is separate from its OpenAI compatibility layer. Native thinking levels are not copied into this catalog without compatibility-layer evidence.
- [BigModel Chat Completion API](https://docs.bigmodel.cn/api-reference/模型-api/对话补全.md) distinguishes ordinary API values from Coding Plan aliases.

## Provider and model coverage

### moonshot

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `kimi-k2-0711-preview` | Unknown | — | `moonshot` | No verified model-specific effort values. |
| `kimi-k2-0905-preview` | Unknown | — | `moonshot` | No verified model-specific effort values. |
| `kimi-k2-turbo-preview` | Unknown | — | `moonshot` | No verified model-specific effort values. |
| `kimi-k2-thinking` | Unknown | — | `moonshot` | No verified model-specific effort values. |
| `kimi-k2-thinking-turbo` | Unknown | — | `moonshot` | No verified model-specific effort values. |
| `kimi-k2.5` | Unknown | — | `moonshot` | No verified model-specific effort values. |
| `kimi-k2.6` | Unsupported (`[]`) | — | `moonshot` | The model parameter comparison explicitly marks reasoning_effort unsupported. |
| `kimi-k2.7-code` | Unsupported (`[]`) | — | `moonshot` | The model parameter comparison explicitly marks reasoning_effort unsupported. |
| `kimi-k3` | `low`, `high`, `max` | — | `moonshot` | Documented choices. |

### deepseek

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `deepseek-chat` | Unknown | — | `deepseek` | No verified model-specific effort values. |
| `deepseek-reasoner` | Unknown | — | `deepseek` | No verified model-specific effort values. |
| `deepseek-v4-flash` | Unknown | — | `deepseek` | No verified model-specific effort values. |
| `deepseek-v4-flash-vision-exp` | Unknown | — | `deepseek` | No verified model-specific effort values. |
| `deepseek-v4-pro` | `none`, `low`, `high`, `max` | `minimal` → `low`, `medium` → `high`, `xhigh` → `high`, `ultra` → `max` | `deepseek` | none disables thinking; minimal->low; medium/xhigh->high; ultra->max. |
| `deepseek-v4.1-flash` | `none`, `low`, `high`, `max` | `minimal` → `low`, `medium` → `high`, `xhigh` → `high`, `ultra` → `max` | `deepseek` | Shares Flash effort metadata; official API request ID is `deepseek-flash`. |
| `deepseek-flash` | `none`, `low`, `high`, `max` | `minimal` → `low`, `medium` → `high`, `xhigh` → `high`, `ultra` → `max` | `deepseek` | none disables thinking; minimal->low; medium/xhigh->high; ultra->max. |

### baichuan

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `Baichuan4` | Unknown | — | `baichuan` | No verified model-specific effort values. |

### groq

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `mixtral-8x7b-32768` | Unknown | — | `groq` | No verified model-specific effort values. |
| `llama3-70b-8192` | Unknown | — | `groq` | No verified model-specific effort values. |
| `llama3-8b-8192` | Unknown | — | `groq` | No verified model-specific effort values. |
| `gemma-7b-it` | Unknown | — | `groq` | No verified model-specific effort values. |
| `gemma2-9b-it` | Unknown | — | `groq` | No verified model-specific effort values. |
| `llama3-groq-70b-8192-tool-use-preview` | Unknown | — | `groq` | No verified model-specific effort values. |
| `llama3-groq-8b-8192-tool-use-preview` | Unknown | — | `groq` | No verified model-specific effort values. |
| `llama-3.1-70b-versatile` | Unknown | — | `groq` | No verified model-specific effort values. |
| `llama-3.1-8b-instant` | Unknown | — | `groq` | No verified model-specific effort values. |

### qwen

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `qwen2.5-7b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-14b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-32b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-coder-32b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwq-32b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-72b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2-vl-72b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-vl-72b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-vl-7b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen2.5-vl-3b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen-max` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen-max-longcontext` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen-plus` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen-turbo` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qvq-max` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-235b-a22b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-32b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-30b-a3b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-14b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-8b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-4b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-1.7b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-0.6b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-235b-a22b-instruct-2507` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-235b-a22b-thinking-2507` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-coder-480b-a35b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-next-80b-a3b-thinking` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-next-80b-a3b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-max-preview` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-max` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-plus` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-coder-plus` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-coder-flash` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-235b-a22b-thinking` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-235b-a22b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-30b-a3b-thinking` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-30b-a3b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-8b-thinking` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-8b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-flash` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-32b-thinking` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3-vl-32b-instruct` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-397b-a17b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-122b-a10b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-27b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-35b-a3b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-9b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-4b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-2b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.5-0.8b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.6-plus` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.6-flash` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.6-35b-a3b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.6-27b` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.7-max` | Unknown | — | `qwen` | No verified model-specific effort values. |
| `qwen3.8-flash-next` | `low`, `medium`, `xhigh` | — | `qwen-flash-next` | Configurable thinking; xhigh is the default. Disable via enable_thinking, nested in chat_template_kwargs for self-hosted frameworks. Hosted none/alias semantics are not inferred for the open-weight ID. |
| `qwen3.8-max` | `none`, `low`, `medium`, `xhigh` | `minimal` → `low`, `high` → `xhigh`, `max` → `xhigh` | `qwen` | Effective low/medium/xhigh; minimal->low; high/max->xhigh; none disables thinking. Do not combine with thinking_budget. |
| `qwen3.8-27b` | `none`, `low`, `medium`, `xhigh` | `minimal` → `low`, `high` → `xhigh`, `max` → `xhigh` | `qwen` | Effective low/medium/xhigh; minimal->low; high/max->xhigh; none disables thinking. Do not combine with thinking_budget. |

### yi

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `yi-lightning` | Unknown | — | `yi` | No verified model-specific effort values. |
| `yi-vision-v2` | Unknown | — | `yi` | No verified model-specific effort values. |

### zhipuai

The ordinary Chat Completion API applies `reasoning_effort` only while `thinking` is enabled and defaults to `max` when effort is omitted. GLM-5.2 supports configurable thinking (enabled by default); GLM-5.3 and GLM-5.3-FLASH require thinking and reject `thinking.type=disabled`. The global parameter enum combines model-specific inputs and is not a list of effective levels for every model. Coding Plan aliases are separate from ordinary API defaults and can be declared on endpoint bindings.

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `glm-4.5` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.5-x` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.5-air` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.5-airx` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.5-flash` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.5v` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.6` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.6v` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.6v-flash` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.7` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-4.7-flash` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-5` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-5-code` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-5-turbo` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-5v-turbo` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-5.1` | Unsupported (`[]`) | — | `zhipuai` | Documentation explicitly limits effort control to GLM-5.2 and later. |
| `glm-5.2` | `none`, `high`, `max` | `minimal` → `none`, `low` → `high`, `medium` → `high`, `xhigh` → `max` | `zhipuai` | Ordinary API: none/minimal disable thinking; low/medium->high; xhigh->max. |
| `glm-5.3` | `low`, `high`, `max` | — | `zhipuai` | Ordinary API rejects other values; Coding Plan accepts additional aliases via endpoint overrides. |
| `glm-5.3-flash` | `low`, `high`, `max` | — | `zhipuai` | Ordinary API rejects other values; Coding Plan accepts additional aliases via endpoint overrides. |

### mistral

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `open-mistral-7b` | Unknown | — | `mistral` | No verified model-specific effort values. |
| `open-mixtral-8x7b` | Unknown | — | `mistral` | No verified model-specific effort values. |
| `open-mixtral-8x22b` | Unknown | — | `mistral` | No verified model-specific effort values. |
| `open-mistral-nemo` | Unknown | — | `mistral` | No verified model-specific effort values. |
| `codestral-latest` | Unknown | — | `mistral` | No verified model-specific effort values. |
| `mistral-small-latest` | `none`, `high` | — | `mistral` | high returns thinking chunks; none omits the thinking chunk. |
| `mistral-medium-latest` | Unknown | — | `mistral` | No verified model-specific effort values. |
| `mistral-large-latest` | Unknown | — | `mistral` | No verified model-specific effort values. |

### openai

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `gpt-35-turbo` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4-turbo` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4o` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4o-mini` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4v` | Unknown | — | `openai` | No verified model-specific effort values. |
| `o1-mini` | Unsupported (`[]`) | — | `azure-reasoning` | Explicitly does not support reasoning_effort. |
| `o1-preview` | Unknown | — | `openai` | No verified model-specific effort values. |
| `o3` | `low`, `medium`, `high` | — | `azure-reasoning` | O-series support table and legacy low/medium/high controls. |
| `o3-mini` | `low`, `medium`, `high` | — | `azure-reasoning` | O-series support table and legacy low/medium/high controls. |
| `o4-mini` | `low`, `medium`, `high` | — | `azure-reasoning` | O-series support table and legacy low/medium/high controls. |
| `gpt-4.1` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4.1-mini` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-4.1-nano` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5` | `minimal`, `low`, `medium`, `high` | — | `openai-gpt5` | Documented choices. |
| `gpt-5-mini` | `minimal`, `low`, `medium`, `high` | — | `openai-gpt5` | Documented choices. |
| `gpt-5-nano` | `minimal`, `low`, `medium`, `high` | — | `openai-gpt5` | Documented choices. |
| `gpt-5-chat-latest` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5-codex` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5-pro` | `high` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5-pro) | Responses API only. |
| `gpt-5.1` | `none`, `low`, `medium`, `high` | — | `openai-gpt51` | Documented choices. |
| `gpt-5.1-codex` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5.1-codex-mini` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5.1-codex-max` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5.1-chat` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5.2` | `none`, `low`, `medium`, `high`, `xhigh` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.2) | Documented choices. |
| `gpt-5.3-chat` | Unknown | — | `openai` | No verified model-specific effort values. |
| `gpt-5.3-codex` | `low`, `medium`, `high`, `xhigh` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.3-codex) | Responses API. |
| `gpt-5.4` | `none`, `low`, `medium`, `high`, `xhigh` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.4) | Documented choices. |
| `gpt-5.4-pro` | `medium`, `high`, `xhigh` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.4-pro) | Responses API only. |
| `gpt-5.5` | `none`, `low`, `medium`, `high`, `xhigh` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.5) | Documented choices. |
| `gpt-5.6-sol` | `none`, `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.6-sol) | API values; Codex CLI ultra is an orchestration setting, not a documented API effort. |
| `gpt-5.6-terra` | `none`, `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.6-terra) | API values; Codex CLI ultra is an orchestration setting, not a documented API effort. |
| `gpt-5.6-luna` | `none`, `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-5.6-luna) | API values; Codex CLI ultra is an orchestration setting, not a documented API effort. |
| `gpt-6-astra` | `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-6-astra) | none is explicitly unsupported. |
| `gpt-6-sol` | `none`, `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-6-sol) | `max` is Responses API only; live Chat Completions accepted none through xhigh. |
| `gpt-6-luna` | `none`, `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-6-luna) | `max` is Responses API only; live Chat Completions accepted none through xhigh. |
| `gpt-6.1-sol` | `low`, `medium`, `high`, `xhigh`, `max` | — | [model reference](https://developers.openai.com/api/docs/models/gpt-6.1-sol) | `none`/`minimal` unsupported; `max` and tool calling are Responses API only. Live Chat Completions accepted low through xhigh. |

### anthropic

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `claude-3-5-haiku-20241022` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-3-5-sonnet-20240620` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-3-5-sonnet-20241022` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-3-7-sonnet-20250219` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-sonnet-4-20250514` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-opus-4-20250514` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-opus-4-1-20250805` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-sonnet-4-5-20250929` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-haiku-4-5-20251001` | Unsupported (`[]`) | — | `anthropic` | Excluded by the documented effort support table; thinking budgets remain separate. |
| `claude-opus-4-6` | `low`, `medium`, `high`, `max` | — | `anthropic` | Documented choices. |
| `claude-sonnet-4-6` | `low`, `medium`, `high` | — | `anthropic` | Documented choices. |
| `claude-opus-4-7` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Documented choices. |
| `claude-opus-4-8` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Documented choices. |
| `claude-fable-5` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Documented choices. |
| `claude-sonnet-5` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Documented choices. |
| `claude-opus-5` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Documented choices. |
| `claude-opus-5-5` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Inherited from `claude-opus-5`; all five values accepted by a live request on 2026-09-29. |
| `claude-sonnet-5-5` | `low`, `medium`, `high`, `xhigh`, `max` | — | `anthropic` | Documented choices; a live probe accepted all five and rejected `none`. |

### minimax

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `MiniMax-M2.1` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |
| `MiniMax-M2.1-lightning` | Unknown | — | `minimax` | No verified model-specific effort values. |
| `MiniMax-M2.1-highspeed` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |
| `MiniMax-M2.5` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |
| `MiniMax-M2.5-highspeed` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |
| `MiniMax-M2.7` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |
| `MiniMax-M3` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |
| `MiniMax-M2.7-highspeed` | Unsupported (`[]`) | — | `minimax` | Effort is effective only for MiniMax-M3.1-Flash-Preview; that model is not in this catalog. |

### gemini

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `gemini-2.5-pro` | `low`, `medium`, `high` | `minimal` → `low` | `gemini` | OpenAI-compatible values, not native thinking_level values. |
| `gemini-2.5-flash` | `none`, `low`, `medium`, `high` | `minimal` → `low` | `gemini` | 2.5 budgets: minimal/low->1024, medium->8192, high->24576; none->0. |
| `gemini-2.5-flash-lite` | `none`, `low`, `medium`, `high` | `minimal` → `low` | `gemini` | 2.5 budgets: minimal/low->1024, medium->8192, high->24576; none->0. |
| `gemini-3-pro-preview` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3-pro` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3-pro-image-preview` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3-flash-preview` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3-flash` | `minimal`, `low`, `medium`, `high` | — | `gemini` | OpenAI-compatible values, not native thinking_level values. |
| `gemini-3.1-pro-preview` | `low`, `medium`, `high` | — | `gemini` | Official compatibility table maps minimal to low, but a live official-route request rejected minimal (HTTP 400, not supported). Alias excluded pending verification. |
| `gemini-3.1-flash-lite-preview` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3.1-flash-lite` | `minimal`, `low`, `medium`, `high` | — | `gemini` | OpenAI-compatible values, not native thinking_level values. |
| `gemini-3.5-flash` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3.7-flash` | Unknown | — | `gemini` | No verified model-specific effort values. |
| `gemini-3.8-flash` | Unknown | — | `gemini` | No verified model-specific effort values. |

### ernie

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `ernie-lite` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-speed` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-speed-pro-128k` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-3.5-8k` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-3.5-128k` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-4.0-8k-latest` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-4.0-8k` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-4.0-turbo-8k` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-4.5-8k-preview` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-4.5-turbo-128k` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-5.0` | Unknown | — | `ernie` | No verified model-specific effort values. |
| `ernie-5.1` | Unknown | — | `ernie` | No verified model-specific effort values. |

### stepfun

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `step-2-mini` | Unknown | — | `stepfun` | No verified model-specific effort values. |
| `step-3` | Unknown | — | `stepfun` | No verified model-specific effort values. |
| `step-3.5-flash` | Unknown | — | `stepfun` | No verified model-specific effort values. |

### xai

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `grok-4.20-0309-reasoning` | Unknown | — | `xai` | No verified model-specific effort values. |
| `grok-4.20-0309-non-reasoning` | Unknown | — | `xai` | No verified model-specific effort values. |
| `grok-4.20-multi-agent-0309` | Unknown | — | `xai` | No verified model-specific effort values. |
| `grok-4-1-fast-reasoning` | Unknown | — | `xai` | No verified model-specific effort values. |
| `grok-4-1-fast-non-reasoning` | Unknown | — | `xai` | No verified model-specific effort values. |
| `grok-4.6` | `low`, `medium`, `high`, `xhigh` | — | `xai` | Documented choices. |

### xiaomi

| Model | Effective choices | Compatibility inputs | Evidence | Qualification |
| --- | --- | --- | --- | --- |
| `mimo-v2-pro` | Unknown | — | `xiaomi` | No verified model-specific effort values. |
| `mimo-v2-omni` | Unknown | — | `xiaomi` | No verified model-specific effort values. |
| `mimo-v2-tts` | Unknown | — | `xiaomi` | No verified model-specific effort values. |
| `mimo-v2-flash` | Unknown | — | `xiaomi` | No verified model-specific effort values. |

## Observed compatibility limits

- DeepSeek has three effective intensities: low, high and max. Minimal maps to low; medium and xhigh map to high; ultra maps to max. None turns thinking off. These mappings apply to Flash, the V4.1 Flash catalog alias, and V4 Pro; other legacy/vision IDs remain unknown.
- Qwen 3.8 uses low, medium and xhigh, plus none for off. Minimal maps to low; high and max map to xhigh. Do not also send a thinking budget.
- GLM 5.2 documents none/minimal as off, low/medium as high and xhigh as max. In the live response, none and minimal still included reasoning content; the off behavior was not verified. GLM 5.3 ordinary API documents low/high/max; Coding Plan aliases require endpoint overrides.
- Gemini 3.1 Pro: the compatibility document lists minimal → low, but the live official route rejected minimal as unsupported. Low/medium/high succeeded; minimal is excluded pending verification.
- Kimi K3 accepts low/high/max, but the live invalid-value probe was also accepted. The live call cannot establish strict parameter validation or intensity behavior.
- Anthropic direct documentation redirected to a regional availability page during direct fetch; the official indexed effort support table supplied model coverage. Transport acceptance is recorded separately in the runtime report.
