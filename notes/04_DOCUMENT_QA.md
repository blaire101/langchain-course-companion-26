# 4. Question Answering over Documents

## RAG flow

```text
Documents
→ Load
→ Split into chunks
→ Create embeddings
→ Store vectors
→ Retrieve relevant chunks
→ Add chunks to prompt
→ Generate grounded answer
```

## Why RAG

- LLM training knowledge may be outdated.
- Private company documents are not in model training data.
- Retrieval provides evidence at query time.
- Source metadata improves traceability.

## Important design choices

- Chunk size and overlap
- Embedding model
- Retrieval top-k
- Metadata and access filters
- Prompt instructions for insufficient evidence
- Evaluation of retrieval and final answers

## Interview answer

> RAG separates knowledge from the model. I index external documents as embeddings, retrieve the most relevant chunks at query time, and require the model to answer only from that context while returning source metadata.
