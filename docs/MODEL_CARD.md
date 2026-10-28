# Model Card — Selected Purchase Intent Model

**Model:** Random Forest | **Scenario:** B_without_PageValues | **Threshold:** 0.72

**Intended use:** Offline ranking of shopping sessions for analyst review and hypothetical targeting scenarios. Not a proven uplift model.

**Data:** 12,000 synthetic/packaged e-commerce sessions; buyer prevalence 15.72%. Evaluation uses the documented train/test split and training-only cross-validation.

**Held-out test:** PR-AUC 0.5447; precision 0.6311; recall 0.4085; confusion matrix [[1933, 90], [223, 154]].

**Leakage precaution:** PageValues excluded from the final model because its timing could make it unsuitable for early predictions.

**Limitations:** Offline dataset; model calibration not established; potential distribution drift; no causal intervention validation; session-level explanations are associations rather than causal drivers. Do not deploy without independent validation, monitoring, and privacy review.

**Artifact:** `models/final_model.joblib`; metadata: `models/model_info.json`.


## Additional evaluation

Calibration diagnostics, prevalence baselines, and assumption sensitivity are documented in `reports/evaluation_addendum.md`. These do not establish causal campaign lift or guarantee calibrated individual probabilities.
