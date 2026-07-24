# 6. Agents

## Core idea

An agent combines a model with tools and lets the model decide which tool to call.

```text
User request → Model decision → Tool call → Tool result → Final response
```

## Tool design

A tool should have:

- a clear name;
- typed arguments;
- a concise and accurate docstring;
- predictable return values;
- input validation and error handling.

## When to use

Use agents when:

- the user request may need different tools;
- the number or order of steps is not known beforehand;
- tool selection benefits from language understanding.

Avoid agents when a deterministic chain is enough.

## Interview answer

> An agent is useful when the model must decide whether to search documents, calculate a value, or perform another action. I keep the tool set small and descriptions precise to reduce incorrect tool selection.
