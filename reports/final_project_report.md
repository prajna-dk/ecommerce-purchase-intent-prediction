# Final Project Report — E-Commerce Purchase-Intent Prediction

## Executive summary
This project predicts conversion from e-commerce session behaviour and presents its results in a five-page Power BI report. The supplied dataset contains **12,000 sessions**, **1,886 buyers**, and a **15.72% conversion rate**. The selected early-session model is a **Random Forest**, trained without PageValues to reduce potential timing/leakage concerns. Its held-out test PR-AUC is **0.5447**.

## Business objective and limitations
Rank sessions for potential engagement interventions while accounting for class imbalance and targeting costs. The data do not establish that any intervention causes additional purchases; all business-value calculations are hypothetical.

## Dataset and preparation
Source: `data/raw/ecommerce_sessions.csv`; prepared dataset: `data/clean_sessions.csv`. Target: `Converted`. Session identifiers are retained for analytics and joins. The project contains notebooks for data inspection, EDA, preparation, model evaluation, final training, explanation and export.

## Modelling and evaluation
Six algorithms were compared in five-fold cross-validation under two feature scenarios: A with PageValues, B without PageValues. The best PR-AUC in A was **CatBoost** at **0.8462**; the best in B was **Random Forest** at **0.5281**. Scenario B was selected for early-session usability despite lower offline performance. The tuned training CV PR-AUC was **0.5286**.

### Final selected model
- Model: **Random Forest**
- Scenario: **B_without_PageValues**
- Selected threshold: **0.72**
- Held-out test PR-AUC: **0.5447**
- Held-out test precision: **0.6311**
- Held-out test recall: **0.4085**
- Confusion matrix: **TN=1933, FP=90, FN=223, TP=154**

## Decision threshold and business economics
Training out-of-fold threshold table (`bi/threshold_table.csv`) reaches its maximum estimated net value at **0.72**, with **806 flagged sessions**, **500 buyers caught**, and **970 illustrative value units**. Formula: `buyers_caught × 50 × 0.2 − flagged_sessions × 5`. These counts are from the threshold evaluation table, **not** the held-out test confusion matrix or a live campaign.

## Explainability
The project includes global SHAP feature importance (`bi/feature_importance.csv`), SHAP and LIME figures, and session-level top-driver exports. Mean absolute SHAP indicates influence magnitude, not positive direction or causality. See `docs/06_explainability_notes.md`.

## Dashboard
`bi/dashboard.pbix` contains the user-completed Power BI report with five pages: Overview; Funnel and Segments; Model Comparison; Threshold and Money; Explainability. Five screenshots are in `bi/screenshots/`. This report uses CSV imports, not the PRD's requested Streamlit application. The engagement funnel is a product-page activity proxy, not cart/checkout event tracking.

## Requirements status
The PRD also specifies FastAPI serving, a six-section Streamlit application with live scoring, MLflow model registry, Docker Compose, GitHub Actions CI, tests, and AWS-ready configuration. **Those components were not present in the submitted archive and have not been represented as complete.** See `docs/PRD_COMPLIANCE_AUDIT.md`.

## Responsible use and future work
Validate timing and leakage, evaluate calibration and out-of-time performance, establish actual intervention lift via randomized experiments, implement production serving and monitoring, and document privacy controls for behavioural data.

## Reproduction
Open the numbered notebooks in `notebooks/` in sequence with the supplied data; verify package versions and Colab environment before rerunning. The existing Power BI file may need CSV source paths updated on refresh. The archive does not yet provide a verified clean-checkout automated build.


## Evaluation extension: calibration, baselines, and business impact

See `reports/evaluation_addendum.md` for the measured reliability diagnostics, random-ranking and constant-score baselines, and sensitivity of hypothetical net value to intervention assumptions. These diagnostics use saved training OOF and held-out scores without refitting the model or changing its selected threshold. The business calculation is **not measured incremental revenue**.
