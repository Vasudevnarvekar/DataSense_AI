import streamlit as st

from utils.ai_recommendation import generate_ai_recommendations


def show_ai_recommendations(df):
    """
    Display AI-generated dataset recommendations.
    """

    st.subheader("🤖 AI Recommendation Engine")

    recommendations, quality_score = generate_ai_recommendations(df)

    # -----------------------------------------
    # Recommendation Statistics
    # -----------------------------------------

    total = len(recommendations)

    high = sum(r["priority"] == "High" for r in recommendations)
    medium = sum(r["priority"] == "Medium" for r in recommendations)
    low = sum(r["priority"] == "Low" for r in recommendations)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Quality Score", f"{quality_score}/100")
    col2.metric("Total Issues", total)
    col3.metric("High Priority", high)
    col4.metric("Medium Priority", medium)

    st.divider()

    if total == 0:
        st.success("🎉 Excellent! No major issues were detected.")
        return

    # -----------------------------------------
    # High Priority
    # -----------------------------------------

    high_recs = [r for r in recommendations if r["priority"] == "High"]

    if high_recs:
        with st.expander(f"🔴 High Priority ({len(high_recs)})", expanded=True):

            for rec in high_recs:
                st.error(f"**{rec['title']}**\n\n{rec['description']}")

    # -----------------------------------------
    # Medium Priority
    # -----------------------------------------

    medium_recs = [r for r in recommendations if r["priority"] == "Medium"]

    if medium_recs:
        with st.expander(f"🟡 Medium Priority ({len(medium_recs)})", expanded=True):

            for rec in medium_recs:
                st.warning(f"**{rec['title']}**\n\n{rec['description']}")

    # -----------------------------------------
    # Low Priority
    # -----------------------------------------

    low_recs = [r for r in recommendations if r["priority"] == "Low"]

    if low_recs:
        with st.expander(f"🟢 Low Priority ({len(low_recs)})"):

            for rec in low_recs:
                st.info(f"**{rec['title']}**\n\n{rec['description']}")

                
    # ----------------------------
    # No Recommendations
    # ----------------------------
    if not recommendations:
        st.success("🎉 Excellent! No major issues were detected in your dataset.")
        return

    # ----------------------------
    # Display Recommendations
    # ----------------------------
    for rec in recommendations:

        priority = rec["priority"]
        title = rec["title"]
        description = rec["description"]

        if priority == "High":
            st.error(f"🔴 {title}\n\n{description}")

        elif priority == "Medium":
            st.warning(f"🟡 {title}\n\n{description}")

        else:
            st.info(f"🟢 {title}\n\n{description}")