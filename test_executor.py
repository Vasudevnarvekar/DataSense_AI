import pandas as pd

from services.tool_executor import ToolExecutorService

df = pd.read_csv(r"C:\Users\vasud\Downloads\Salary_Data (2).csv")

result = ToolExecutorService.execute(
    tool_name="summary",
    df=df
)

print(result.to_dict())