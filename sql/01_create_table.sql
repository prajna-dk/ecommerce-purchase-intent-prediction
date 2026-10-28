-- Stage 2: create schema and table. Run before using Workbench Table Data Import Wizard.
CREATE DATABASE IF NOT EXISTS ecom_purchase;
USE ecom_purchase;

CREATE TABLE IF NOT EXISTS raw_sessions (
  session_id INT PRIMARY KEY,
  Administrative INT,
  Administrative_Duration DOUBLE,
  Informational INT,
  Informational_Duration DOUBLE,
  ProductRelated INT,
  ProductRelated_Duration DOUBLE,
  BounceRates DOUBLE,
  ExitRates DOUBLE,
  PageValues DOUBLE,
  SpecialDay DOUBLE,
  Month VARCHAR(10),
  OperatingSystems TINYINT,
  Browser TINYINT,
  Region TINYINT,
  TrafficType TINYINT,
  VisitorType VARCHAR(20),
  Weekend TINYINT,
  Converted TINYINT
);

-- Import data/clean_sessions.csv into raw_sessions using Table Data Import Wizard.
-- Select existing table and verify all 19 columns map correctly.
-- Run these AFTER the import:
SELECT COUNT(*) AS imported_sessions FROM raw_sessions; -- expected 12000
SELECT COUNT(DISTINCT session_id) AS distinct_ids,
       SUM(Converted) AS buyers,
       ROUND(AVG(Converted), 4) AS conversion_rate
FROM raw_sessions; -- expected 12000, 1886, 0.1572
