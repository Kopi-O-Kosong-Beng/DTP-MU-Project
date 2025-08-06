"""
Prediction page for CO₂ emissions per capita using state‐specific linear models.
Includes a feedback form and displays all past user feedback.
"""

import streamlit as st
import pandas as pd

from data_service import predict_co2

# Configure the page BEFORE any other Streamlit calls
st.set_page_config(page_title="Prediction", layout="wide")

# ─────────────────────────────────────────────────────────────────
# Page header
# ─────────────────────────────────────────────────────────────────
st.title("CO₂ Emission Prediction")
st.markdown(
    """
    Select a state model and enter its key drivers below to forecast CO₂ emissions per capita.
    After seeing your result, please leave your name and a quick note on what you think of it.
    """
)

# ─────────────────────────────────────────────────────────────────
# Sidebar: Model selector + inputs
# ─────────────────────────────────────────────────────────────────
st.sidebar.header("Model & Inputs")

state = st.sidebar.selectbox(
    "Select state model",
    ("WY", "ND", "AK"),
    format_func=lambda x: {"WY": "Wyoming", "ND": "North Dakota", "AK": "Alaska"}[x]
)

renewable = st.sidebar.number_input(
    "Renewable energy consumption (Billion Btu/yr)",
    min_value=0.0,
    max_value=300_000.0,
    value=6611.0,
    step=1_000.0,
    format="%.1f",
    help="Typical range by state: 0–300,000 Billion Btu per year"
)

coal = st.sidebar.number_input(
    "Coal electricity consumption (short tons/yr)",
    min_value=0.0,
    max_value=100_000_000.0,
    value=26831408.0,
    step=100_000.0,
    format="%.0f",
    help="Typical range by state: 0–100 million short tons per year"
)

gas = st.sidebar.number_input(
    "Natural gas consumption (thousand cubic feet/yr)",
    min_value=0.0,
    max_value=20_000_000_000.0,
    value=4052911.0,
    step=100_000_000.0,
    format="%.0f",
    help="Typical range by state: 0–20 million cubic feet per year"
)

pce = st.sidebar.number_input(
    "Personal consumption expenditure (USD per person)",
    min_value=0.0,
    max_value=100_000.0,
    value=20184.0,
    step=500.0,
    format="%.0f",
    help="Typical U.S. range: 20,000–60,000 USD per person"
)

urban = st.sidebar.number_input(
    "Urban population (number of people)",
    min_value=0,
    max_value=500_000,
    value=322110,
    step=10_000,
    format="%d",
    help="Enter the estimated number of residents in urban areas"
)

# ─────────────────────────────────────────────────────────────────
# Run prediction and show results
# ─────────────────────────────────────────────────────────────────
if st.sidebar.button("Run Prediction"):
    # Compute prediction
    prediction = predict_co2(
        state_code=state,
        renewable_energy=renewable,
        coal_elec=coal,
        gas_elec=gas,
        pce_per_capita=pce,
        urban_pop=urban
    )

    # Display predicted metric
    st.metric(
        label=f"Predicted CO₂ per Capita ({state})",
        value=f"{prediction:.2f} t"
    )

    # Show the inputs for transparency
    st.subheader("Input Data")
    st.dataframe(
        pd.DataFrame({
            "State": [state],
            "Renewable Energy (%)": [renewable],
            "Coal Electricity Consumption": [coal],
            "Natural Gas Electricity Consumption": [gas],
            "PCE per Capita (USD)": [pce],
            "Estimated Urban Population (%)": [urban]
        })
    )
