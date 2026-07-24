# Interview Cheat Sheet

## 30-second project explanation

> I built a customer-support copilot using LangChain. It classifies incoming requests into structured fields, maintains thread-level conversation memory, retrieves evidence from product and policy documents using FAISS, evaluates answers against a small test set, and uses an agent to select between document search and calculation tools. I implemented the course concepts using modern LangChain APIs and kept the pipeline modular for future deployment.

## What is LangChain?

> LangChain is an application orchestration framework that connects language models with prompts, structured outputs, memory, retrieval systems, and tools.

## What is RAG?

> RAG retrieves relevant external knowledge at query time and supplies it to the model so the answer is grounded in current or private information.

## Chain vs agent

> A chain follows a predefined sequence. An agent dynamically decides which tools to call and in what order.

## What would you improve for production?

> I would add persistent vector and conversation stores, document-level authorization, hybrid retrieval and reranking, offline and online evaluation, observability, rate limits, caching, and human review for low-confidence responses.
