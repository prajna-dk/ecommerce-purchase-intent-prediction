# Data preparation decisions

| Decision | Why |
| --- | --- |
| 80/20 stratified split, seed 42 | Keep 2,400 test sessions untouched until final evaluation; reproducible buyer proportions |
| Category IDs one-hot encoded | OperatingSystems, Browser, Region and TrafficType are labels, not ordered quantities; Month and VisitorType are categorical too |
| Duration and PageValues columns log1p then RobustScaler | Reduce right-skew and outlier influence; log1p handles zeros |
| `total_pages` | Sum administrative, informational and product page counts |
| `total_duration` | Sum time across the three page families |
| `avg_time_per_page` | Total duration divided by total pages, safe when page count is zero |
| `product_page_share` | Fraction of pages that are product-related |
| `product_time_share` | Fraction of browsing duration spent on product pages |
| `is_returning` | Indicator derived from VisitorType |
| Pipeline | Learn scaling and one-hot categories from training folds only, avoiding test-set leakage |
| Class imbalance | Apply class weights to models that support them in Stage 5; prioritize PR-AUC and buyer recall |
| PageValues | Compare with and without it because availability at inference time may create leakage |

## Split verification
- Original: 12,000 rows, 19 columns.
- Train: 9,600 rows, 1,509 buyers (15.7188%).
- Test: 2,400 rows, 377 buyers (15.7083%).
- Test data was used only to create and verify the split, not to fit the pipeline.
- Preprocessing smoke test: logistic-regression pipeline fits training data with PageValues excluded; 79 transformed features.

## Note on business-value assumptions
The 50-unit conversion value, 5-unit nudge cost and 20% nudge-success rate in `helpers.py` are **illustrative**, not validated business estimates. They must be reviewed before using net value to select a threshold. The threshold table counts already-converting buyers, which does not establish incremental conversions caused by a nudge.
