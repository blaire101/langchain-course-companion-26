# LangChain Course Companion 2026

A modern, interview-focused companion to **LangChain for LLM Application Development**.

The repository uses **gpt-4o-mini** and covers the full learning path:

```text
Models & Structured Output
→ Memory
→ Chains
→ Document Q&A / RAG
→ Evaluation
→ Agents & Tools
```

## Start Here

### [Open the Complete Interview & Audio Guide](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/INTERVIEW_GUIDE.html)

The guide is English-only and includes:

- Fast memory diagrams
- Clear explanations of what was built
- Three interview questions per lesson
- 30-second interview answers
- One-line résumé descriptions
- Browser-based English pronunciation controls

> Open HTML links in Chrome for the best speech-synthesis experience.

## Lessons

| No. | Notebook | Interview & Audio Guide |
|---:|---|---|
| 1 | [Models, Prompts & Output](notebooks/01_models_prompts_parsers.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/01_models_prompts_parsers.html) |
| 2 | [Memory](notebooks/02_memory.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/02_memory.html) |
| 3 | [Chains](notebooks/03_chains.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/03_chains.html) |
| 4 | [Document Q&A / RAG](notebooks/04_document_qa.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/04_document_qa.html) |
| 5 | [Evaluation](notebooks/05_evaluation.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/05_evaluation.html) |
| 6 | [Agents & Tools](notebooks/06_agents.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/06_agents.html) |
| 7 | [Finial-1-6](notebooks/07.ipynb) | [Interview + Audio](https://htmlpreview.github.io/?https://github.com/blaire101/langchain-course-companion-26/blob/main/docs/LangChain_LLM_Agent_Demo.html) |

## Project Scenario

The six lessons use one consistent **Customer Support Copilot** scenario:

- Classify incoming support tickets into structured fields
- Remember customer context across turns
- Summarize support issues through deterministic chains
- Answer policy questions using RAG and source documents
- Evaluate expected answers with repeatable test cases
- Route requests dynamically across lookup and calculation tools

## Repository Structure

```text
.
├── INTERVIEW_GUIDE.html          # Combined interview and audio guide
├── README.md
├── notebooks/                    # Six executable learning notebooks
├── docs/                         # One interview/audio HTML per notebook
├── assets/                       # PNG, SVG, and DOT diagrams
├── data/                         # Local support-policy documents
└── src/                          # Reusable support-copilot code
```

## Setup

```bash
conda activate g2ai
python -m pip install -U \
  openai \
  "langchain>=1.0,<2.0" \
  langchain-openai \
  langchain-community \
  langgraph \
  faiss-cpu \
  python-dotenv \
  pydantic \
  notebook \
  ipykernel
```

Create `.env` in the repository root:

```env
OPENAI_API_KEY=your_api_key_here
```

Start Jupyter:

```bash
jupyter notebook
```

## Interview Positioning

> I built a customer-support copilot that demonstrates structured output, conversation memory, deterministic chains, source-grounded RAG, repeatable evaluation, and dynamic tool-calling agents using LangChain and gpt-4o-mini.

## Important Notes

- Notebook responses may vary slightly because they are model-generated.
- GitHub notebook previews do not execute JavaScript, so pronunciation is provided in the linked HTML guides.
- All sample business data is fictional and intended only for learning and interview preparation.
