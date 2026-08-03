"""
Graph Service

Single entry point for executing the LangGraph workflow.
"""

from ai.graph.graph import build_graph


class GraphService:

    _graph = build_graph()

    @classmethod
    def invoke(
        cls,
        df,
        question,
        chat_history
    ):

        state = {
            "df": df,
            "question": question,
            "tool": "",
            "result": "",
            "chat_history": chat_history,
        }

        result = cls._graph.invoke(state)

        return result["result"]