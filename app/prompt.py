def create_prompt(
    question,
    category,
    urgency,
    documents
):

    context = "\n\n".join(documents)

    prompt = f"""
You are a helpful customer support assistant.

Answer the user's question using ONLY the provided knowledge.

Category:
{category}

Urgency:
{urgency}

Knowledge:
{context}

User question:
{question}

Instructions:
- Give a clear and concise answer.
- Do not invent information.
- If the knowledge does not contain the answer, say that you do not have enough information.
"""

    return prompt