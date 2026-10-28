USE ecom_purchase;
-- Run AFTER Stage 2 raw_sessions is populated with 12,000 records.
CREATE TABLE IF NOT EXISTS sessions_scored (
 session_id INT PRIMARY KEY, probability DOUBLE, score_source VARCHAR(20), predicted TINYINT,
 risk_band VARCHAR(10), top_driver_1 VARCHAR(100), top_driver_2 VARCHAR(100), top_driver_3 VARCHAR(100),
 CONSTRAINT fk_scored_session FOREIGN KEY(session_id) REFERENCES raw_sessions(session_id)
);
CREATE TABLE IF NOT EXISTS model_results (
 scenario VARCHAR(40), model VARCHAR(40), cv_pr_auc DOUBLE, cv_roc_auc DOUBLE,
 cv_recall DOUBLE, cv_precision DOUBLE, cv_f1 DOUBLE, cv_accuracy DOUBLE
);
CREATE TABLE IF NOT EXISTS threshold_table (
 threshold DOUBLE, sessions_flagged INT, true_buyers_caught INT, prec DOUBLE, rec DOUBLE, net_value DOUBLE
);
CREATE TABLE IF NOT EXISTS feature_importance (
 feature VARCHAR(80), shap_mean_abs DOUBLE, perm_importance DOUBLE
);
CREATE OR REPLACE VIEW v_sessions_enriched AS
SELECT r.*,s.probability,s.score_source,s.predicted,s.risk_band,s.top_driver_1,s.top_driver_2,s.top_driver_3,
 FIELD(r.Month,'Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec') AS month_num
FROM raw_sessions r INNER JOIN sessions_scored s USING(session_id);
-- After importing each matching bi/*.csv into the existing table, verify:
SELECT COUNT(*) AS raw_rows FROM raw_sessions;
SELECT COUNT(*) AS scored_rows FROM sessions_scored;
SELECT COUNT(*) AS comparison_rows FROM model_results;
SELECT COUNT(*) AS threshold_rows FROM threshold_table;
SELECT COUNT(*) AS importance_rows FROM feature_importance;
SELECT COUNT(*) AS enriched_rows FROM v_sessions_enriched;
SELECT risk_band,COUNT(*) AS sessions,ROUND(AVG(Converted),4) AS actual_conversion
FROM v_sessions_enriched GROUP BY risk_band ORDER BY FIELD(risk_band,'Low','Medium','High');
