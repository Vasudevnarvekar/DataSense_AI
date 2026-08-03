from langchain_ollama import ChatOllama

from ai.llm.config import LLMConfig


class LLMProvider:
    """
    Create and manage LLM instances.
    """

    @staticmethod
    def get_llm():

        return ChatOllama(

            model=LLMConfig.MODEL,

            temperature=LLMConfig.TEMPERATURE,

            base_url=LLMConfig.BASE_URL,

        )