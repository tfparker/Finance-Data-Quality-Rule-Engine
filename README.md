##Finance Data Quality Rule Engine — v1
##Copyright © 2026 Tripp Parker 

Status: Work in Progress / v1 Prototype Freeze Candidate
Project Type: Python/FastAPI finance data governance prototype
Primary Use Case: Deterministic data quality validation for uploaded CSV/XLSX finance datasets

##

Overview

Finance Data Quality Rule Engine — v1 is a lightweight Python/FastAPI prototype that validates uploaded CSV and XLSX files for common finance data quality and control-readiness issues.

The project is designed as a deterministic finance data governance prototype, not as an AI system, forecasting model, dashboard, production data quality platform, or automated decisioning tool.

The engine accepts uploaded files, profiles the dataset, applies a reusable finance transaction control pack, returns structured JSON results, and supports user-initiated export of a downloadable exception report.

The current v1 scope focuses on transparency, auditability, and defensible control logic rather than automation, prediction, or UI polish.

###

What This Project Demonstrates

This prototype demonstrates how a lightweight data quality validation layer can be used to identify common issues in finance-style datasets before those files are used for reporting, reconciliation, analysis, or control review.

It is intended to show applied capability in:

* Finance data governance
* Data quality validation
* Control-pack design
* Deterministic exception detection
* Python/FastAPI prototyping
* CSV/XLSX ingestion safeguards
* Audit metadata design
* Testing and limited prototype UAT documentation

##

Core Capabilities

File Intake

The engine supports:

* CSV uploads
* XLSX uploads
* File profiling
* Upload-only scanning with auto-detection
* Optional manual configuration overrides
* Defensive handling of common Python/pandas ingestion risks

Validation and Control Logic

The engine detects or warns on issues including:

* Missing required values
* Duplicate full rows
* Duplicate transaction identifiers
* Invalid dates
* Excel serial-looking dates
* Locale-ambiguous slash dates
* Non-numeric amount values
* Negative or excessive amount values
* Margin percentage validity issues
* Missing source system values
* Long numeric identifier precision risk
* Leading/trailing whitespace
* Thousand separator formatting issues
* Header-only files
* Unsupported file types
* Corrupt or unreadable XLSX files

Outputs

The scan output includes:

* File summary
* Data type summary
* Intake metadata
* Control pack summary
* Control-level results
* Rule summary
* Exceptions by rule
* Affected columns
* Affected row counts
* Warnings
* Audit metadata
* Optional downloadable exception report

##

API Endpoints

Endpoint	Method	Purpose
/	GET	Service information
/health	GET	Health/liveness check
/control-packs	GET	Lists available control packs
/profile-file	POST	Profiles uploaded file and suggests likely columns
/scan-file	POST	Runs full deterministic validation scan

###

Default Control Pack

The default control pack is:

finance_transaction_controls

Controls

Control ID	Control Name	Purpose
C001	REQUIRED_FIELDS	Checks required finance transaction fields for missing or blank values
C002	TRANSACTION_ID_UNIQUENESS	Detects duplicate transaction identifiers
C003	DATE_VALIDITY	Detects invalid dates, Excel serial-looking dates, and ambiguous slash dates
C004	AMOUNT_NUMERIC_VALIDITY	Confirms amount values can be parsed numerically
C005	AMOUNT_REASONABLENESS	Detects negative or excessive amount values
C006	MARGIN_PCT_VALIDITY	Validates margin percentage values as numeric and within expected range
C007	SOURCE_SYSTEM_COMPLETENESS	Checks source system lineage/control-readiness field completeness
C008	LONG_IDENTIFIER_PRECISION_RISK	Warns when long numeric identifiers may be at precision risk
C009	STRING_HYGIENE	Detects leading/trailing whitespace in string fields
C010	DUPLICATE_ROW_RECONCILIATION_RISK	Detects duplicate full rows

##

Example Transaction Columns

The prototype works with arbitrary CSV/XLSX files, but the default control pack is most meaningful for transaction-style datasets with columns such as:

transaction_id
account_id
trade_date
settlement_date
amount
margin_pct
status
source_system
region
product_type

##

Example Request Fields

For /scan-file, the user may upload only a file and allow auto-detection to run.

Optional fields include:

Field	Required	Description
file	Yes	CSV or XLSX file
sheet_name	No	Optional XLSX sheet selection
auto_detect	No	Defaults to true
key_columns	No	Comma-separated key columns
expected_columns	No	Comma-separated expected schema columns
date_column	No	User-specified date column
threshold_rules	No	JSON string containing numeric min/max rules
include_csv_report	No	Returns downloadable exception report when invoked
control_pack	No	Defaults to finance_transaction_controls

Example threshold rules:

{
  "amount": {"min": 0, "max": 1000000},
  "margin_pct": {"min": 0.05}
}

##

Ingestion Protections Covered

This project includes documented and regression-tested safeguards for common CSV/XLSX ingestion and transformation failure modes.

File-Level Protections

* Unsupported file type rejection
* Empty CSV handling
* Header-only CSV handling
* Oversized file rejection
* Corrupt XLSX handling

CSV Encoding and Parsing

* UTF-8 BOM handling
* Windows-1252 / Latin-1 fallback handling
* Quoted comma preservation
* Delimiter drift warning
* Malformed row warning

Type Preservation

* Long numeric transaction IDs preserved as strings
* Leading zero identifiers preserved
* Mixed-type column warnings
* Thousand separator detection
* Blank strings treated as missing

Excel Handling

* Visible sheet reading
* Hidden sheet warnings
* Missing requested sheet handling
* Blank row handling
* Footer-like row warnings
* Repeated header row warnings

