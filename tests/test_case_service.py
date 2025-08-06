import os
import sys

# ────────────────────────────────────────────────────────────────
# Ensure the project root is on sys.path so imports work
# ────────────────────────────────────────────────────────────────
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd
import pytest

from case_service import load_merged_data, get_state_co2_series

REQUIRED_COLUMNS = ["State", "Year", "co2 per capita"]


@pytest.fixture(scope="module")
def merged_df():
    """Load the full merged dataset once for all tests."""
    return load_merged_data()


def test_load_merged_data_returns_dataframe(merged_df):
    """load_merged_data should return a pandas DataFrame with required columns."""
    assert isinstance(merged_df, pd.DataFrame)
    for col in REQUIRED_COLUMNS:
        assert col in merged_df.columns, f"Column '{col}' missing."


@pytest.mark.parametrize("state", ["WY", "ND", "AK"])
def test_get_state_co2_series_structure_and_sorting(merged_df, state):
    """
    get_state_co2_series should return a DataFrame with only the 'Year' and
    'co2 per capita' columns, sorted ascending by Year, and matching the
    number of rows in the merged data for that state.
    """
    df_series = get_state_co2_series(state)
    # It must be a DataFrame
    assert isinstance(df_series, pd.DataFrame)
    # Only these two columns
    assert list(df_series.columns) == ["Year", "co2 per capita"]
    # Row count matches
    expected = merged_df[merged_df["State"] == state]
    assert len(df_series) == len(expected)
    # Check sorting
    years = df_series["Year"].tolist()
    assert years == sorted(years), "Years are not sorted ascending"


def test_get_state_co2_series_unknown_state():
    """
    If an unknown state code is given, the result should be an empty DataFrame
    with the correct columns.
    """
    df_unknown = get_state_co2_series("ZZ")
    assert isinstance(df_unknown, pd.DataFrame)
    # Must have only Year & co2 per capita
    assert list(df_unknown.columns) == ["Year", "co2 per capita"]
    assert df_unknown.empty
