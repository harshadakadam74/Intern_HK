"""
Weather Data Analysis and Visualization
Beginner-friendly end-to-end data analysis project.
Run: python main.py
"""
from pathlib import Path
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "weather_data.csv"
REPORT_DIR = ROOT / "report"
CHART_DIR = ROOT / "visualizations"

REQUIRED_COLUMNS = [
    "date", "city", "temperature_c", "humidity_pct",
    "rainfall_mm", "wind_speed_kmh", "weather_condition"
]
NUMERIC_COLUMNS = ["temperature_c", "humidity_pct", "rainfall_mm", "wind_speed_kmh"]


def load_data(path=DATA_FILE):
    """Load CSV data and validate that required columns are present."""
    if not Path(path).exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    data = pd.read_csv(path)
    missing = [col for col in REQUIRED_COLUMNS if col not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if data.empty:
        raise ValueError("Dataset is empty.")
    return data


def clean_data(data):
    """Clean dates, numeric values, invalid ranges, and missing records."""
    data = data.copy()
    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    for col in NUMERIC_COLUMNS:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    data["city"] = data["city"].astype("string").str.strip()
    data["weather_condition"] = data["weather_condition"].astype("string").str.strip()

    # Remove records without core date/city/weather values or numeric measurements.
    data = data.dropna(subset=REQUIRED_COLUMNS)
    data = data[(data["humidity_pct"] >= 0) & (data["humidity_pct"] <= 100)]
    data = data[(data["rainfall_mm"] >= 0) & (data["wind_speed_kmh"] >= 0)]
    data = data.drop_duplicates(subset=["date", "city"], keep="first")
    return data.sort_values(["date", "city"]).reset_index(drop=True)


def analyze_data(data):
    """Calculate overall metrics and useful grouped summaries."""
    if data.empty:
        raise ValueError("No valid records remain after cleaning.")
    summary = {
        "records": int(len(data)),
        "cities": int(data["city"].nunique()),
        "average_temperature_c": float(data["temperature_c"].mean()),
        "minimum_temperature_c": float(data["temperature_c"].min()),
        "maximum_temperature_c": float(data["temperature_c"].max()),
        "average_humidity_pct": float(data["humidity_pct"].mean()),
        "total_rainfall_mm": float(data["rainfall_mm"].sum()),
        "average_wind_speed_kmh": float(data["wind_speed_kmh"].mean()),
    }
    data = data.copy()
    data["month"] = data["date"].dt.to_period("M").astype(str)
    monthly = data.groupby("month", as_index=False).agg(
        average_temperature_c=("temperature_c", "mean"),
        average_humidity_pct=("humidity_pct", "mean"),
        total_rainfall_mm=("rainfall_mm", "sum"),
        record_count=("date", "count"),
    )
    city_summary = data.groupby("city", as_index=False).agg(
        average_temperature_c=("temperature_c", "mean"),
        average_humidity_pct=("humidity_pct", "mean"),
        total_rainfall_mm=("rainfall_mm", "sum"),
        average_wind_speed_kmh=("wind_speed_kmh", "mean"),
    )
    condition_summary = data["weather_condition"].value_counts().rename_axis("weather_condition").reset_index(name="days")
    return summary, monthly, city_summary, condition_summary


def create_visualizations(data, monthly, city_summary, condition_summary):
    """Create three clear charts and save them to visualizations/."""
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["month"], monthly["average_temperature_c"], marker="o", linewidth=2)
    plt.title("Average Temperature by Month")
    plt.xlabel("Month")
    plt.ylabel("Average temperature (°C)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "monthly_temperature_trend.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    ordered = city_summary.sort_values("average_temperature_c", ascending=False)
    plt.bar(ordered["city"], ordered["average_temperature_c"])
    plt.title("Average Temperature by City")
    plt.xlabel("City")
    plt.ylabel("Average temperature (°C)")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "average_temperature_by_city.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 7))
    plt.pie(condition_summary["days"], labels=condition_summary["weather_condition"],
            autopct="%1.1f%%", startangle=90)
    plt.title("Weather Condition Distribution")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "weather_condition_distribution.png", dpi=150)
    plt.close()


