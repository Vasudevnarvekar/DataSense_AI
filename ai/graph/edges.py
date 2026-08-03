from typing import Literal


def route_after_router(state) -> Literal["summary", "chat"]:

    if state["tool"] == "summary":
        return "summary"

    return "chat"