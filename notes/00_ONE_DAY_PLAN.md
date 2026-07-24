# One-Day Study Plan

## Goal

By the end of today, you should be able to explain and demonstrate:

```text
Model → Prompt → Structured Output
Conversation → Memory
Steps → Chain
Documents → Embeddings → Retrieval → Answer
Test Cases → Evaluation
Question → Agent → Tool → Final Answer
```

## Schedule

| Time | Activity | Output |
|---|---|---|
| 09:00–09:25 | Models, Prompts, Parsers lesson + notebook | Structured ticket classifier |
| 09:25–09:50 | Memory lesson + notebook | Two-turn conversation |
| 09:50–10:15 | Chains lesson + notebook | Reusable analysis chain |
| 10:15–10:45 | Document Q&A lesson + notebook | Small RAG system |
| 10:45–11:15 | Evaluation lesson + notebook | Five-question test set |
| 11:15–11:45 | Agents lesson + notebook | Tool-calling agent |
| 13:00–15:00 | Build mini-project | Customer Support Copilot |
| 15:00–16:00 | Read migration guide | Explain old vs modern APIs |
| 16:00–17:00 | Practice interview answers | 30-second and 2-minute explanation |
| 17:00–18:00 | Push to GitHub | README, screenshot, architecture |

## Must understand

1. LangChain is an orchestration framework, not an LLM.
2. A prompt template separates reusable instructions from runtime input.
3. Structured output converts free text into validated fields.
4. Memory means storing and reusing conversation state.
5. A chain is a deterministic sequence of components.
6. RAG retrieves external context before generation.
7. Evaluation should use repeatable questions and expected criteria.
8. An agent chooses tools dynamically; a chain follows a predefined path.

## Skip today

- Fine-tuning
- Multi-agent systems
- Persistent production memory
- Reranking
- LangSmith deployment
- Complex LangGraph workflows
