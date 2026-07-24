# Course API to Modern LangChain

The concepts in the course remain valuable, but LangChain APIs have evolved.

| Earlier course style | Modern direction |
|---|---|
| `LLMChain` | Runnable composition or explicit functions |
| Legacy memory classes | LangGraph checkpointers / message state |
| Manual JSON parsing | `with_structured_output(PydanticModel)` |
| Legacy agent executors | `create_agent()` |
| Older retrieval chains | Explicit retriever + prompt/model composition or current retrieval helpers |

## Key principle

Learn the abstraction, not only the exact import path:

- model
- prompt
- message history
- chain
- retriever
- tool
- agent
- evaluator

## Why this matters

In interviews, say:

> I studied the course concepts and implemented them using the current LangChain API. I understand that LangChain evolves quickly, so I focus on stable architectural concepts and verify current APIs in the official documentation.
