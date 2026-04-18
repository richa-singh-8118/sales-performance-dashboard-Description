-- Database: sales_db
CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

-- Table structure for cleaned sales data
CREATE TABLE IF NOT EXISTS sales_data (
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    segment VARCHAR(50),
    region VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(10, 2),
    quantity INT,
    discount DECIMAL(4, 2),
    revenue DECIMAL(10, 2),
    profit DECIMAL(10, 2),
    profit_margin_pct DECIMAL(5, 2)
);

-- Note: In a production environment, we would use a Star Schema (Dimensions and Fact tables)
-- for better performance. For this project, a flat table is used for simplified BI integration.
