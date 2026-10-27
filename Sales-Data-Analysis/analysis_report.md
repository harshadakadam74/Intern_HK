# Sales Data Analysis Report

## 1. Project Overview

This project analyzes sales data using Python and Pandas.
The objective is to identify sales trends, product performance,
and regional revenue.

## 2. Dataset Summary

- Number of records after cleaning: 20
- Number of columns: 7
- Total units sold: 103
- Date range: 2024-01-01 to 2024-01-20

## 3. Key Metrics

| Metric | Result |
|---|---:|
| Total Revenue | Rs. 2,915,257.00 |
| Total Units Sold | 103 |
| Average Sale | Rs. 145,762.85 |
| Highest Sale | Rs. 373,932.00 |
| Lowest Sale | Rs. 16,780.00 |
| Sales Value Mismatches Corrected | 0 |

## 4. Product Analysis

- Best-selling product by quantity: Laptop
- Units sold for the best-selling product: 43
- Highest-revenue product: Laptop

| Product    |   Units_Sold |   Revenue |
|:-----------|-------------:|----------:|
| Laptop     |           43 |   1530408 |
| Phone      |           33 |    937670 |
| Headphones |           11 |    178193 |
| Tablet     |            8 |    219706 |
| Monitor    |            8 |     49280 |

## 5. Regional Analysis

- Highest-revenue region: South
- Revenue from that region: Rs. 1,088,182.00

| Region   |   Revenue |
|:---------|----------:|
| South    |   1088182 |
| North    |    889957 |
| East     |    474015 |
| West     |    463103 |

## 6. Data Cleaning

- Removed duplicate records.
- Converted dates and numerical fields to appropriate types.
- Removed rows with missing essential fields.
- Excluded invalid quantities and prices.
- Recalculated sales as Quantity multiplied by Price.

## 7. Key Findings

1. Total revenue was Rs. 2,915,257.00.
2. Laptop was the best-selling product by quantity.
3. Laptop generated the highest product revenue.
4. South was the highest-revenue region.

## 8. Tools and Technologies

- Python
- Pandas
- CSV
- Markdown

## 9. Testing and Validation

The following checks were performed during the analysis:

- Verified that the dataset contains 20 records and 7 columns.
- Checked for missing values and duplicate records.
- Converted date and numerical columns to appropriate data types.
- Validated sales amounts using quantity multiplied by price.
- Calculated total revenue, average sale, highest sale, and lowest sale.
- Grouped sales by product and region.
- Generated the Markdown report successfully.

### Validation Results

| Test | Expected Result | Status |
|---|---|---|
| Dataset loading | 20 records loaded | Passed |
| Total revenue calculation | Rs. 2,915,257.00 | Passed |
| Total units calculation | 103 units | Passed |
| Sales value validation | 0 mismatches | Passed |
| Best-selling product | Laptop | Passed |
| Highest-revenue region | South | Passed |
| Report generation | Markdown file created | Passed |

## 10. Future Improvements

- Create sales charts using Matplotlib.
- Analyze monthly and regional sales trends.
- Build an interactive dashboard using Streamlit.
- Add automated tests for data validation.
- Export cleaned data to a separate CSV file.

## 11. Conclusion

This project demonstrates how Pandas can be used to clean,
summarize, and analyze real-world sales data.
