from services.tool_result import ToolResult
from services.tools.base_tool import BaseTool


class SQLTool(BaseTool):

    @property
    def name(self):
        return "sql"

    def execute(self, df, **kwargs):

        return ToolResult(
            success=False,
            tool=self.name,
            message="SQL integration coming soon."
        )