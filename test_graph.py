import pandas as pd

from ai.graph.graph import build_graph

graph = build_graph()

df = pd.read_csv(r"C:\Users\vasud\Downloads\cleaned_dataset.csv")

result = graph.invoke(
    {
        "df": df,
        "question": "Give me summary of dataset",
        "tool": "",
        "result": "",
        "chat_history": []
    }
)

print(result["result"])