# **Stage 9 — Power BI Dashboard Documentation**

## **Project Title**

E-Commerce Purchase Intent Prediction

## **Objective**

Develop an interactive Power BI dashboard to visualize shopping-session behaviour, purchase conversion, machine-learning model performance, decision-threshold economics, and model explainability.

## **Data Source**

The dashboard uses CSV files exported from the Google Colab machine-learning pipeline. CSV imports were selected instead of a direct MySQL connection.

**Source files:**

* `data/clean_sessions.csv`  
* `bi/sessions_scored.csv`  
* `bi/model_results.csv`  
* `bi/threshold_table.csv`  
* `bi/feature_importance.csv`

The `clean_sessions` and `sessions_scored` datasets were merged using `session_id` to create the `v_sessions_enriched` table.

## **Dataset Summary**

* Total sessions: 12,000  
* Total purchases: approximately 1,886  
* Overall conversion rate: approximately 15.72%  
* Target variable: `Converted`

## **Dashboard Pages**

### **Page 1 — Overview**

Displays total sessions, total buyers, overall conversion rate, monthly conversion performance, and conversion rates by visitor type.

### **Page 2 — Funnel and Segments**

Displays a behavioural engagement funnel, conversion rate by traffic source, and a Month × Visitor Type conversion heatmap.

The engagement funnel uses recorded product-page activity as a proxy for engagement. It does not represent verified cart or checkout events.

### **Page 3 — Model Comparison**

Compares machine-learning models across scenarios with and without PageValues. PR-AUC is the primary comparison metric, supported by ROC-AUC, precision, recall, F1 score, and accuracy.

### **Page 4 — Threshold and Money**

Displays estimated net business value, precision, recall, and flagged-session counts across decision thresholds. Identifies the threshold with the highest estimated net value in the exported results.

Business-value estimates depend on the assumptions defined in the model evaluation pipeline and do not represent observed incremental revenue.

### **Page 5 — Explainability**

Displays global feature importance using mean absolute SHAP values, individual session prediction scores, top model drivers, and observed conversion rates by risk band.

## **Key Power BI Measures**

**Sessions**

```
Sessions = COUNTROWS(v_sessions_enriched)
```

**Buyers**

```
Buyers = SUM(v_sessions_enriched[Converted])
```

**Conversion Rate**

```
Conversion Rate = DIVIDE([Buyers], [Sessions])
```

## **Validation**

The dashboard was reviewed for:

* Correct overall session and purchase counts.  
* Correct data types and visual aggregations.  
* Consistent model comparison results.  
* Appropriate threshold and business-value interpretation.  
* Functional slicers and cross-filtering.  
* Readable charts, labels, and report layout.

## **Deliverables**

* `bi/dashboard.pbix`  
* `bi/screenshots/page1_overview.png`  
* `bi/screenshots/page2_funnel_segments.png`  
* `bi/screenshots/page3_models.png`  
* `bi/screenshots/page4_threshold.png`  
* `bi/screenshots/page5_explainability.png`  
* `reports/stage9_dashboard_documentation.md`

## **Conclusion**

Stage 9 provides a unified business intelligence dashboard for exploring shopping behaviour, evaluating purchase-intent models, assessing threshold-based targeting decisions, and interpreting predictions.

The dashboard supports analytical decision-making while keeping predictive model outputs distinct from observed customer outcomes.

&nbsp;