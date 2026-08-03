from services.tool_result import ToolResult
from services.tools.base_tool import BaseTool


class PythonTool(BaseTool):

    @property
    def name(self):
        return "python"

    def execute(self, df, **kwargs):

        return ToolResult(
            success=False,
            tool=self.name,
            message="Python integration coming soon."
        )