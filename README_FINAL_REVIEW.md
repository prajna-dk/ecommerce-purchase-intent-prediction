# Reviewed Project Package

This folder preserves the supplied project and adds a verified-numbers final report, a model card, a PRD gap audit, and a presentation outline.

**Start here:** `docs/PRD_COMPLIANCE_AUDIT.md`. The current CSV + Power BI implementation does **not** satisfy the PRD's required API, Streamlit, MLOps, and deployment scope.

**Key files:** `reports/final_project_report.md`, `docs/MODEL_CARD.md`, `presentation/PRESENTATION_OUTLINE.md`, `bi/dashboard.pbix`, `bi/screenshots/`, `models/model_info.json`.

**Accuracy note:** Dashboard file and screenshots are included as provided; visual functionality has not been independently tested. No missing production components are claimed to exist.


### Evaluation extension

See `reports/evaluation_addendum.md`, `reports/calibration_reliability.png`, `reports/evaluation_addendum_metrics.json`, and `reports/business_impact_sensitivity.csv`. Reproduce with `python scripts/evaluate_saved_scores.py`. No model or threshold was changed.
