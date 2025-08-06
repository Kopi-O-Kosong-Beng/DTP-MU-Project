import streamlit as st
import pandas as pd
from data_service import load_model, predict_co2

# Page settings
st.set_page_config(page_title="Prediction", layout="wide")

# Title and instructions
st.title("Prediction")
st.markdown(
    "Configure your inputs in the sidebar and click **Run Prediction** to forecast CO₂ emissions per capita."
)

# Sidebar inputs
st.sidebar.header("Input Parameters")
coal_prod = st.sidebar.number_input(
    "Coal Production (million tonnes)", min_value=0.0, value=100.0, step=1.0
)
gas_prod = st.sidebar.number_input(
    "Natural Gas Production (billion cubic meters)", min_value=0.0, value=50.0, step=1.0
)
pci = st.sidebar.number_input(
    "Per Capita Income (USD)", min_value=0.0, value=30000.0, step=1000.0
)
urban_pct = st.sidebar.slider(
    "Urban Population (%)", min_value=0, max_value=100, value=60
)
renew_pct = st.sidebar.slider(
    "Renewable Energy Consumption (%)", min_value=0, max_value=100, value=20
)

# Load model (use cache_resource for persistent model objects)
@st.cache_resource

def get_model():
    """
    Load and cache the ML model resource.
    """
    return load_model("model.joblib")

model = get_model()

# Run prediction
if st.sidebar.button("Run Prediction"):
    # Build input DataFrame
    input_df = pd.DataFrame({
        "Coal Production": [coal_prod],
        "Natural Gas Production": [gas_prod],
        "Per Capita Income": [pci],
        "Urban Population %": [urban_pct],
        "Renewable Energy %": [renew_pct]
    })

    # Predict
    prediction = predict_co2(model, input_df)

    # Display results
    st.subheader("Prediction Result")
    st.metric(label="Predicted CO₂ per capita", value=f"{prediction:.2f}")

    # Show input data
    st.markdown("**Input Data**")
    st.dataframe(input_df)

# Footer note
st.markdown("---")
st.caption("Model: Placeholder dummy model. Replace with actual trained model for real predictions.")
