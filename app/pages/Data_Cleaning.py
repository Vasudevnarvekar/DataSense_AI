import streamlit as st
from app.cleaning_dashboard import show_cleaning_dashboard

st.set_page_config(
    page_title="Data Cleaning",
    page_icon="🧹",
    layout="wide"
)

show_cleaning_dashboard()