# Stages 9–11: runbook

## Stage 9: Power BI Desktop
1. Verify Stage 8 MySQL imports, especially 12,000 rows in `v_sessions_enriched`.
2. Home > Get data > MySQL database; server `localhost`, database `ecom_purchase`; Import. Install the MySQL connector if prompted.
3. Select `v_sessions_enriched`, `v_by_month`, `v_by_visitor`, `v_by_traffic`, `v_funnel`, `model_results`, `threshold_table`, `feature_importance`.
4. Set Month to sort by month_num in the relevant tables. Use `v_sessions_enriched` for slicers and cross-filtered cards; aggregate views may not automatically respond to those slicers.
5. Right-click `v_sessions_enriched` > New measure, create each measure from `bi/POWER_BI_MEASURES.dax.txt`.
6. Create five pages:
   - Overview: cards for Sessions/Buyers/Conversion Rate, monthly and visitor conversion bars, Month/VisitorType slicers.
   - Funnel and segments: funnel of stage/sessions, traffic-source bar, Month × VisitorType conversion matrix.
   - Models: model_results table and grouped PR-AUC by model/scenario.
   - Threshold and money: threshold/net_value line, threshold/precision/recall lines, cards for flagged, precision, recall; explain the assumptions.
   - Explainability: top-12 SHAP bar, session score/driver table filtered by risk_band, risk_band conversion summary.
7. Confirm slicer interactions, month order, all visuals and no ambiguous relationships. Save `bi/dashboard.pbix`, and five screenshots in `bi/screenshots/`. Complete `docs/07_dashboard_notes.md`.
8. Tick Stage 9 only after these checks.

## Stage 10 (optional)
1. Confirm `models/final_model.joblib` and `models/model_info.json` exist in Drive.
2. Open `notebooks/07_predict_demo.ipynb` and Run all.
3. It scores a sample session, an unseen region, and tests `/health` and `/predict` using FastAPI TestClient.
4. Tick Stage 10 if successful; otherwise mark it skipped (optional).

## Stage 11
1. Restart runtime and run every notebook top-to-bottom; verify MySQL imports and Power BI refresh.
2. Fill actual Stage 6 metrics and Stage 7 drivers in `docs/model_card.md` and the final README; do not use placeholder values.
3. Create pinned `requirements.txt` from your tested runtime (see `docs/GENERATE_REQUIREMENTS.md`).
4. Confirm `.gitignore` excludes caches and logs. Review datasets, model binaries and PRD for permission to publish before uploading to GitHub.
5. Verify files, screenshots, and links, then push to GitHub. Tick Stage 11 only after upload succeeds.

**Note:** A working `.pbix` cannot be generated or validated without Power BI Desktop. This package contains instructions, not a fabricated dashboard file.
