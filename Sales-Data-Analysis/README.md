# Sales Data Analysis Using Python and Pandas

##  Project Overview

**Sales Data Analysis** is a Python project developed as part of Week 3 of the Python learning roadmap. The project uses the Pandas library to load, clean, analyze, and summarize sales data from a CSV file.

The goal is to understand sales performance by identifying total revenue, best-selling products, regional sales, and other important business metrics.

##  Objectives

- Load sales data from a CSV file using Pandas.
- Explore the dataset's rows, columns, and data types.
- Identify missing values and duplicate records.
- Clean invalid or incomplete data.
- Calculate total revenue, average sales, highest sales, and lowest sales.
- Identify the best-selling product by quantity.
- Determine which product generates the highest revenue.
- Analyze revenue across different regions.
- Generate a formatted Markdown analysis report.

##  Technologies Used

- **Python** — Programming language
- **Pandas** — Data analysis and manipulation
- **CSV** — Data storage format
- **Markdown** — Report generation and documentation
- **Visual Studio Code** — Code editor
- **Git and GitHub** — Version control and project hosting

##  Project Structure

```text
Sales-Data-Analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── terminal_output.png
    └── analysis_report.png
```

##  Dataset Description

The project uses a sales dataset containing the following columns:

| Column | Description |
|---|---|
| `Date` | Date of the sale |
| `Product` | Name of the product sold |
| `Quantity` | Number of units sold |
| `Price` | Price per unit |
| `Customer_ID` | Customer identification number |
| `Region` | Sales region |
| `Total_Sales` | Total revenue for the record |

**Dataset size:** 20 records and 7 columns.

**Date range:** January 1, 2024, to January 20, 2024.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3 installed on your computer.
- Visual Studio Code or another Python editor.
- Basic knowledge of Python.

### Step 1: Clone the Repository

```bash
git clone https://github.com/harshadakadam74/Sales-Data-Analysis.git
```

### Step 2: Open the Project Folder

```bash
cd Sales-Data-Analysis
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Program

```bash
python sales_analysis.py
```

After successful execution, the program displays the sales analysis results in the terminal and generates the `analysis_report.md` file.

##  Analysis Process

### 1. Load Data

The Pandas `read_csv()` function loads the sales dataset.

```python
df = pd.read_csv("sales_data.csv")
```

### 2. Explore Data

The dataset is explored using the following Pandas methods:

- `head()` — Displays the first five rows.
- `shape` — Returns the number of rows and columns.
- `info()` — Displays data types and non-null counts.
- `describe()` — Provides descriptive statistics.
- `isnull().sum()` — Counts missing values.
- `duplicated().sum()` — Counts duplicate rows.

### 3. Clean Data

The cleaning process includes:

- Removing duplicate records.
- Converting date and numerical columns to appropriate data types.
- Removing rows with missing essential information.
- Excluding invalid quantities and prices.
- Recalculating total sales using quantity multiplied by price.
- Correcting inconsistent sales totals before analysis.

### 4. Analyze Sales

The program calculates important sales metrics and groups the data by product and region.

### 5. Generate Report

The program generates a Markdown report containing the main metrics, product performance, regional revenue, data-cleaning summary, and key findings.

##  Key Metrics

The project calculates:

| Metric | Description |
|---|---|
| Total Revenue | Sum of all valid sales |
| Total Units Sold | Sum of product quantities |
| Average Sale | Average revenue per valid sales record |
| Highest Sale | Largest individual sales amount |
| Lowest Sale | Smallest individual sales amount |
| Best-Selling Product | Product with the highest total quantity sold |
| Highest-Revenue Product | Product generating the most revenue |
| Highest-Revenue Region | Region generating the most revenue |

##  Sample Results

Based on the included 20-record dataset:

| Metric | Result |
|---|---:|
| Total Revenue | ₹29,15,257.00 |
| Total Units Sold | 103 |
| Number of Records | 20 |
| Average Sale | ₹1,45,762.85 |
| Highest Sale | ₹3,73,932.00 |
| Lowest Sale | ₹4,195.00 |
| Best-Selling Product | Laptop |
| Quantity of Best-Selling Product | 43 units |
| Highest-Revenue Product | Laptop |
| Highest-Revenue Region | South |
| South Region Revenue | ₹10,88,182.00 |

*Note: These results apply to the provided sample dataset.*

##  Key Findings

1. The dataset contains 20 sales records across five product categories.
2. Total revenue from the dataset is ₹29,15,257.
3. Laptop is the best-selling product by quantity, with 43 units sold.
4. Laptop also generates the highest product revenue.
5. The South region contributes the highest revenue.
6. Regional grouping helps compare sales performance across different locations.
7. Data cleaning improves the reliability of the analysis.

##  Testing and Validation

The project can be tested using the following cases:

| Test Case | Expected Result |
|---|---|
| Load a valid CSV file | Dataset loads successfully |
| Check dataset dimensions | 20 rows and 7 columns before cleaning |
| Check duplicate records | Duplicate count is displayed |
| Check missing values | Missing-value counts are displayed |
| Validate sales calculations | Total sales equal quantity multiplied by price |
| Analyze product performance | Product quantity and revenue summaries are generated |
| Analyze regional performance | Revenue is grouped by region |
| Generate the report | `analysis_report.md` is created |

### Error Handling

The program checks whether the dataset exists, validates required columns, handles invalid numeric values, and stops with a clear error if no valid sales records remain after cleaning.

##  Screenshots

Add screenshots of your own program execution to the `screenshots/` directory.

Recommended screenshots:

1. **Terminal Output:** Shows the sales metrics and product summary.

##  Future Improvements

Possible enhancements include:

- Creating bar charts and line graphs using Matplotlib.
- Creating interactive dashboards using Plotly or Streamlit.
- Analyzing monthly and weekly sales trends.
- Calculating revenue contributions by product and region.
- Exporting cleaned data to a new CSV file.
- Adding automated unit tests.
- Building an interactive sales dashboard.

## Learning Outcomes

After completing this project, I gained practical experience in:

- Python file handling.
- Pandas DataFrame operations.
- Reading and analyzing CSV files.
- Data cleaning and validation.
- Statistical calculations.
- Grouping and aggregating data.
- Generating reports programmatically.
- Organizing and documenting a GitHub project.

## Author

**Harshada Kadam**


## Conclusion

This project demonstrates how Python and Pandas can be used to analyze sales data efficiently. By loading, cleaning, grouping, and summarizing records, the program identifies important business metrics and generates a readable report.

The project provides a foundation for learning more advanced data analysis, data visualization, and data science techniques.
