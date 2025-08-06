"""
Data service module for fitting state‐specific linear regression models
and predicting CO₂ per capita using NumPy. Also provides plotting helpers.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ────────────────────────────────────────────────────────
# Module‐level cache for the merged dataset
# ────────────────────────────────────────────────────────
_cached_df = None


def load_merged_data() -> pd.DataFrame:
    """Load and cache the merged CO₂-per-capita dataset from Excel."""
    global _cached_df
    if _cached_df is None:
        path = "assets/All main data (1998 to 2023).xlsx"
        _cached_df = pd.read_excel(path, sheet_name="merged", engine="openpyxl")
    return _cached_df


# ────────────────────────────────────────────────────────
# Core regression fitting
# ────────────────────────────────────────────────────────
# List of feature column names (must match the Excel sheet exactly)
_FEATURES = [
    "renewable energy",
    "Coal Electricity Consumption",
    "Natural Gas Electricity Consumption",
    "PCE per capita",
    "Estimated Urban Population",
]

# The three case‐study state codes
_STATES = ["WY", "ND", "AK"]

# Cache for the fitted models (intercept + slopes)
_fitted_models = None


def fit_state_models() -> dict[str, dict[str, float]]:
    """
    Fit and cache OLS coefficient dictionaries for each state in _STATES.
    
    Returns:
        {
          "WY":   {"intercept": float, "renewable energy": float, ..., },
          "ND":   {...},
          "AK":   {...}
        }
    """
    global _fitted_models
    if _fitted_models is not None:
        return _fitted_models

    df = load_merged_data()
    models: dict[str, dict[str, float]] = {}

    for state in _STATES:
        # Filter data for this state and drop any rows with missing values
        df_s = df[df["State"] == state].dropna(subset=_FEATURES + ["co2 per capita"])
        
        # Design matrix X (n×(p+1)) with leading column of 1s for intercept
        X_raw = df_s[_FEATURES].values
        ones = np.ones((X_raw.shape[0], 1))
        X = np.hstack([ones, X_raw])
        
        # Response vector y
        y = df_s["co2 per capita"].values
        
        # Solve OLS via the normal equations: β = (XᵀX)⁻¹ Xᵀ y
        # We use np.linalg.lstsq for numerical stability
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        
        # Build a dict of coefficients
        coef_dict = {"intercept": float(beta[0])}
        for idx, feat in enumerate(_FEATURES, start=1):
            coef_dict[feat] = float(beta[idx])
        
        models[state] = coef_dict

    _fitted_models = models
    return models


# ────────────────────────────────────────────────────────
# Prediction API
# ────────────────────────────────────────────────────────
def predict_co2(
    state_code: str,
    renewable_energy: float,
    coal_elec: float,
    gas_elec: float,
    pce_per_capita: float,
    urban_pop: float,
) -> float:
    """
    Predict CO₂ emissions per capita for a given state and input features.

    Args:
        state_code (str): "WY", "ND", or "AK" (case-insensitive).
        renewable_energy (float): Renewable energy consumption (%).
        coal_elec (float): Coal electricity consumption.
        gas_elec (float): Natural gas electricity consumption.
        pce_per_capita (float): Personal consumption expenditure per capita.
        urban_pop (float): Estimated urban population (%).

    Returns:
        float: Predicted CO₂ per capita.
    """
    state = state_code.upper()
    models = fit_state_models()
    if state not in models:
        raise ValueError(f"Model for state {state} not found. Choose among {list(models)}.")
    
    coefs = models[state]
    # Compute intercept + Σ (slope_i × feature_i)
    pred = coefs["intercept"]
    pred += coefs["renewable energy"]                  * renewable_energy
    pred += coefs["Coal Electricity Consumption"]       * coal_elec
    pred += coefs["Natural Gas Electricity Consumption"]* gas_elec
    pred += coefs["PCE per capita"]                    * pce_per_capita
    pred += coefs["Estimated Urban Population"]        * urban_pop
    
    return float(pred)
