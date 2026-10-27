
"""
Project: Sales Data Analysis
Week 3 - Introduction to Data Analysis

Description:
Analyze sales records using Pandas, clean the data,
calculate sales metrics, and generate a Markdown report.
"""

from pathlib import Path
import pandas as pd

# --------------------------------------------------
# 1. File paths and required columns
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
REPORT_FILE = BASE_DIR / "analysis_report.md"

REQUIRED_COLUMNS = [
    "Date",
    "Product",
    "Quantity",
    "Price",
    "Customer_ID",
    "Region",
    "Total_Sales",
]


# --------------------------------------------------
# 2. Load the dataset
# --------------------------------------------------

def load_data():
    """Load CSV data and check required columns."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "sales_data.csv was not found."
        )

    df = pd.read_csv(DATA_FILE)

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    print("\nDATA LOADED SUCCESSFULLY")
    print("-" * 45)
    print(df.head())

    return df


# --------------------------------------------------
# 3. Explore the dataset
# --------------------------------------------------

def explore_data(df):
    """Display dataset structure and quality."""

    print("\nDATASET OVERVIEW")
    print("-" * 45)
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(f"Column names: {df.columns.tolist()}")

    print("\nData types and non-null counts:")
    df.info()

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate records:", df.duplicated().sum())

    print("\nNumerical statistics:")
    print(df.describe())


# --------------------------------------------------
# 4. Clean the data
# --------------------------------------------------

def clean_data(df):
    """Remove duplicate and invalid records."""

    df = df.copy()
    original_rows = len(df)

    # Remove duplicate records.
    df = df.drop_duplicates()

    # Convert the date column to datetime.
    df["Date"] = pd.to_datetime(
        df["Date"], errors="coerce"
    )

    # Convert numeric columns to numeric types.
    numeric_columns = [
        "Quantity", "Price", "Total_Sales"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col], errors="coerce"
        )

    # Remove rows missing essential information.
    required_values = [
        "Date", "Product", "Quantity",
        "Price", "Customer_ID", "Region",
    ]

    df = df.dropna(subset=required_values)

    # Remove blank product, customer, and region values.
    for col in ["Product", "Customer_ID", "Region"]:
        df = df[
            df[col].astype(str).str.strip().ne("")
        ]

    # Keep only positive quantities and prices.
    df = df[
        (df["Quantity"] > 0)
        & (df["Price"] > 0)
    ]

    # Calculate the correct sales amount.
    df["Calculated_Sales"] = (
        df["Quantity"] * df["Price"]
    )

    # Compare the supplied sales value with the
    # calculated value before replacing it.
    df["Sales_Mismatch"] = (
        df["Total_Sales"].isna()
        | (
            (df["Total_Sales"] - df["Calculated_Sales"])
            .abs() > 0.01
        )
    )

    mismatch_count = int(df["Sales_Mismatch"].sum())

    # Use the calculated value for reliable analysis.
    df["Total_Sales"] = df["Calculated_Sales"]

    # Remove helper columns from final dataset.
    df = df.drop(
        columns=["Calculated_Sales", "Sales_Mismatch"]
    )

    df = df.reset_index(drop=True)

    print("\nDATA CLEANING SUMMARY")
    print("-" * 45)
    print(f"Original rows: {original_rows}")
    print(f"Cleaned rows: {len(df)}")
    print(f"Rows removed: {original_rows - len(df)}")
    print(f"Sales mismatches corrected: {mismatch_count}")
    print("\nRemaining missing values:")
    print(df.isnull().sum())

    return df, mismatch_count


# --------------------------------------------------
# 5. Analyze sales
# --------------------------------------------------

def analyze_sales(df):
    """Calculate sales metrics and product summaries."""

    if df.empty:
        raise ValueError(
            "No valid sales records remain after cleaning."
        )

    total_revenue = df["Total_Sales"].sum()
    total_units = df["Quantity"].sum()
    average_sale = df["Total_Sales"].mean()

    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()

    # Summarize units and revenue for each product.
    product_summary = (
        df.groupby("Product")
        .agg(
            Units_Sold=("Quantity", "sum"),
            Revenue=("Total_Sales", "sum"),
        )
        .sort_values(
            ["Units_Sold", "Revenue"],
            ascending=False,
        )
    )

    # Identify the product with the most units sold.
    best_selling_product = product_summary.index[0]

    # Identify the product generating the most revenue.
    highest_revenue_product = (
        product_summary["Revenue"].idxmax()
    )

    # Summarize revenue by region.
    region_summary = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    # Calculate daily revenue.
    daily_sales = (
        df.groupby("Date")["Total_Sales"]
        .sum()
        .sort_index()
    )

    metrics = {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "average_sale": average_sale,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "best_selling_product": best_selling_product,
        "best_selling_units": product_summary.iloc[0]["Units_Sold"],
        "highest_revenue_product": highest_revenue_product,
        "highest_revenue_region": region_summary.idxmax(),
        "highest_region_revenue": region_summary.max(),
        "product_summary": product_summary,
        "region_summary": region_summary,
        "daily_sales": daily_sales,
    }

    return metrics


# --------------------------------------------------
# 6. Display the results
# --------------------------------------------------

def display_results(metrics):
    """Print a formatted sales analysis."""

    print("\nSALES ANALYSIS REPORT")
    print("=" * 45)

    print(
        f"Total Revenue: "
        f"Rs. {metrics['total_revenue']:,.2f}"
    )
    print(f"Total Units Sold: {metrics['total_units']:,.0f}")
    print(
        f"Average Sale: "
        f"Rs. {metrics['average_sale']:,.2f}"
    )
    print(
        f"Highest Sale: "
        f"Rs. {metrics['highest_sale']:,.2f}"
    )
    print(
        f"Lowest Sale: "
        f"Rs. {metrics['lowest_sale']:,.2f}"
    )

    print(
        f"\nBest-Selling Product: "
        f"{metrics['best_selling_product']}"
    )
    print(
        f"Units Sold: "
        f"{metrics['best_selling_units']:,.0f}"
    )
    print(
        f"Highest-Revenue Product: "
        f"{metrics['highest_revenue_product']}"
    )
    print(
        f"Top Region: "
        f"{metrics['highest_revenue_region']}"
    )

    print("\nPRODUCT SUMMARY")
    print(metrics["product_summary"].to_string())

    print("\nREGIONAL REVENUE")
    print(metrics["region_summary"].to_string())


# --------------------------------------------------
# 7. Generate the Markdown report
# --------------------------------------------------

def generate_report(df, metrics, mismatch_count):
    """Save the analysis findings to a Markdown file."""

    product_table = metrics["product_summary"].to_markdown()
    region_table = metrics["region_summary"].to_frame(
        name="Revenue"
    ).to_markdown()

    report = f"""# Sales Data Analysis Report

