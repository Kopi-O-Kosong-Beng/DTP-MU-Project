import streamlit as st
from case_service import get_state_co2_series, load_merged_data

# ─── Page configuration ────────────────────────────────────────────────────────
# Set the browser tab title and choose a wide layout so charts span the width.
st.set_page_config(page_title="Case Studies", layout="wide")

# ─── Page header ───────────────────────────────────────────────────────────────
st.title("Case Studies: WY, ND & AK")
st.markdown(
    """
    We pivoted to a targeted case-study approach by selecting the top three CO₂ per-capita
    emitters (Wyoming, North Dakota, Alaska)—to yield state-specific insights within
    our course scope.
    """
)

# ─── Loop over the three states and render each section ────────────────────────
for code, name in [("WY", "Wyoming"), ("ND", "North Dakota"), ("AK", "Alaska")]:
    # Sub‐section header for the state
    st.subheader(f"{name} ({code})")
    
    # Fetch time series and rename the emission column for clarity
    df_series = get_state_co2_series(code).rename(columns={"co2 per capita": "CO₂"})
    # Plot the historical CO₂ per capita as a line chart
    st.line_chart(df_series.set_index("Year"))
    
    # Add narrative text that explains the drivers behind each state’s ranking
    if code == "WY":
        st.markdown(
            """
            **Wyoming** ranks **1st** in CO₂ per capita nationwide. This high intensity stems
            from its enormous coal reserves and coal-fired power plants—among the largest
            generators of coal electricity in the U.S.—coupled with a small population base.
            In 2023, over **80%** of its in-state electricity came from coal combustion,
            yielding one of the largest per-person emissions footprints in the country.
            """
        )
    elif code == "ND":
        st.markdown(
            """
            **North Dakota** places **2nd**, driven primarily by its booming oil and natural
            gas sector. Hydraulic fracturing and associated gas flaring in the Bakken region
            release substantial CO₂, while its low population dilutes total state emissions
            across fewer residents.
            """
        )
    else:  # AK
        st.markdown(
            """
            **Alaska** is **3rd**, reflecting high energy needs for heating in an Arctic climate
            and the energy intensity of transporting oil and gas off-shore. Despite growing
            renewable installations, per-capita use of diesel and natural gas for electricity
            and heating remains elevated in rural and urban communities alike.
            """
        )

# ─── Optional raw data preview ─────────────────────────────────────────────────
# Give users the option to inspect the underlying numbers
if st.checkbox("Show raw data preview for WY, ND & AK"):
    df = load_merged_data()  # load full dataset
    df_subset = df[df["State"].isin(["WY", "ND", "AK"])]
    df_display = (
        df_subset[["State", "Year", "co2 per capita"]]
        .sort_values(["State", "Year"])
        .reset_index(drop=True)
    )
    st.dataframe(df_display)  # interactive table

# ─── Data sources ─────────────────────────────────────────────────────────────
st.markdown(
    """
    **Sources:**
    1. U.S. Energy Information Administration (EIA). State Energy Data System, 2023.  
    2. U.S. Environmental Protection Agency (EPA). Greenhouse Gas Inventory Data, 2022.  
    3. National Oceanic and Atmospheric Administration (NOAA). Arctic Climatology, 2023. 
    """
)
