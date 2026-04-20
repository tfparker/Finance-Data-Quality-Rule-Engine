##Testing Ingestion Risk Python Script - Finance Data Quality Rule Engine
##Copyright © 2026 Tripp Parker 

The project includes a private regression suite covering representative CSV/XLSX ingestion risks using synthetic data only.

Coverage categories:
- Unsupported files
- Empty and header-only files
- UTF-8 BOM handling
- Windows-1252 characters
- Quoted commas
- Malformed rows
- Long numeric identifier preservation
- Leading zero preservation
- Mixed-type columns
- Thousand separator detection
- XLSX sheet handling
- Invalid dates
- Excel serial-looking dates
- Slash-date ambiguity
- Duplicate columns
- Blank columns
- Mostly empty columns
- Duplicate full rows
- Stable response structure

Reported coverage:
- 33 ingestion-risk tests
- Synthetic data only
- No production data
- No client data
- No private data