Date Handling

* Valid ISO date handling
* Slash-date ambiguity warning
* Invalid date detection
* Excel serial date warning
* Blank date treated as missing rather than invalid

Column and Schema Hygiene

* Duplicate column name warning
* Unnamed/blank column warning
* Mostly empty column warning
* Leading/trailing whitespace warning
* Duplicate full-row detection

##

Testing Summary

This project includes automated functional and regression tests.

Reported test coverage includes:

* Core API behavior
* CSV upload processing
* XLSX upload processing
* Control-pack execution
* Missing value detection
* Duplicate row detection
* Duplicate key detection
* Date validation
* Threshold validation
* Downloadable exception report behavior
* Ingestion-risk safeguards

A dedicated ingestion-risk regression suite was added:

test_ingestion_risks.py

Reported ingestion-risk coverage:

* 33 ingestion-risk tests
* File-level failures
* CSV encoding/parsing
* Type preservation
* Excel handling
* Date handling
* Column/schema hygiene
* Structural response invariants

##

Limited Prototype UAT

Limited prototype UAT was performed using generated UAT sample files and FastAPI/Swagger execution.

This was not enterprise UAT, production certification, regulatory validation, security approval, or formal business-owner signoff.

UAT Scenario Summary

Scenario ID	Scenario Name	Type	Result
UAT-001	Health check returns version	Positive	PASS
UAT-002	Control-packs listing returns 10 controls	Positive	PASS
UAT-003	Valid CSV scan — all controls pass	Positive	PASS
UAT-004	Profile file returns column suggestions	Usability	PASS
UAT-005	Downloadable exception report is available after scan	Output	PASS
UAT-006	Dirty data — duplicates, invalid dates, missing fields	Negative	PASS
UAT-007	Unsupported file type rejected	Negative	PASS
UAT-008	Header-only CSV — zero rows handled gracefully	Negative	PASS
UAT-009	Invalid threshold JSON rejected before scan	Negative	PASS
UAT-010	XLSX with empty/header-only sheet handled gracefully	Negative	PASS

Summary:

10 scenarios executed
10 passed
0 failed

##

Project Documentation

The project documentation package includes:

docs/BRD.md
docs/FRD.md
docs/TESTING.md
docs/UAT.md

Documentation covers:

* Business requirements
* Functional requirements
* Testing approach
* Ingestion-risk coverage
* Limited prototype UAT
* V1 scope and limitations
* Future version candidates

##

Suggested File Structure

finance-data-quality-rule-engine/
├── main.py
├── requirements.txt
├── test_app.py
├── test_ingestion_risks.py
├── README.md
├── docs/
│   ├── BRD.md
│   ├── FRD.md
│   ├── TESTING.md
│   └── UAT.md
├── sample_data/
│   ├── sample_trade_transactions_100.csv
│   ├── valid_trade_sample.csv
│   ├── dirty_trade_sample.csv
│   ├── header_only.csv
│   ├── header_only_sheet.xlsx
│   └── unsupported_file.txt
└── reports/
    └── sample_exception_report.csv

Actual file structure may vary depending on the Replit project export.

##

How to Run Locally

Install dependencies:

pip install -r requirements.txt

Run the API:

uvicorn main:app --host 0.0.0.0 --port 8000

Open Swagger UI:

http://localhost:8000/docs

Run tests:

python -m pytest -v

##

Design Boundaries

This prototype intentionally does not include:

* AI-generated findings
* Recommendations
* Forecasting
* Predictive scoring
* Automated decisioning
* Alerts or notifications
* Authentication
* Database persistence
* Production deployment hardening
* Workflow routing
* Approval workflows
* Full dashboard UI
* PII detection
* AML/fraud decisioning
* Credit decisioning
* Enterprise-scale processing

Required deterministic method note:

No prediction, scoring, or automated decisioning performed.

##

Known Limitations

This project is a v1 prototype and has known limitations:

1. It is not production-hardened.
2. It does not persist scan history.
3. It does not compare current files against prior baselines.
4. It does not perform source-to-target reconciliation.
5. It does not perform multi-file balancing.
6. It does not automatically repair data.
7. It does not support complex Excel workbook extraction across multiple embedded tables.
8. It is not designed for very large enterprise-scale files.
9. It does not provide role-based access control.
10. It does not include security testing or production certification.
11. Limited prototype UAT used generated sample files, not production data.
12. Warning counts and failed exception counts should be reviewed carefully when interpreting summary metrics.

##

Future Version Candidates

Potential future versions may include:

V2: Baseline vs Current File Comparison

A future version may allow users to upload a baseline file and current file to compare:

* New control failures
* Resolved control failures
* Control failure rate deltas
* Schema changes
* Row count changes
* Warning observation changes
* New vs recurring exceptions

This would extend the prototype toward signal governance and drift detection without adding forecasting or automated decisioning.

Additional Future Enhancements

* External JSON/YAML control-pack definitions
* Control severity metadata
* Control owner placeholder metadata
* Row-level exception inventory refinement
* Downloadable executive control summary
* Additional finance-specific control packs

##

Status

Current status: Work in Progress / v1 Prototype Freeze Candidate

The current build is suitable for portfolio demonstration and continued documentation, provided it is represented accurately as a prototype. It has been supported by developer-led functional testing, ingestion-risk regression testing, and limited prototype UAT using generated sample data.

This project should is not represented as production-ready, enterprise-certified, security-approved, regulatory-validated, or independently business-signed-off.


Next build:

Finance Data Quality Rule Engine — v2: Baseline vs Current File Comparison / Signal Governance Edition
