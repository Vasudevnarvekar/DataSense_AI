from operator import add
from typing import Annotated

import pandas as pd
from typing_extensions import TypedDict


class GraphState(TypedDict):
    df: pd.DataFrame
    question: str
    tool: str
    result: str
    chat_history: Annotated[list, add]