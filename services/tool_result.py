"""
Tool Result

Standard response object for all tools.
"""


class ToolResult:

    def __init__(
        self,
        success: bool,
        tool: str,
        data=None,
        message=""
    ):
        self.success = success
        self.tool = tool
        self.data = data
        self.message = message

    def to_dict(self):

        return {
            "success": self.success,
            "tool": self.tool,
            "data": self.data,
            "message": self.message,
        }