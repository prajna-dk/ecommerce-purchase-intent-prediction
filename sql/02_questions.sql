-- Stage 2: run each query separately in MySQL Workbench.
USE ecom_purchase;

-- Q1. Overall sessions, buyers, conversion rate.
SELECT COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions;

-- Q2. Conversion by PageValues flag.
SELECT (PageValues > 0) AS has_page_value,
       COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY (PageValues > 0)
ORDER BY has_page_value;

-- Q3. Months ranked by conversion rate.
SELECT Month, COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY Month
ORDER BY conversion_rate DESC;

-- Q4. Conversion by visitor type.
SELECT VisitorType, COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY VisitorType
ORDER BY conversion_rate DESC;

-- Q5. Behavioral differences between buyers and nonbuyers.
SELECT Converted,
       ROUND(AVG(PageValues), 2) AS avg_page_values,
       ROUND(AVG(ProductRelated), 1) AS avg_product_pages,
       ROUND(AVG(ExitRates), 4) AS avg_exit_rate
FROM raw_sessions
GROUP BY Converted;

-- Q6. Traffic sources ranked by number of buyers.
SELECT TrafficType, COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY TrafficType
ORDER BY buyers DESC, TrafficType;
