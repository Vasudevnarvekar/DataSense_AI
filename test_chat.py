import pandas as pd

from services.ai_chat import AIChatService


df = pd.read_csv(r"C:\Users\vasud\Downloads\Salary_Data (2).csv")

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer = AIChatService.ask(df, question)

    print("\nAI:\n")
    print(answer)