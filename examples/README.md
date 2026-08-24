# ChatRequest examples

- `basic-chat-request.json` — text completion.
- `tools-chat-request.json` — function tool with an object `tool_choice`.
- `multimodal-chat-request.json` — flat and nested image URL forms.

All files satisfy `schemas/chat-request.v1.schema.json` and are checked by
`python scripts/validate_contract.py`.

## 中文

- `basic-chat-request.json`：文本对话。
- `tools-chat-request.json`：函数工具与 object `tool_choice`。
- `multimodal-chat-request.json`：flat 与 nested 两种图片 URL 结构。

运行 `python scripts/validate_contract.py` 校验全部示例。
