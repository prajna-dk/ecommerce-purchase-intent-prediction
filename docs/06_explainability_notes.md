# Explainability notes

- Model: RandomForestClassifier; PageValues included: False.
- SHAP sample: 500 held-out sessions (not the full test population).
- Top 5 overall SHAP drivers: ProductRelated, ExitRates, total_pages, BounceRates, total_duration.
- Example session score: 0.0090. Three largest signed drivers: ExitRates (-), total_pages (-), ProductRelated (-).
- LIME top local terms: numbers__ExitRates > 0.52, numbers__total_pages <= -0.40, numbers__ProductRelated <= -0.43, categories__Browser_12 <= 0.00, categories__VisitorType_Other <= 0.00.
- SHAP, LIME, and permutation measure different quantities; compare broad patterns rather than expecting identical ranks.
- Permutation importance is evaluated on a held-out sample and must not be used to retune the model after the final test.
- SHAP values explain associations learned by the model, not causes of purchase. PageValues availability and score calibration require care.