def write_report(data, summary, monthly, city_summary, condition_summary):
    """Save summary tables and a readable Markdown report."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    cleaned_path = REPORT_DIR / "cleaned_weather_data.csv"
    data.to_csv(cleaned_path, index=False)
    monthly.to_csv(REPORT_DIR / "monthly_weather_summary.csv", index=False)
    city_summary.to_csv(REPORT_DIR / "city_weather_summary.csv", index=False)
    condition_summary.to_csv(REPORT_DIR / "weather_condition_summary.csv", index=False)

    warmest_city = city_summary.loc[city_summary["average_temperature_c"].idxmax()]
    coolest_city = city_summary.loc[city_summary["average_temperature_c"].idxmin()]
    wettest_city = city_summary.loc[city_summary["total_rainfall_mm"].idxmax()]
    most_common_condition = condition_summary.iloc[0]

    lines = [
        "# Weather Data Analysis Report", "",
        "## 1. Project Overview",
        "This project uses Python, Pandas, and Matplotlib to clean, analyze, and visualize weather observations across multiple cities.", "",
        "## 2. Dataset Summary",
        f"- Valid records after cleaning: {summary['records']}",
        f"- Cities covered: {summary['cities']}",
        f"- Date range: {data['date'].min().date()} to {data['date'].max().date()}",
        "- Measurements: temperature, humidity, rainfall, wind speed, and weather condition", "",
        "## 3. Key Metrics",
        f"- Average temperature: {summary['average_temperature_c']:.2f} °C",
        f"- Minimum temperature: {summary['minimum_temperature_c']:.2f} °C",
        f"- Maximum temperature: {summary['maximum_temperature_c']:.2f} °C",
        f"- Average humidity: {summary['average_humidity_pct']:.2f}%",
        f"- Total recorded rainfall: {summary['total_rainfall_mm']:.2f} mm",
        f"- Average wind speed: {summary['average_wind_speed_kmh']:.2f} km/h", "",
        "## 4. Insights",
        f"- Warmest city by average temperature in this dataset: **{warmest_city['city']}** ({warmest_city['average_temperature_c']:.2f} °C).",
        f"- Coolest city by average temperature in this dataset: **{coolest_city['city']}** ({coolest_city['average_temperature_c']:.2f} °C).",
        f"- Highest accumulated rainfall: **{wettest_city['city']}** ({wettest_city['total_rainfall_mm']:.2f} mm).",
        f"- Most frequently recorded condition: **{most_common_condition['weather_condition']}** ({int(most_common_condition['days'])} records).",
        "- The monthly temperature chart helps show changes across the observation period.",
        "- These are insights from the included synthetic practice dataset, not a live weather forecast.", "",
        "## 5. Visualizations",
        "- `visualizations/monthly_temperature_trend.png` — line chart",
        "- `visualizations/average_temperature_by_city.png` — bar chart",
        "- `visualizations/weather_condition_distribution.png` — pie chart", "",
        "## 6. Methodology",
        "1. Load the CSV and validate required columns.",
        "2. Convert dates and numeric measurements to suitable data types.",
        "3. Remove incomplete, duplicate, and invalid records.",
        "4. Calculate overall metrics and group summaries.",
        "5. Generate charts and export report files.", "",
        "## 7. Limitations",
        "The included data is synthetic and intended for learning. It should not be used for safety decisions or real weather forecasting.", "",
        "## 8. Conclusion",
        "This project demonstrates an end-to-end beginner data analysis workflow, including validation, cleaning, descriptive statistics, visualization, and written insights.", ""
    ]
    (REPORT_DIR / "analysis_report.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    try:
        raw_data = load_data()
        cleaned = clean_data(raw_data)
        summary, monthly, city_summary, condition_summary = analyze_data(cleaned)
        create_visualizations(cleaned, monthly, city_summary, condition_summary)
        write_report(cleaned, summary, monthly, city_summary, condition_summary)
        print("Weather Data Analysis completed successfully.")
        print(f"Records analyzed: {summary['records']}")
        print(f"Cities covered: {summary['cities']}")
        print(f"Average temperature: {summary['average_temperature_c']:.2f} °C")
        print(f"Total rainfall: {summary['total_rainfall_mm']:.2f} mm")
        print(f"Charts saved in: {CHART_DIR}")
        print(f"Report saved in: {REPORT_DIR / 'analysis_report.md'}")
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
