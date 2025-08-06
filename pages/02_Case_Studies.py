import streamlit as st
import pandas as pd
from data_service import get_co2_per_capita_data

# Page settings
st.set_page_config(page_title="Case Studies", layout="wide")

# Title and description
st.title("Case Studies: WY, ND & AK")
st.markdown(
    "Explore historical CO₂ emissions per capita trends for our three case-study states."
)

# Define the states and their display names
states = [
    ("WY", "Wyoming"),
    ("ND", "North Dakota"),
    ("AK", "Alaska"),
]

# Iterate through each state and plot
for code, name in states:
    st.subheader(f"{name} ({code})")
    data = get_co2_per_capita_data(code)
    df = pd.DataFrame({
        "Year": data["years"],
        "CO₂ per Capita": data["values"]
    })
    st.line_chart(df.set_index("Year"))
    st.markdown(
        f"**Insight:** Describe the trend for {name}, noting any significant increases or decreases over time."
    )

# Footer note
st.markdown("---")
st.caption("Data source: Placeholder historical dataset – replace with real data when available.")

# Placeholder for detailed DataFrame view (to be implemented with pandas)
st.markdown("**Detailed Data (Placeholder):**")
placeholder_df = pd.DataFrame({
    "Year": ["–"],
    "CO₂ per Capita": ["–"]
})
st.dataframe(placeholder_df)