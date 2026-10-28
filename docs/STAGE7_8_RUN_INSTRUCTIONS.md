# Stages 7 and 8: execution checklist

1. In MyDrive/Internmo/purchase_intent_project, confirm Stage 6 produced `models/final_model.joblib` and `models/model_info.json` and Stage 5 produced 12 rows in `reports/model_results.csv`.
2. Upload the updates package while preserving folder paths. Open `notebooks/05_explain.ipynb` in Colab and Run all. Review SHAP, LIME, permutation chart, and generated `docs/06_explainability_notes.md`.
3. Open `notebooks/06_export.ipynb` and Run all. It exports four CSVs into `bi/`.
4. Download the four CSVs to your computer. Run `sql/04_results_tables.sql` in MySQL Workbench **before** importing. Import CSVs into the four existing tables, mapping all columns, including `score_source`.
5. Run the verification queries at the bottom of the SQL script. Expect 12,000 scored/enriched rows, 12 model results, 91 thresholds. Importance rows depend on the features.
6. Only after these checks pass, tick Stages 7 and 8 in README.md.

Caution: Test rows receive final-model scores; training rows receive out-of-fold scores. Driver explanations use the final model for all rows and are approximate for OOF scores. `probability` is an uncalibrated ranking score. The threshold economics are hypothetical, not measured uplift.
