from langchain_core.prompts import ChatPromptTemplate

ROUTER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI router.

Choose ONLY ONE tool.

Available tools:

chat
summary
sql
python
visualization
automl

Rules:

Return ONLY ONE WORD.

Never explain.

Never use punctuation.
            """
        ),
        (
            "human",
            """
User Request:

{question}
            """
        )
    ]
)   