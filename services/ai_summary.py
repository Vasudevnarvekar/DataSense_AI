"""
AI Summary Service
"""

import pandas as pd

from ai.llm.provider import LLMProvider
from ai.prompts.summary import SUMMARY_PROMPT

from services.dataset_profile import DatasetProfileService
from services.ai_parser import AIResponseParser


class AISummaryService:
    """
    Service responsible for generating AI-powered dataset summaries.
    """

    @staticmethod
    def generate_summary(df: pd.DataFrame) -> str:
        """
        Generate an AI summary for the given dataset.

        Parameters
        ----------
        df : pd.DataFrame
            Input dataset.

        Returns
        -------
        str
            Parsed AI-generated summary.
        """

        # -----------------------------
        # Validate Input
        # -----------------------------

        if df is None or df.empty:
            return "Dataset is empty."

        # -----------------------------
        # Build Dataset Profile
        # -----------------------------

        dataset_profile = DatasetProfileService.build(df)

        # -----------------------------
        # Load LLM
        # -----------------------------

        llm = LLMProvider.get_llm()

        # -----------------------------
        # Create Prompt Chain
        # -----------------------------

        chain = SUMMARY_PROMPT | llm

        # -----------------------------
        # Generate AI Response
        # -----------------------------

        response = chain.invoke(
            {
                "dataset_profile": dataset_profile
            }
        )

        # -----------------------------
        # Parse Response
        # -----------------------------

        return AIResponseParser.parse(response.content)