import pandas as pd

from ai.graph.nodes.summary_node import summary_node

df = pd.read_csv(r"C:\Users\vasud\Downloads\Salary_Data (2).csv")

state = {
    "df": df,
    "question": "Give summary",
    "tool": "summary",
    "result": "",
    "chat_history": []
}

result = summary_node(state)

print(result["result"])