## 1. Project Overview

This project analyzes sales data using Python and Pandas.
The objective is to identify sales trends, product performance,
and regional revenue.

## 2. Dataset Summary

- Number of records after cleaning: {len(df)}
- Number of columns: {len(REQUIRED_COLUMNS)}
- Total units sold: {metrics['total_units']:,.0f}
- Date range: {df['Date'].min().date()} to {df['Date'].max().date()}

## 3. Key Metrics

| Metric | Result |
|---|---:|
| Total Revenue | Rs. {metrics['total_revenue']:,.2f} |
| Total Units Sold | {metrics['total_units']:,.0f} |
| Average Sale | Rs. {metrics['average_sale']:,.2f} |
| Highest Sale | Rs. {metrics['highest_sale']:,.2f} |
| Lowest Sale | Rs. {metrics['lowest_sale']:,.2f} |
| Sales Value Mismatches Corrected | {mismatch_count} |

## 4. Product Analysis

- Best-selling product by quantity: {metrics['best_selling_product']}
- Units sold for the best-selling product: {metrics['best_selling_units']:,.0f}
- Highest-revenue product: {metrics['highest_revenue_product']}

{product_table}

## 5. Regional Analysis

- Highest-revenue region: {metrics['highest_revenue_region']}
- Revenue from that region: Rs. {metrics['highest_region_revenue']:,.2f}

{region_table}

## 6. Data Cleaning

- Removed duplicate records.
- Converted dates and numerical fields to appropriate types.
- Removed rows with missing essential fields.
- Excluded invalid quantities and prices.
- Recalculated sales as Quantity multiplied by Price.

## 7. Key Findings

1. Total revenue was Rs. {metrics['total_revenue']:,.2f}.
2. {metrics['best_selling_product']} was the best-selling product by quantity.
3. {metrics['highest_revenue_product']} generated the highest product revenue.
4. {metrics['highest_revenue_region']} was the highest-revenue region.

## 8. Tools and Technologies

- Python
- Pandas
- CSV
- Markdown

## 9. Conclusion

This project demonstrates how Pandas can be used to clean,
summarize, and analyze real-world sales data.
"""

    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"\nReport generated: {REPORT_FILE}")


# --------------------------------------------------
# 8. Main program
# --------------------------------------------------

def main():
    """Execute all analysis steps."""

    df = load_data()

    explore_data(df)

    cleaned_df, mismatch_count = clean_data(df)

    metrics = analyze_sales(cleaned_df)

    display_results(metrics)

    generate_report(
        cleaned_df, metrics, mismatch_count
    )


if __name__ == "__main__":
    main()
