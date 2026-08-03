from services.tool_result import ToolResult
from services.tools.base_tool import BaseTool


class VisualizationTool(BaseTool):

    @property
    def name(self):
        return "visualization"

    def execute(self, df, **kwargs):

        return ToolResult(
            success=False,
            tool=self.name,
            message="Visualization integration coming soon."
        )