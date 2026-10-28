# PRD Compliance Audit — 28 October 2026

**Source of truth:** `docs/PRD.docx` in the supplied project. **Assessment:** file-level inspection of the user-submitted archive; existence does not establish that code executes or that screenshots reflect a functioning report.

| PRD requirement | Evidence in supplied archive | Status |
|---|---|---|
| Raw data and data dictionary | `data/raw/ecommerce_sessions.csv`, `data/raw/data_dictionary.csv` | Present |
| Data exploration and preparation | Numbered notebooks, clean sessions CSV, EDA figures | Present; runtime not reverified |
| Six-model comparison, imbalance-aware metrics | `bi/model_results.csv` (12 rows), model notebooks | Present |
| Saved final model and value-based threshold | `models/final_model.joblib`, `models/model_info.json`, threshold CSV | Present; runtime not reverified |
| Global SHAP and local LIME | Figures, explainability notebook, feature importance | Present; runtime not reverified |
| Model card | `docs/MODEL_CARD.md` (added in this reviewed package) | Documentation added |
| FastAPI `/predict`, `/health`, `/docs`, validation and explanations | No `src/api` or API app in submitted archive | **Missing** |
| Six-section Streamlit dashboard including live scoring | Power BI PBIX + five screenshots instead | **Not PRD-compliant substitution** |
| Docker and Docker Compose | No Dockerfiles or compose config | **Missing** |
| MLflow runs and model registry | No tracking integration or run evidence | **Missing** |
| GitHub Actions CI and pytest tests | No workflow or tests directory | **Missing** |
| AWS-ready deployment configuration | No deployment/config package | **Missing** |
| Central typed/YAML config and production `src/` modules | Not present as specified | **Missing** |
| Clean-checkout README and pinned dependencies | Original README is a stage progress note; no pinned dependency manifest | **Incomplete** |
| Final written report | `reports/final_project_report.md` (added) | Added |
| Presentation | `presentation/PRESENTATION_OUTLINE.md` (added) | Outline only |

## Critical scope decision
The work delivered so far follows a **CSV + Power BI analysis route**, not the PRD's production-serving architecture. A reviewer must explicitly approve this change or the missing requirements must be implemented and verified. Do not describe the archive as fully PRD-compliant.

## Verification boundaries
- Confirmed ZIP contains a PBIX and five PNG screenshots; the report was not opened in Power BI Desktop in this environment.
- Threshold CSV peak and final model metadata agree at 0.72.
- No live API, container, CI, or MLflow validation has been performed.
- No GitHub push or cloud deployment has been performed.
