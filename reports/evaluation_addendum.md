# Evaluation Addendum — Calibration, Baselines, and Business Impact

## Scope and provenance

This addendum uses **existing exported scores**, not a retrained model. `bi/sessions_scored.csv` contains 9,600 `train_oof` predictions and 2,400 `test_holdout` predictions, joined to observed `Converted` labels by `session_id` in `data/train.csv` and `data/test.csv`. The stored test predictions reproduce the recorded confusion matrix (TN=1933, FP=90, FN=223, TP=154). The selected model is Random Forest in B_without_PageValues; its selected threshold remains 0.72. No test-driven threshold tuning or calibration fitting was performed.

## 1. Calibration diagnostics

| Metric | Training OOF | Held-out test |
|---|---:|---:|
| Sessions | 9,600 | 2,400 |
| Purchase prevalence | 15.72% | 15.71% |
| Brier score (model; lower is better) | 0.1190 | 0.1163 |
| Brier score (constant-prevalence baseline) | 0.1325 | 0.1324 |
| Log loss (model; lower is better) | 0.3845 | 0.3795 |
| Log loss (constant-prevalence baseline) | 0.4350 | 0.4348 |

See `reports/calibration_reliability.png` and `reports/calibration_reliability_bins.csv`. These are **diagnostics**, not a fitted probability calibration model. Reliability bins contain sampling uncertainty; the chart is not evidence of guaranteed individual probability accuracy. If probability calibration is required for deployment, fit a calibrator on training-only out-of-fold predictions or a separate training-side calibration set, then evaluate once on a fresh untouched test set. The existing held-out test set must not be used to select or fit a calibrator and then reused as an unbiased final evaluation.

## 2. Baseline comparisons

| Metric | Training OOF | Held-out test |
|---|---:|---:|
| Model average precision (PR-AUC summary) | 0.5245 | 0.5447 |
| Random-ranking expected AP / purchase prevalence | 0.1572 | 0.1571 |
| Model ROC-AUC | 0.8252 | 0.8430 |

The random-ranking AP baseline is prevalence, not a separately fitted classifier. A constant-prevalence prediction baseline is included for proper scoring rules (Brier and log loss). These baselines provide context, but do not establish profitability or prospective generalization. Accuracy alone is misleading for an imbalanced purchase outcome.

## 3. Business-impact explanation and sensitivity

The original threshold analysis assumes value per successful incremental conversion **50 units**, intervention success **20%**, and cost per flagged session **5 units**. The formula is:

`estimated_net_value = true_buyers_caught × conversion_value × assumed_nudge_success − sessions_flagged × cost_per_flagged_session`

This is a **hypothetical scenario calculation**, not measured incremental lift or realized revenue. It implicitly applies the assumed intervention effect to identified existing buyers; this does **not** prove those conversions are incremental, nor does it measure how nonbuyers might respond. Real economic impact requires randomized intervention/control measurement, incremental lift, costs, and operational constraints.

At the fixed selected threshold 0.72, held-out test predictions flag 244 sessions, catch 154 buyers, and yield **320 illustrative units** under these assumptions. This held-out number is descriptive, not a threshold-selection objective and not a causal business outcome. The threshold table contains training OOF counts, so do not mix its net-value totals with test-set totals.

The sensitivity analysis in `reports/business_impact_sensitivity.csv` recomputes estimated value under several assumptions using **training OOF threshold counts only**. Alternative optima are *scenario illustrations*, not recommendations validated on the test set.

## 4. Evaluation safeguards and limitations

- Model and threshold are unchanged; no fitting or threshold tuning uses the held-out test labels.
- Source score files and saved model metadata remain unchanged.
- Saved model was built with scikit-learn 1.6.1; this environment has 1.8.0, and the model artifact did not load successfully here. The evaluation instead uses the saved score export, independently matched to split labels and the recorded confusion matrix.
- Because the held-out test set has already been examined, further modelling changes should be validated on a new untouched or prospective test set.
- Confirm the timing/availability of all prediction features and the operational definition of the intervention before deployment.
