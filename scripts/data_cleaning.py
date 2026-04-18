import pandas as pd
import numpy as np

def clean_data():
    # Load raw data
    df = pd.read_csv('data/raw_sales_data.csv')
    print(f"Initial shape: {df.shape}")

    # 1. Remove Duplicates
    df.drop_duplicates(inplace=True)
    print(f"Shape after removing duplicates: {df.shape}")

    # 2. Handle Missing Values
    # Missing sales: Fill with median sales for that specific sub-category
    df['Sales'] = df.groupby('Sub-Category')['Sales'].transform(lambda x: x.fillna(x.median()))
    
    # 3. Standardize Categorical Data
    # Fix inconsistent Region names
    df['Region'] = df['Region'].str.title()
    
    # 4. Data Type Conversion
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    # 5. Feature Engineering
    # Calculate Unit Price
    df['Unit Price'] = round(df['Sales'] / df['Quantity'], 2)
    
    # Calculate Revenue (Sales * (1 - Discount))
    df['Revenue'] = round(df['Sales'] * (1 - df['Discount']), 2)
    
    # Calculate Profit Margin %
    # Avoid division by zero
    df['Profit Margin %'] = np.where(df['Revenue'] != 0, (df['Profit'] / df['Revenue']) * 100, 0)
    df['Profit Margin %'] = df['Profit Margin %'].round(2)

    # 6. Final Polish
    # Reorder columns for better readability
    cols = ['Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID',
            'Segment', 'Region', 'Category', 'Sub-Category', 'Product Name',
            'Sales', 'Quantity', 'Discount', 'Revenue', 'Profit', 'Profit Margin %']
    df = df[cols]

    # Save cleaned data
    df.to_csv('data/cleaned_sales_data.csv', index=False)
    print("Cleaned data saved to data/cleaned_sales_data.csv")
    
    # Display some stats for the report
    print("\n--- Sales Summary by Region ---")
    print(df.groupby('Region')['Revenue'].sum().sort_values(ascending=False))

if __name__ == "__main__":
    clean_data()
