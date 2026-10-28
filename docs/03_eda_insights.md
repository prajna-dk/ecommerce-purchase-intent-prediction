# EDA insights — Stage 3

Dataset: `data/clean_sessions.csv` (12,000 sessions; 1,886 buyers; 15.72% conversion). Rates below are descriptive associations, not causal effects.

| Chart | What it shows | Decision it leads to |
| --- | --- | --- |
| 01 outcome | 1,886 of 12,000 sessions converted (15.72%); the nonbuyer class dominates. | Use PR-AUC and buyer recall, not accuracy alone. |
| 02 buyers vs non-buyers | Buyers average PageValues 50.56 vs 5.08, ProductRelated pages 34.41 vs 17.11, and ExitRates 0.0309 vs 0.0584. | Compare models with and without PageValues; investigate when each feature becomes available. |
| 03 month | November leads at 20.00%, while June (9.87%) and February (10.08%) trail. | Treat Month as a category; do not interpret its codes as continuous quantities. |
| 04 visitor type | Returning visitors convert at 16.57% versus 10.17% for new visitors (Other: 15.04%). | Consider an `is_returning` indicator, retaining visitor type in exploratory comparisons. |
| 05 month × visitor type (interactive) | Conversion rates vary across months and visitor segments; smaller groups may be noisy. | Review segment sample sizes before relying on any apparent month-by-visitor difference. |

Additional check: weekend conversion is 15.57% vs weekday 15.76%, a small descriptive difference. No causal conclusion is implied.

**Potential leakage:** `PageValues` may be influenced by events occurring near or after conversion. Before deployment, establish the exact prediction moment and whether `PageValues` is available then. Evaluate a no-PageValues model as a realistic benchmark.

**Outputs:** four PNGs and one interactive HTML in `reports/figures/`. The notebook regenerates all five.
