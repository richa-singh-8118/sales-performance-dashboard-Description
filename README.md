# Sales Performance Dashboard - Business Intelligence Project

[![Tech Stack](https://img.shields.io/badge/Tech%20Stack-Python%20|%20SQL%20|%20Power%20BI%20|%20Excel-blue)](https://github.com/)

## 📌 Project Overview
This project is a comprehensive Business Intelligence (BI) solution designed to analyze sales performance for a global retail corporation. It covers the entire data lifecycle: from synthetic data generation and automated cleaning to SQL-based KPI generation and interactive Power BI visualization.

**🚀 Live Demo:** [Deploying to Streamlit Cloud...](#-how-to-deploy-live) (See instructions below to get your own public link!)

The goal is to provide management with actionable insights into revenue trends, regional performance, and product profitability to drive data-driven decision-making.

---

## 🛠️ Tech Stack & Tools
- **Data Engineering**: Python (Pandas, NumPy)
- **Database**: MySQL (Optimized SQL Queries)
- **Visualization**: Power BI (DAX, Interactive Dashboards)
- **Environment**: VS Code, MySQL Workbench

---

## 🚀 Key Features

### 1. Data Pipeline (Python)
- **Synthetic Data Generation**: Created a realistic dataset of 6,000+ records with seasonality and regional variations.
- **Automated Cleaning**: Developed a Python script to handle missing values, duplicates, and inconsistent categorical data.
- **Feature Engineering**: Calculated key metrics like `Revenue`, `Profit Margin`, and `Unit Price` during preprocessing.

### 2. SQL Analytics
- Integrated cleaned data into a MySQL database.
- Authored complex SQL queries for:
  - Monthly Growth Rates (YoY/MoM)
  - Regional Revenue Contribution
  - Customer Segmentation (RFM-lite)
  - Top 10 High-Performing Products

### 3. Power BI Interactive Dashboard
- **Executive Summary**: High-level KPI cards (Revenue, Profit, Orders, Margin %).
- **Regional Performance**: Bubble maps and bar charts for geographical analysis.
- **Trend Analysis**: Interactive time-series charts with drill-down capabilities.
- **Product Insights**: Breakdown of sales by Category and Sub-category.
- **Dynamic Filters**: Slice data by Region, Segment, and Time Period.

---

## 📁 Project Structure
```bash
├── data/
│   ├── raw_sales_data.csv       # Original dataset with noise
│   └── cleaned_sales_data.csv   # Preprocessed data for BI
├── scripts/
│   ├── generate_data.py         # Synthetic data generation script
│   └── data_cleaning.py         # Pandas cleaning pipeline
├── sql/
│   ├── database_setup.sql       # Schema definition
│   └── queries.sql              # Analytical KPI queries
├── docs/
│   ├── dax_measures.md          # DAX formulas & Design specs
│   └── business_insights.md     # Strategic recommendations
└── README.md                    # Project documentation
```

---

## 📈 Business Insights (Summary)
- **Top Region**: Asia-Pacific accounts for the highest revenue share (~21%).
- **Seasonality**: Peak sales occur in Q4 (Nov-Dec), driven by Electronics.
- **Profitability**: High discounts in the Electronics category are impacting overall margins; a revised pricing strategy is recommended.
- **Customer Base**: 50% of the revenue is driven by the Consumer segment, but Corporate clients show higher average order values.

---

## 🎯 Impact & Future Scope
- **Impact**: Provides a real-time view of business health, identifying underperforming regions and high-growth products.
- **Future Work**: 
  - Integrate a Machine Learning model for **Sales Forecasting**.
  - Automate data ingestion using an ETL pipeline (Airflow).
  - Implement Row-Level Security (RLS) in Power BI for regional managers.

---

## 👨‍💻 How to Use
1. Clone the repository.
2. Run `python scripts/generate_data.py` to create the raw dataset.
3. Run `python scripts/data_cleaning.py` to preprocess the data.
4. Import `cleaned_sales_data.csv` into MySQL and execute `sql/queries.sql`.
5. Connect `cleaned_sales_data.csv` to Power BI and apply the DAX measures from `docs/dax_measures.md`.

---

## 🌐 How to Deploy Live (Streamlit Cloud)
To get a public "Deploy Link" for your resume, follow these 3 simple steps:
1. Go to [share.streamlit.io](https://share.streamlit.io/).
2. Connect your GitHub account and select this repository.
3. Set the Main file path to: `scripts/dashboard_app.py`.
4. Click **Deploy**! You will get a custom URL like `https://your-dashboard.streamlit.app`.
