from app.services.vector_store import search
from app.services.llm import generate_answer


def build_context(chunks):
    context = ""

    for c in chunks:
        context += f"- {c['text']}\n"

    return context


def ask_copilot(patient_id: int, question: str):

    # 1. Retrieve relevant patient memory
    relevant_chunks = search(question, k=5)

    if not relevant_chunks:
        return {
            "answer": "Insufficient patient data to answer this question.",
            "sources": []
        }

    # 2. Build grounded context
    context = build_context(relevant_chunks)

    # 3. STRICT clinical prompt (VERY IMPORTANT)
    prompt = f"""
You are a clinical AI assistant.

RULES:
- Only use the provided patient data
- Do NOT assume or hallucinate
- If data is insufficient, say "insufficient data"

PATIENT DATA:
{context}

QUESTION:
{question}

ANSWER in concise clinical reasoning:
"""

    # 4. LLM call
    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "sources": relevant_chunks
    }