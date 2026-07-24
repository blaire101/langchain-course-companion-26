# 3. Chains

## Core idea

A chain is a predefined sequence of steps.

```text
Input → Prompt → Model → Parser → Output
```

Use a chain when the workflow is known in advance and should be deterministic.

## Chain vs agent

| Chain | Agent |
|---|---|
| Fixed execution path | Model chooses actions dynamically |
| Easier to test | More flexible |
| Lower operational risk | More failure modes |
| Best for stable workflows | Best for ambiguous multi-step tasks |

## Interview answer

> I prefer deterministic chains for stable business processes and introduce agents only when the application genuinely needs dynamic tool selection.
