# Purchase-Intent Prediction with Explainable AI

Predict purchase intent from anonymized e-commerce sessions using Colab, MySQL, and Power BI.

## Status
Stages 0–8: verify against your own Colab and MySQL outputs.
Stage 9: pending Power BI build and screenshots.
Stage 10: optional, pending notebook/API test.
Stage 11: pending final reproducibility checks and GitHub upload.

## Headline results
- Observed conversion rate: 1,886 / 12,000 = 15.72%.
- Final model and test metrics: fill from models/model_info.json and Stage 6 test output.
- PageValues choice: confirm in model_info.json and explain the timing/leakage tradeoff.

## Structure
`data/` raw, clean, train, test; `notebooks/` Colab notebooks; `sql/` MySQL scripts; `models/` trained model and metadata; `reports/` results and figures; `bi/` dashboard and exports; `docs/` stage notes and model card; `helpers.py` shared code; `app.py` optional API.

## Reproduce
1. Mount Drive and run notebooks in order, from a fresh runtime.
2. Execute SQL scripts in order and import cleaned/BI CSV files as directed.
3. Build and save `bi/dashboard.pbix` in Power BI Desktop.
4. Verify the five screenshots, refresh, model card, and Stage 10 demo (if included).

## Limitations and next steps
- Calibrate probabilities before treating them as literal probabilities.
- Evaluate real nudge uplift in an A/B test.
- Add automated validation and data drift monitoring.
