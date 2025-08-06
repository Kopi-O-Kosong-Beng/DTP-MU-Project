import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CO₂ Emissions Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and introduction
st.title("CO₂ Emissions Explorer")
st.markdown(
    """
    Welcome to the CO₂ Emissions Explorer! Use the sidebar menu to navigate between:
    - **Case Studies**: Historical trends for Wyoming (WY), North Dakota (ND), and Alaska (AK).
    - **Prediction**: Forecast CO₂ emissions per capita based on your inputs.
    - **HASS Reflection**: Qualitative analysis and insights.

    This app is built with Streamlit and modularized for clarity and scalability.
    """
)

# Add vertical spacing above the logo using Streamlit
st.write("")
st.write("")

# Display logo under introduction if available
try:
    from PIL import Image
    logo = Image.open("assets/future.png")
    st.image(logo, width=500)
except Exception:
    pass

# Sidebar navigation instructions
st.sidebar.header("Navigation")
st.sidebar.markdown(
    "Select a page from the top-left menu to begin."
)
