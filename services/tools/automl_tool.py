from services.tool_result import ToolResult
from services.tools.base_tool import BaseTool


class AutoMLTool(BaseTool):

    @property
    def name(self):
        return "automl"

    def execute(self, df, **kwargs):

        return ToolResult(
            success=False,
            tool=self.name,
            message="AutoML integration coming soon."
        )