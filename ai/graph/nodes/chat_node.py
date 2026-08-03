from services.ai_chat import AIChatService


def chat_node(state):

    answer = AIChatService.ask(
        df=state["df"],
        question=state["question"],
        chat_history=state["chat_history"]
    )

    return {
        "result": answer
    }