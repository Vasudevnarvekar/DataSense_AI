from ai.graph.nodes.router_node import router_node

state = {
    "df": None,
    "question": "Give me a summary of the dataset",
    "tool": "",
    "result": "",
    "chat_history": []
}

result = router_node(state)

print(result)