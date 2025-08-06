import pandas as pd
import numpy as np

# Placeholder model loading
def load_model(path: str):
    """
    Placeholder loader. Returns dummy model object.
    Replace with `joblib.load(path)` in production.
    """
    return {"model": "dummy"}


def predict_co2(model, input_df: pd.DataFrame) -> float:
    """
    Placeholder prediction logic.
    Calculates a dummy CO₂ per capita based on input features.
    """
    # Extract features
    coal = float(input_df.loc[0, "Coal Production"])
    gas = float(input_df.loc[0, "Natural Gas Production"])
    income = float(input_df.loc[0, "Per Capita Income"])
    urban = float(input_df.loc[0, "Urban Population %"])
    renew = float(input_df.loc[0, "Renewable Energy %"])
    # Dummy formula: weighted sum
    value = (
        0.02 * coal +
        0.015 * gas +
        0.0001 * income +
        0.03 * urban -
        0.025 * renew
    )
    # Ensure non-negative
    return max(value, 0.0)


def get_co2_per_capita_data(state_code: str) -> dict:
    """
    Placeholder historical data generator.
    Returns a linear trend with slight variation per state.
    """
    years = list(range(1990, 2021))
    offset = {"WY": 1.0, "ND": 1.5, "AK": 2.0}.get(state_code, 0.5)
    values = [offset + (i * 0.05) for i in range(len(years))]
    return {"years": years, "values": values}
