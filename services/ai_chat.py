"""
AI Chat Service
"""

import pandas as pd

from ai.llm.provider import LLMProvider
from ai.prompts.chat import CHAT_PROMPT

from services.dataset_profile import DatasetProfileService


class AIChatService:

    @staticmethod
    def ask(
        df: pd.DataFrame,
        question: str,
        chat_history: list
    ) -> str:

        dataset_profile = DatasetProfileService.build(df)

        llm = LLMProvider.get_llm()

        chain = CHAT_PROMPT | llm

        response = chain.invoke(
            {
                "dataset_profile": dataset_profile,
                "question": question,
                "chat_history": chat_history
            }
        )

        return response.content