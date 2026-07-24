# 1. Models, Prompts and Output Parsers

## Core idea

```text
User input → Prompt template → Chat model → Structured result
```

### Model
A model is the reasoning and generation component. LangChain provides a common interface over model providers.

模型负责理解和生成内容；LangChain负责统一调用方式以及把模型连接到其他组件。

### Prompt
A prompt template combines fixed instructions with runtime variables.

Prompt 不只是字符串，而是可复用的指令模板。

### Output parser / structured output
Applications need predictable fields, not uncontrolled prose. Modern LangChain commonly uses Pydantic schemas through `with_structured_output()`.

生产系统通常需要 JSON 或 Pydantic 对象，而不是一段无法稳定解析的文本。

## Interview answer

> I use prompt templates to separate system instructions from runtime data, and structured output to convert model responses into validated objects that downstream systems can safely consume.

## Common mistake

Do not rely on prompt wording alone to guarantee JSON. Prefer provider-native or tool-based structured output with schema validation.
