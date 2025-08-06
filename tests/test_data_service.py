import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

import pandas as pd
from matplotlib.figure import Figure

from data_service import (
    load_merged_data,
    fit_state_models,
    predict_co2,
)

# List of all feature columns we expect in the Excel
EXPECTED_FEATURES = [
    "renewable energy",
    "Coal Electricity Consumption",
    "Natural Gas Electricity Consumption",
    "PCE per capita",
    "Estimated Urban Population",
]


def test_load_merged_data_returns_dataframe_with_required_columns():
    """
    load_merged_data() should return a pandas DataFrame containing
    the key columns for both case studies and prediction.
    """
    df = load_merged_data()
    # It must be a DataFrame
    assert isinstance(df, pd.DataFrame)
    # Check for core columns
    for col in ["State", "Year", "co2 per capita"] + EXPECTED_FEATURES:
        assert col in df.columns, f"Missing column: {col}"


def test_fit_state_models_structure_and_types():
    """
    fit_state_models() should return a dict with keys 'WY','ND','AK',
    each mapping to a dict of float coefficients including 'intercept'.
    """
    models = fit_state_models()
    # Must have exactly our three case studies
    assert set(models.keys()) == {"WY", "ND", "AK"}

    for state, coefs in models.items():
        # Each state must have an 'intercept'
        assert "intercept" in coefs
        assert isinstance(coefs["intercept"], float)

        # And each feature must appear as a float
        for feat in EXPECTED_FEATURES:
            assert feat in coefs, f"{feat} missing in {state} model"
            assert isinstance(coefs[feat], float)


@pytest.mark.parametrize("state", ["WY", "ND", "AK"])
def test_predict_co2_at_zero_equals_intercept(state):
    """
    If all inputs are zero, predict_co2() should return the intercept
    term from the fitted model for that state.
    """
    models = fit_state_models()
    intercept = models[state]["intercept"]

    # Zero out all feature inputs
    pred = predict_co2(state, 0, 0, 0, 0, 0)
    assert pytest.approx(intercept, rel=1e-6) == pred

