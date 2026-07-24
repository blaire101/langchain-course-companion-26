from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.common import DATA_DIR, get_embeddings, get_model


class TicketClassification(BaseModel):
    category: Literal["billing", "product", "technical", "other"]
    priority: Literal["low", "medium", "high"]
    summary: str = Field(description="One-sentence summary")


def build_index() -> FAISS:
    documents = []
    for path in sorted(DATA_DIR.glob("*.txt")):
        docs = TextLoader(str(path), encoding="utf-8").load()
        for doc in docs:
            doc.metadata["file_name"] = path.name
        documents.extend(docs)

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=60,
    ).split_documents(documents)
    return FAISS.from_documents(chunks, get_embeddings())


def classify_ticket(text: str) -> TicketClassification:
    model = get_model().with_structured_output(TicketClassification)
    return model.invoke(
        "Classify the following support ticket. Use high priority only for severe service impact.\n\n"
        f"Ticket: {text}"
    )


def build_agent(index: FAISS):
    @tool
    def search_support_documents(query: str) -> str:
        """Search product, refund, pricing, and support-policy documents."""
        docs = index.similarity_search(query, k=3)
        return "\n\n".join(
            f"SOURCE: {doc.metadata.get('file_name')}\n{doc.page_content}" for doc in docs
        )

    @tool
    def monthly_cost(plan_price: float, months: int) -> float:
        """Calculate total subscription cost from a monthly price and number of months."""
        return round(plan_price * months, 2)

    return create_agent(
        model=get_model(),
        tools=[search_support_documents, monthly_cost],
        system_prompt=(
            "You are an Acme Cloud support copilot. Use tools when policy, product, pricing, "
            "or calculation evidence is required. Cite source file names returned by the search tool. "
            "Never invent policy details."
        ),
    )


def main() -> None:
    print("Building local FAISS index...")
    index = build_index()

    ticket = "Our production API is unavailable and all customers are affected."
    classification = classify_ticket(ticket)
    print("\nStructured classification:")
    print(classification.model_dump_json(indent=2))

    agent = build_agent(index)
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "Which plan has audit logs, and what is the cost for 12 months?"}]}
    )
    print("\nAgent response:")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
