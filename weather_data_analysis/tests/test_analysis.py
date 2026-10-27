import sys
from pathlib import Path
import pandas as pd
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import load_data, clean_data, analyze_data, REQUIRED_COLUMNS


def test_load_data_has_required_columns():
    data = load_data()
    assert all(column in data.columns for column in REQUIRED_COLUMNS)
    assert len(data) > 0


def test_missing_column_raises_value_error(tmp_path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"date": ["2025-01-01"], "city": ["Pune"]}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="Missing required columns"):
        load_data(path)


def test_cleaning_removes_invalid_humidity_and_duplicates():
    sample = pd.DataFrame({
        "date": ["2025-01-01", "2025-01-01", "2025-01-02"],
        "city": ["Pune", "Pune", "Mumbai"],
        "temperature_c": [25, 27, 30],
        "humidity_pct": [50, 50, 140],
        "rainfall_mm": [0, 0, 2],
        "wind_speed_kmh": [10, 10, 12],
        "weather_condition": ["Clear", "Clear", "Hot"],
    })
    cleaned = clean_data(sample)
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["city"] == "Pune"


def test_analysis_summary_has_expected_keys():
    cleaned = clean_data(load_data())
    summary, monthly, city_summary, conditions = analyze_data(cleaned)
    assert summary["records"] == len(cleaned)
    assert summary["cities"] >= 1
    assert not monthly.empty
    assert not city_summary.empty
    assert not conditions.empty
