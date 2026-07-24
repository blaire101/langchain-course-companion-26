# 2. Memory

## Core idea

Memory allows an application to reuse information from earlier turns.

```text
Thread ID → Stored messages → Model sees relevant history
```

## Types

- Short-term memory: conversation history inside one thread
- Long-term memory: information persisted across threads or sessions

## Production concerns

- Context windows are finite.
- Sending all history increases cost and latency.
- Sensitive history needs retention and access policies.
- Production memory should use persistent storage, not an in-memory dictionary.

## Interview answer

> For a prototype, I use an in-memory checkpointer keyed by thread ID. In production, I would move conversation state to a persistent store and apply summarization, retention, and access-control policies.
