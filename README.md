# LangChain for LLM Application Development — Study Companion

> An original learning companion aligned to the public syllabus of DeepLearning.AI's **LangChain for LLM Application Development**.
>
> This package does **not** reproduce the course's proprietary videos, transcripts, quiz answers, or original notebooks. Download the official notebooks from the course workspace using **File → Download as → Notebook (.ipynb)**. This package provides original notes, modern LangChain examples, exercises, a mini-project, and a one-day study plan.

## What is included

- Bilingual study notes for all six coding modules
- Six original Jupyter notebooks
- One end-to-end customer-support mini-project
- Course-to-modern-LangChain migration notes
- Practice exercises and answer guidance
- Interview cheat sheet
- One-day learning plan

## Course map

| Module | Core idea | Notebook |
|---|---|---|
| Models, Prompts, Parsers | Model invocation, prompt templates, structured output | `01_models_prompts_parsers.ipynb` |
| Memory | Conversation history and thread state | `02_memory.ipynb` |
| Chains | Compose steps into reusable pipelines | `03_chains.ipynb` |
| Document Q&A | Retrieval-Augmented Generation over private data | `04_document_qa.ipynb` |
| Evaluation | Test quality with repeatable examples and metrics | `05_evaluation.ipynb` |
| Agents | Let a model choose and call tools | `06_agents.ipynb` |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
jupyter lab
```

Then open notebooks in order from `notebooks/`.

## Recommended one-day order

1. Read `notes/00_ONE_DAY_PLAN.md`
2. Watch each course lesson at 1.5× speed
3. Run the matching notebook immediately after the lesson
4. Complete only the "Must Do" exercises
5. Run the mini-project in `src/support_copilot.py`
6. Review `notes/08_INTERVIEW_CHEAT_SHEET.md`

## Mini-project

The included project is a **Customer Support Copilot** that:

- classifies a customer request into a structured schema;
- remembers the current conversation;
- retrieves product and policy information from local documents;
- evaluates groundedness with a small test set;
- uses an agent to choose between policy search and a calculator tool.

Run:

```bash
python -m src.support_copilot
```

## Important note on versions

The original course was created with an older LangChain API. This package uses modern LangChain patterns where practical. See:

- `notes/07_COURSE_TO_MODERN_LANGCHAIN.md`

