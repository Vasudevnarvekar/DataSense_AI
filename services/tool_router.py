"""
LLM Tool Router
"""

from ai.llm.provider import LLMProvider
from ai.prompts.router import ROUTER_PROMPT


class ToolRouterService:

    VALID_TOOLS = {
        "chat",
        "summary",
        "sql",
        "python",
        "visualization",
        "automl",
    }

    @staticmethod
    def route(question: str) -> str:

        try:

            llm = LLMProvider.get_llm()

            chain = ROUTER_PROMPT | llm

            response = chain.invoke(
                {
                    "question": question
                }
            )

            tool = response.content.strip().lower()

            if tool in ToolRouterService.VALID_TOOLS:
                return tool

        except Exception:
            pass

        # Fallback
        return ToolRouterService.rule_based_route(question)

    @staticmethod
    def rule_based_route(question: str):

        question = question.lower()

        if "summary" in question or "overview" in question:
            return "summary"

        if "sql" in question:
            return "sql"

        if "python" in question:
            return "python"

        if (
            "chart" in question
            or "plot" in question
            or "graph" in question
            or "heatmap" in question
        ):
            return "visualization"

        if (
            "train" in question
            or "model" in question
            or "predict" in question
        ):
            return "automl"

        return "chat"