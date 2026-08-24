# vv-llm-contract

`vv-llm-contract` 是 Python `vv-llm`、Rust `vv-llm-rs` 与 TypeScript
`vv-llm-ts` 共用的语言无关契约仓库。

本仓库是可序列化 JSON 结构、一致性 fixture 和默认模型目录的权威来源。

## 仓库内容

- `schemas/`：基于 JSON Schema 2020-12 的 chat、流式事件、错误、检索、
  Settings V2 与模型目录契约。
- `fixtures/`：三种语言均应在无密钥、无网络条件下通过的映射与归一化样例。
- `examples/`：通过 schema 校验的 canonical `ChatRequest`。
- `catalog/`：单独修订的默认聊天模型目录快照。
- `manifest.json`：contract、schema、fixture 与 catalog 版本清单。
- `checksums.sha256`：所有发布 artifact 的完整性校验值。
- `consumer-lock.v1.json`：运行时仓库消费的固定版本与哈希清单。
- `scripts/validate_contract.py`：仓库完整性和 schema 校验入口。

canonical JSON 统一使用 `snake_case`。各语言 API 可以使用本语言的命名习惯，
在 contract 边界显式转换。

canonical chat 与 error 外层对象采用严格模式：未知字段必须使用 `x_` 扩展前缀。
Provider 原始 wire payload、Settings V2、模型目录项和检索响应保持开放，用于
保留 transport metadata 与 provider 字段。

## Canonical ChatRequest

`schemas/chat-request.v1.schema.json` 定义可移植的请求结构。先看
[examples](examples/README.md)。

| Canonical 字段 | Adapter 职责 |
| --- | --- |
| `options` | 保持嵌套，由 transport adapter 构造 provider 请求。 |
| `tools` | 使用 canonical tool 结构，由 provider adapter 添加 wire envelope。 |
| `tool_choice` | 同时保留具名字符串选择与 opaque object 两种形式。 |
| `extra_body` | 保持为 opaque JSON，在构造 provider 请求时合并。 |
| `x_*` | 在 canonical 编解码中原样往返；transport 行为由扩展自身定义。 |

各运行时提供 typed `ChatRequest` API 和显式 canonical JSON codec。方法名与流式
返回类型由各语言运行时定义。

## 校验

```text
python -m pip install -r requirements-dev.txt
python scripts/validate_contract.py
python -m unittest discover -s tests -v
python scripts/build_bundle.py
```

推送 `v<contract_version>` tag 后，release workflow 会执行这些校验并构建 ZIP。

所有校验均为本地确定性测试，不读取密钥，也不调用真实模型接口。

## 运行时消费方式

各语言运行时的发布包携带固定版本的 contract 文件。应用安装运行时后不需要本仓库。

运行时维护者应显式执行升级：

1. 下载并校验带 tag 的 release bundle。
2. 将解压后的 release 目录传给运行时的同步命令。
3. 更新运行时外部的 consumer-lock 固定值，并运行打包测试。

## 版本规则

- contract 仓库独立使用 SemVer。
- schema 与 fixture 自身携带明确版本。
- 新增可选字段属于 minor；字段改名、类型、必填性、枚举含义或归一化语义变化
  属于 major，并创建新的 schema 版本。
- 模型目录通过 `catalog_revision` 单独修订，不强迫 contract 升 major。
- 三个运行时包继续独立发版，只需固定 contract 版本和 artifact SHA-256。

运行时必须在 vendored tree 之外固定 consumer lock 自身的哈希。当前 SHA-256
随 release 发布，并记录在各运行时中。

## 不包含的内容

HTTP 客户端、认证、重试、middleware、fallback、tokenizer、provider SDK、真实
接口测试和业务消息由各运行时负责。
