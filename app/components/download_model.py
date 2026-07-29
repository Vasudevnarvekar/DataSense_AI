import io
import joblib
import streamlit as st


def show_model_download(
    pipeline,
    model_name,
):
    """
    Download the trained pipeline as a .pkl file.
    """

    st.divider()
    st.subheader("💾 Download Best Model")

    buffer = io.BytesIO()

    joblib.dump(
        pipeline,
        buffer,
    )

    buffer.seek(0)

    filename = (
        model_name.lower()
        .replace(" ", "_")
        + "_model.pkl"
    )

    st.download_button(
        label="⬇️ Download Trained Model",
        data=buffer,
        file_name=filename,
        mime="application/octet-stream",
        use_container_width=True,
    )