##Testing Python Application - Finance Data Quality Rule Engine
##Copyright © 2026 Tripp Parker 
Note: This is a public-safe summary of the core API test coverage for the prototype repository. Full working test files may include additional implementation-specific assertions.

## 1. Purpose

"""
`test_app.py` contains core functional tests for the Finance Data Quality Rule Engine — v1.
The purpose of this test file is to verify that the FastAPI application can process representative CSV/XLSX inputs, execute deterministic validation logic, return expected response structures, and handle common user/API scenarios without unhandled failures.
This test file supports prototype confidence, but it does not represent production QA certification, enterprise UAT, security testing, or regulatory validation.
"""

## 2. Testing Scope

The tests in `test_app.py` focus on core application behavior, including:

- API endpoint availability
- CSV upload processing
- Missing value detection
- Duplicate row detection
- Duplicate key detection
- Schema drift detection
- Invalid date detection
- Numeric threshold breach detection
- Unsupported file rejection
- Auto-detection behavior
- Control-pack execution
- Exception report availability

## 3. Primary Endpoints Tested

| Endpoint | Method | Test Purpose |
|---|---|---|
| `/` | GET | Confirms service information endpoint is reachable |
| `/health` | GET | Confirms health/liveness response |
| `/control-packs` | GET | Confirms finance control pack is available |
| `/profile-file` | POST | Confirms uploaded files can be profiled |
| `/scan-file` | POST | Confirms deterministic validation scan executes |

## 4. Representative Test Scenarios

| Scenario | Purpose |
|---|---|
| Clean CSV upload | Confirms valid file can be scanned successfully |
| CSV with nulls | Confirms missing values are detected |
| CSV with duplicate rows | Confirms duplicate full-row detection |
| CSV with duplicate key values | Confirms duplicate key control logic |
| CSV missing expected columns | Confirms schema drift detection |
| CSV with invalid dates | Confirms date validation behavior |
| CSV with threshold breaches | Confirms deterministic numeric min/max rule checks |
| Unsupported file type | Confirms unsupported files are rejected safely |
| Upload-only scan | Confirms auto-detection can run without manual control fields |
| Control-pack scan | Confirms `finance_transaction_controls` executes |
| Exception report request | Confirms report output can be generated through user-initiated export |

## 5. Synthetic Test Data

"""
The tests use generated in-memory or small synthetic files. No production data, client data, personal data, or proprietary datasets are required.

Typical test columns include:

```text

transaction_id
account_id
trade_date
amount
margin_pct
status
source_system

"""
