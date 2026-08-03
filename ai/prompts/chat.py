from langchain_core.prompts import ChatPromptTemplate

CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Senior Data Analyst.

Answer ONLY using the provided dataset profile and previous conversation.

Rules:

1. Never invent facts.
2. If information is unavailable, say so.
3. Keep answers clear and professional.
4. Use Markdown formatting.
5. Give actionable business insights whenever possible.
            """
        ),
        (
            "human",
            """
Dataset Profile:

{dataset_profile}

Conversation History:

{chat_history}

User Question:

{question}
            """
        ),
    ]
)