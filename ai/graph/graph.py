from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from ai.graph.state import GraphState

from ai.graph.nodes.router_node import router_node
from ai.graph.nodes.summary_node import summary_node
from ai.graph.nodes.chat_node import chat_node

from ai.graph.edges import route_after_router


def build_graph():

    builder = StateGraph(GraphState)

    builder.add_node(
        "router",
        router_node
    )

    builder.add_node(
        "summary",
        summary_node
    )

    builder.add_node(
        "chat",
        chat_node
    )

    builder.add_edge(
        START,
        "router"
    )

    builder.add_conditional_edges(
        "router",
        route_after_router
    )

    builder.add_edge(
        "summary",
        END
    )

    builder.add_edge(
        "chat",
        END
    )

    return builder.compile()