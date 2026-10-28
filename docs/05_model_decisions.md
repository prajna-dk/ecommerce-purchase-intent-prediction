# Model decisions

## Comparison (5-fold cross-validation on training data only)

Training rows: 9,600; buyer rate: 15.72%. The test set was not used.

| Scenario | Best model | CV PR-AUC | CV ROC-AUC | CV recall | CV precision |
| --- | --- | ---: | ---: | ---: | ---: |
| A: with PageValues | CatBoost | 0.8462 | 0.9678 | 0.9006 | 0.6311 |
| B: without PageValues | Random Forest | 0.5281 | 0.8259 | 0.5606 | 0.5064 |

Full results: `reports/model_results.csv`.

## PageValues decision
- Scenario A PR-AUC: 0.8462.
- Scenario B PR-AUC: 0.5281.
- Choose **B (without PageValues)** for early-session predictions because PageValues may reflect activity close to conversion; verify feature timing with the team. Keep A as an upper-bound comparison.

## Best model
- **Random Forest** (CV PR-AUC 0.5281) leads scenario B.
- Stage 6 will select a threshold using training-only out-of-fold predictions.
- Business-value constants are illustrative, not validated economics.

## Stage 6: Final model and threshold
- Scenario: B (without PageValues), to reduce potential target-timing leakage.
- Stage 5 winning algorithm: Random Forest (CV PR-AUC 0.5281).
- Tuned training CV PR-AUC: 0.5286; parameters: `{'model__min_samples_leaf': 5, 'model__n_estimators': 400}`.
- Threshold: 0.72, selected by maximizing illustrative net value on out-of-fold training predictions.
- Net value assumption: caught buyers × 50 × 0.2 − flagged sessions × 5. Not a validated causal uplift model.
- Held-out test PR-AUC: 0.5447; precision: 0.6311; recall: 0.4085.
- Confusion matrix: TN=1933, FP=90, FN=223, TP=154.
- Test set used only for the final evaluation; no post-test tuning.
- If business assumptions change, recompute the training OOF threshold, then independently validate before deployment.
