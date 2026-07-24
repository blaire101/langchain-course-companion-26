# 5. Evaluation

## Why evaluation matters

LLM outputs are probabilistic. A demo that works once is not evidence of reliability.

## Evaluation layers

1. Retrieval: Did the system retrieve the correct evidence?
2. Groundedness: Is the answer supported by the evidence?
3. Correctness: Does the answer match expected facts?
4. Relevance: Does it directly answer the question?
5. Format: Does the structured output validate?
6. Operational: Latency, errors, and cost

## Minimum evaluation set

Create 5–20 representative questions with:

- expected source;
- expected keywords or facts;
- whether the question is answerable;
- expected behavior when evidence is missing.

## Interview answer

> I evaluate retrieval and generation separately. This helps distinguish a retrieval failure from a generation failure and makes optimization more targeted.
