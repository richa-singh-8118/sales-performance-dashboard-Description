import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sales_data(num_records=5000):
    # Setup seed for reproducibility
    np.random.seed(42)
    random.seed(42)

    # Base data lists
    regions = ['North America', 'Europe', 'Asia-Pacific', 'LATAM', 'EMEA']
    categories = {
        'Electronics': ['Laptops', 'Smartphones', 'Tablets', 'Monitors', 'Accessories'],
        'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Sofas', 'Office Desks'],
        'Office Supplies': ['Paper', 'Binders', 'Pens', 'Storage', 'Art Supplies']
    }
    ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
    segments = ['Consumer', 'Corporate', 'Home Office']

    data = []

    start_date = datetime(2022, 1, 1)
    
    for i in range(num_records):
        order_id = f"CA-{2022 + random.randint(0, 2)}-{100000 + i}"
        # Incorporate seasonality: more orders in Nov/Dec
        day_offset = random.randint(0, 1000)
        order_date = start_date + timedelta(days=day_offset)
        
        # Bias towards end of year
        if order_date.month in [11, 12]:
            if random.random() > 0.3: # Increase density in Q4
                order_date = order_date
        
        ship_date = order_date + timedelta(days=random.randint(1, 7))
        ship_mode = random.choice(ship_modes)
        customer_id = f"CU-{1000 + random.randint(0, 500)}"
        segment = random.choice(segments)
        region = random.choice(regions)
        
        category = random.choice(list(categories.keys()))
        sub_category = random.choice(categories[category])
        product_name = f"{sub_category} Model {random.randint(1, 100)}"
        
        # Pricing logic
        if category == 'Electronics':
            sales = round(random.uniform(200, 2000), 2)
        elif category == 'Furniture':
            sales = round(random.uniform(100, 1500), 2)
        else:
            sales = round(random.uniform(5, 300), 2)
            
        quantity = random.randint(1, 10)
        discount = random.choice([0, 0, 0, 0.1, 0.2, 0.5]) # 50% discount occasionally
        
        # Profit calculation (simplified)
        cost_multiplier = random.uniform(0.5, 0.8)
        profit = round((sales * (1 - discount)) - (sales * cost_multiplier), 2)
        
        # Introduce "Dirty Data"
        if i % 100 == 0: # Null values
            sales = np.nan
        if i % 150 == 0: # Duplicates (will handle later by adding same record)
            pass 
        if i % 200 == 0: # Inconsistent naming
            region = region.lower()
            
        data.append([
            order_id, order_date, ship_date, ship_mode, customer_id, 
            segment, region, category, sub_category, product_name,
            sales, quantity, discount, profit
        ])

    # Add some duplicates
    duplicate_indices = random.sample(range(len(data)), 50)
    for idx in duplicate_indices:
        data.append(data[idx])

    columns = [
        'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID',
        'Segment', 'Region', 'Category', 'Sub-Category', 'Product Name',
        'Sales', 'Quantity', 'Discount', 'Profit'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    
    # Save to CSV
    df.to_csv('data/raw_sales_data.csv', index=False)
    print(f"Generated {len(df)} records in data/raw_sales_data.csv")

if __name__ == "__main__":
    generate_sales_data(6000)
