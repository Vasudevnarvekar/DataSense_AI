"""
Summary Tool
"""

from services.ai_summary import AISummaryService
from services.tool_result import ToolResult
from services.tools.base_tool import BaseTool


class SummaryTool(BaseTool):

    @property
    def name(self):
        return "summary"

    def execute(self, df, **kwargs):

        summary = AISummaryService.generate_summary(df)

        return ToolResult(
            success=True,
            tool=self.name,
            data=summary,
            message="Summary generated successfully."
        )