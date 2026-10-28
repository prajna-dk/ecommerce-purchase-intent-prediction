-- Stage 2: reusable Power BI summary views.
USE ecom_purchase;

CREATE OR REPLACE VIEW v_by_month AS
SELECT Month,
       FIELD(Month, 'Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec') AS month_num,
       COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY Month;

CREATE OR REPLACE VIEW v_by_visitor AS
SELECT VisitorType, COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY VisitorType;

CREATE OR REPLACE VIEW v_by_traffic AS
SELECT TrafficType, COUNT(*) AS sessions, SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions
GROUP BY TrafficType;

CREATE OR REPLACE VIEW v_funnel AS
SELECT 1 AS stage_order, 'All sessions' AS stage, COUNT(*) AS sessions FROM raw_sessions
UNION ALL
SELECT 2, 'Viewed a product page', COUNT(*) FROM raw_sessions WHERE ProductRelated > 0
UNION ALL
SELECT 3, 'Reached a page with value', COUNT(*) FROM raw_sessions WHERE PageValues > 0
UNION ALL
SELECT 4, 'Converted', COUNT(*) FROM raw_sessions WHERE Converted = 1;

-- Validation: these should return 10, 3, 20, and 4 rows respectively.
SELECT * FROM v_by_month ORDER BY month_num;
SELECT * FROM v_by_visitor;
SELECT * FROM v_by_traffic ORDER BY buyers DESC;
SELECT * FROM v_funnel ORDER BY stage_order;
