# Weather Data Analysis and Visualization

## Project overview
A beginner-friendly Python project that loads, validates, cleans, analyzes, and visualizes weather observations across multiple cities.

## Objectives
- Analyze temperature, humidity, rainfall, wind speed, and weather conditions.
- Create at least two chart types (line, bar, and pie charts are included).
- Produce a report with metrics and written insights.
- Demonstrate input validation and error handling.

## Technology
Python, Pandas, NumPy, Matplotlib, CSV, pytest, Git/GitHub.

## Folder structure
```text
weather_data_analysis/
├── data/weather_data.csv
├── visualizations/
├── report/
├── tests/test_analysis.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup on Windows
1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it in PowerShell:
   `.venv\Scripts\Activate.ps1`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Run the analysis:
   `python main.py`
7. Run tests:
   `pytest -q`

## Outputs
- `visualizations/monthly_temperature_trend.png`
- `visualizations/average_temperature_by_city.png`
- `visualizations/weather_condition_distribution.png`
- `report/analysis_report.md`
- Cleaned dataset and summary CSV files in `report/`

## Dataset dictionary
- `date`: observation date
- `city`: city name
- `temperature_c`: temperature in Celsius
- `humidity_pct`: relative humidity percentage (0-100)
- `rainfall_mm`: rainfall in millimetres
- `wind_speed_kmh`: wind speed in kilometres per hour
- `weather_condition`: categorical weather label

## Data note
The included 100-row dataset is synthetic practice data. It is not live weather data and must not be used for forecasting or safety decisions. Replace it with a real dataset if your instructor supplied one.

## Methodology
1. Load CSV and validate columns.
2. Parse dates and numeric columns.
3. Drop incomplete rows, invalid humidity/rainfall/wind values, and duplicate city-date records.
4. Calculate summary metrics and grouped tables.
5. Save visualizations and a Markdown report.

## Testing evidence
Tests cover successful loading, invalid/missing-column validation, and basic data cleaning. Run `pytest -q` and include the terminal output screenshot in your submission.

