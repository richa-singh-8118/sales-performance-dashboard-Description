# Power BI DAX Measures & Data Modeling

This document contains the core DAX formulas used in the Sales Performance Dashboard.

## Core KPI Measures

### 1. Total Revenue
```dax
Total Revenue = SUM('sales_data'[Revenue])
```

### 2. Total Profit
```dax
Total Profit = SUM('sales_data'[Profit])
```

### 3. Total Orders
```dax
Total Orders = DISTINCTCOUNT('sales_data'[Order ID])
```

### 4. Profit Margin %
```dax
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
```

## Advanced Time Intelligence

### 5. Sales Year-over-Year (YoY) Growth
```dax
Sales LY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date]))
YoY Growth % = DIVIDE([Total Revenue] - [Sales LY], [Sales LY], 0)
```

### 6. Rolling 3-Month Revenue
```dax
Rolling 3M Revenue = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -3, MONTH)
)
```

## Performance Ranking

### 7. Product Rank by Profit
```dax
Product Rank = RANKX(ALL('sales_data'[Product Name]), [Total Profit], , DESC)
```

## Dashboard Layout Guidelines
- **KPI Cards**: Place Revenue, Profit, Margin %, and YoY Growth at the top.
- **Slicers**: Add slicers for `Region`, `Category`, and `Order Date` (Year/Month).
- **Trend Chart**: Use an Area Chart for `Total Revenue` and `Total Profit` over `Order Date`.
- **Regional Map**: Use a Bubble Map with `Region` as location and `Total Revenue` as bubble size.
- **Top Products**: Use a Bar Chart for the Top 10 Products by Profit.
