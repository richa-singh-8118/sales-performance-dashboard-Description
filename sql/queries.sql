-- 1. Total Revenue and Profit
SELECT 
    SUM(revenue) AS Total_Revenue,
    SUM(profit) AS Total_Profit,
    (SUM(profit) / SUM(revenue)) * 100 AS Overall_Profit_Margin
FROM sales_data;

-- 2. Monthly Sales Trends (Revenue Growth)
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS Month,
    SUM(revenue) AS Monthly_Revenue,
    LAG(SUM(revenue)) OVER (ORDER BY DATE_FORMAT(order_date, '%Y-%m')) AS Prev_Month_Revenue,
    ((SUM(revenue) - LAG(SUM(revenue)) OVER (ORDER BY DATE_FORMAT(order_date, '%Y-%m'))) / 
     LAG(SUM(revenue)) OVER (ORDER BY DATE_FORMAT(order_date, '%Y-%m'))) * 100 AS Growth_Rate
FROM sales_data
GROUP BY Month
ORDER BY Month;

-- 3. Region-wise Performance
SELECT 
    region,
    SUM(revenue) AS Total_Revenue,
    SUM(profit) AS Total_Profit,
    COUNT(DISTINCT order_id) AS Total_Orders
FROM sales_data
GROUP BY region
ORDER BY Total_Revenue DESC;

-- 4. Top 10 Best Selling Products (By Revenue)
SELECT 
    product_name,
    category,
    SUM(revenue) AS Total_Revenue,
    SUM(quantity) AS Total_Quantity
FROM sales_data
GROUP BY product_name, category
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 5. Underperforming Products (Negative Profit)
SELECT 
    product_name,
    SUM(revenue) AS Total_Revenue,
    SUM(profit) AS Total_Profit
FROM sales_data
GROUP BY product_name
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC
LIMIT 10;

-- 6. Customer Segmentation (RFM Analysis Lite)
-- Segmenting by Total Purchase Value
SELECT 
    customer_id,
    SUM(revenue) AS Total_Spent,
    COUNT(order_id) AS Order_Frequency,
    CASE 
        WHEN SUM(revenue) > 5000 THEN 'High Value'
        WHEN SUM(revenue) BETWEEN 2000 AND 5000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Customer_Segment
FROM sales_data
GROUP BY customer_id
ORDER BY Total_Spent DESC;
