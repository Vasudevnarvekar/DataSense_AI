import pandas as pd

from utils.python_engine import execute_python_code

df = pd.DataFrame({
    "Age": [21, 24, 30]
})

success, output = execute_python_code(
    """
print(df.head())
print(df["Age"].mean())
""",
    df
)

print(success)
print(output)