"""
Conversation Memory Service

Manages chat history for the AI assistant.
"""


class ConversationMemoryService:

    @staticmethod
    def add_message(chat_history, role, content):
        """
        Add a message to chat history.
        """

        chat_history.append(
            {
                "role": role,
                "content": content
            }
        )

        return chat_history

    @staticmethod
    def to_prompt(chat_history):
        """
        Convert Streamlit chat history into
        prompt history for the LLM.
        """

        formatted_history = []

        current_user = None

        for message in chat_history:

            if message["role"] == "user":

                current_user = message["content"]

            elif message["role"] == "assistant":

                formatted_history.append(
                    {
                        "user": current_user or "",
                        "assistant": message["content"]
                    }
                )

                current_user = None

        return formatted_history

    @staticmethod
    def clear():
        """
        Return an empty conversation.
        """

        return []