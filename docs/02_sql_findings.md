# Stage 2 — SQL findings

**Source:** `data/clean_sessions.csv` (12,000 sessions). The findings below were calculated directly from the CSV and should be confirmed by running the SQL in MySQL Workbench. SQL execution and database import are **not yet verified**.

## Overall conversion
- 12,000 sessions, 1,886 purchases; conversion rate **15.72%** (0.1572 rounded to four decimals).
- A model that always predicts no purchase would have 84.28% accuracy, making accuracy misleading on its own.

## Months
- Highest conversion: **November**, 447/2,235 = **20.00%**.
- Lowest conversion: **June**, 59/598 = **9.87%**; next lowest: February, 38/377 = **10.08%**.
- Month-to-month differences are descriptive, not causal.

## Visitor types
- Returning visitors: 1,707/10,303 = **16.57%**.
- New visitors: 159/1,564 = **10.17%**.
- Other: 20/133 = **15.04%**.

## PageValues
- PageValues = 0: **0/6,612 = 0%** conversion.
- PageValues > 0: **1,886/5,388 = 35.00%** conversion.
- **Leakage caution:** PageValues may reflect behavior late in a session. Model evaluation must establish whether it would be available at the intended prediction time; compare models with and without it in Stage 5.

## Buyer behavior
- Nonbuyers: average PageValues **5.08**, product pages **17.1**, exit rate **0.0584**.
- Buyers: average PageValues **50.56**, product pages **34.4**, exit rate **0.0309**.

## Traffic
- TrafficType **18** generated the most buyers: **134** from 625 sessions (21.44%).
- TrafficType is a category ID, not a numerical scale.

## Power BI views
- `v_by_month`: month summary with month ordering.
- `v_by_visitor`: visitor-type summary.
- `v_by_traffic`: traffic-source summary.
- `v_funnel`: four **descriptive counts**, not a proven chronological funnel; stages need not be strictly nested by actual event order.

## MySQL verification checklist (complete locally)
- [ ] Imported `clean_sessions.csv` into `ecom_purchase.raw_sessions`.
- [ ] `SELECT COUNT(*) FROM raw_sessions` returns 12,000.
- [ ] Q1–Q6 match the findings above.
- [ ] Four views created and return 10, 3, 20, and 4 rows respectively.
- [ ] SQL files saved in the Google Drive `sql/` folder.
- [ ] Tick Stage 2 in `README.md` after successful verification.
