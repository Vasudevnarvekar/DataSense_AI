import os
import sys

# ==========================================================
# Add Project Root
# ==========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from services.ai_chat import AIChatService
from services.conversation_memory import ConversationMemoryService
from services.graph_service import GraphService

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="AI Chat",
    page_icon="💬",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

col1, col2 = st.columns([8, 2])

with col1:
    st.title("💬 Chat with your Dataset")

with col2:

    st.write("")

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.chat_history = (
            ConversationMemoryService.clear()
        )

        st.rerun()

st.markdown(
    """
Ask questions about your cleaned dataset using AI.
"""
)

st.divider()

# ==========================================================
# Check Dataset
# ==========================================================

if "cleaned_df" not in st.session_state:

    st.warning(
        "Please upload and clean a dataset first."
    )

    st.stop()

df = st.session_state["cleaned_df"]

# ==========================================================
# Initialize Conversation Memory
# ==========================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

# ==========================================================
# Display Previous Messages
# ==========================================================

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ==========================================================
# Chat Input
# ==========================================================

question = st.chat_input(
    "Ask anything about your dataset..."
)

# ==========================================================
# Handle User Question
# ==========================================================

if question:

    # -----------------------------
    # Store User Message
    # -----------------------------

    ConversationMemoryService.add_message(
        st.session_state.chat_history,
        "user",
        question
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -----------------------------
    # AI Response
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            formatted_history = (
                ConversationMemoryService.to_prompt(
                    st.session_state.chat_history
                )
            )

            answer = GraphService.invoke(
                df=df,
                question=question,
                chat_history=formatted_history
            )

        st.markdown(answer)

    # -----------------------------
    # Store AI Response
    # -----------------------------

    ConversationMemoryService.add_message(
        st.session_state.chat_history,
        "assistant",
        answer
    )