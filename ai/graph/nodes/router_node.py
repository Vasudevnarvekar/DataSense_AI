from services.tool_router import ToolRouterService


def router_node(state):

    tool = ToolRouterService.route(
        state["question"]
    )

    return {
        "tool": tool
    }