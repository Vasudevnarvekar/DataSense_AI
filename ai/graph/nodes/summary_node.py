from services.ai_summary import AISummaryService


def summary_node(state):

    summary = AISummaryService.generate_summary(
        state["df"]
    )

    return {
        "result": summary
    }