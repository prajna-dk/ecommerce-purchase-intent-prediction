# Dashboard notes (complete after building and checking Power BI)

| Page | Main message |
| --- | --- |
| 1 Overview | Conversion rate, monthly pattern, and differences between visitor types |
| 2 Funnel and segments | Product-page and valued-page engagement; traffic and visitor segment comparisons |
| 3 Models | Cross-validated PR-AUC comparison with and without PageValues |
| 4 Threshold and money | How the selected threshold trades precision, recall and assumed net value |
| 5 Explainability | Global SHAP drivers, per-session drivers and observed conversion by risk band |

## Data and caveats
- MySQL sources: v_sessions_enriched, v_by_month, v_by_visitor, v_by_traffic, v_funnel, model_results, threshold_table, feature_importance.
- Stage 8 must finish before refreshing this dashboard.
- Funnel stages are proxy engagement counts, not necessarily sequential journeys.
- Scoring probabilities are ranking scores unless calibrated.
- The threshold economics (50, 5, 0.2) are illustrative assumptions, not measured incremental impact.
- The selected final model excludes PageValues if scenario B was used in Stage 6; verify model_info.json.

## Refresh
Rerun Stage 8 exports, reload the four MySQL result tables (avoid duplicate imports), then Refresh in Power BI. Save screenshots to bi/screenshots/.

## Verification
- [ ] Five pages created
- [ ] Slicers and filters tested
- [ ] MySQL tables and views refreshed
- [ ] bi/dashboard.pbix saved
- [ ] Five screenshots saved
