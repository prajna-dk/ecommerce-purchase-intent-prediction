# Stage 2 — MySQL Workbench instructions

1. Download `data/clean_sessions.csv` to your computer.
2. Connect to your local MySQL server in MySQL Workbench.
3. Open and run `sql/01_create_table.sql` (the final SELECT checks are for **after** importing; they initially return 0 rows).
4. Refresh **Schemas**. Right-click `ecom_purchase.raw_sessions` → **Table Data Import Wizard** → choose `clean_sessions.csv` → **Use existing table**. Confirm all 19 fields map by name; import once only.
5. Run the verification SELECTs at the bottom of `01_create_table.sql`: expect 12,000 sessions, 12,000 distinct IDs, 1,886 buyers, 0.1572 conversion rate.
6. Open `02_questions.sql`, run the six queries, and compare with `docs/02_sql_findings.md`.
7. Run `03_views.sql`; its four verification SELECTs should return 10, 3, 20 and 4 rows.
8. Upload the three `.sql` files to the project's Google Drive `sql/` folder. After successful checks, edit README Stage 2 checkbox from `[ ]` to `[x]`.

**Troubleshooting:** If the wizard fails due to existing IDs, check `SELECT COUNT(*) FROM raw_sessions;` before re-importing. If it has 12,000 rows, do not import again. If only partially imported, investigate and clean up before retrying; don't blindly overwrite rows. MySQL local server and Workbench must be installed and running. The CSV's `Weekend` and `Converted` fields are 0/1.
