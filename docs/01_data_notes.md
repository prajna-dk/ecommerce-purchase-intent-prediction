# Stage 1 — Data notes

## Dataset overview
- Source: `data/raw/ecommerce_sessions.csv`; data dictionary: `data/raw/data_dictionary.csv`.
- Rows and columns: **12,000 sessions × 18 original columns**.
- Missing values: **0**; exact duplicate rows: **0**.
- Target: `Converted` (1 = purchase, 0 = no purchase).
- Buyers: **1,886**; non-buyers: **10,114**; conversion rate: **15.72%**.
- Accuracy trap: predicting *no purchase* for everyone gives **84.28% accuracy** but misses every buyer; prioritize PR-AUC and buyer recall.

## Category-like columns
- `OperatingSystems` (8 unique), `Browser` (13), `Region` (9), and `TrafficType` (20) are **category IDs, not numeric magnitudes**. Handle them as categorical features during modeling.
- `Month` (10 unique) and `VisitorType` (3) are categorical strings; treat them as categories, not ordered numeric quantities.
- Months present: Aug, Dec, Feb, Jul, June, Mar, May, Nov, Oct, Sep. January and April are absent; June is spelled `June`.

## PageValues and possible leakage
- `PageValues == 0`: **6,612 sessions**, **0 purchases**, **0.00% conversion**.
- `PageValues > 0`: **5,388 sessions**, **1,886 purchases**, **35.00% conversion**.
- `PageValues` is closely linked to purchase intent and could contain information unavailable at the moment of a real-time prediction. Compare models with and without this feature in Stage 5, and document when the feature is available before deployment.

## Cleaning and output
- Added unique sequential `session_id` from 1 through 12,000 as the first column, for MySQL joins.
- Converted `Weekend` from boolean (`True`/`False`) to integer (1/0).
- Left original source columns and row order otherwise unchanged; no rows were dropped and no missing values required imputation.
- Saved **`data/clean_sessions.csv`** with **12,000 rows × 19 columns**. Original raw files remain untouched.

## Next
Stage 2: Load the cleaned CSV into MySQL Workbench and answer business questions using SQL.
