from ai.llm.provider import LLMProvider


llm = LLMProvider.get_llm()

response = llm.invoke(
    "Introduce yourself in one sentence."
)

print(response.content)