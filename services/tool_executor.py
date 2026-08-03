"""
Tool Executor
"""

from services.tool_result import ToolResult

from services.tools.summary_tool import SummaryTool
from services.tools.automl_tool import AutoMLTool
from services.tools.sql_tool import SQLTool
from services.tools.visualization_tool import VisualizationTool
from services.tools.python_tool import PythonTool


class ToolExecutorService:

    TOOLS = {
        "summary": SummaryTool(),
        "automl": AutoMLTool(),
        "sql": SQLTool(),
        "visualization": VisualizationTool(),
        "python": PythonTool(),
    }

    @staticmethod
    def execute(tool_name, df, **kwargs):

        tool = ToolExecutorService.TOOLS.get(tool_name)

        if tool is None:

            return ToolResult(
                success=False,
                tool=tool_name,
                message="Unknown tool."
            )

        return tool.execute(df, **kwargs)