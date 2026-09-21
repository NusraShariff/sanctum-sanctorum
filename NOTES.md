Live URL: https://sanctum-sanctorum-1n4b.onrender.com

## Completed

- Implemented ISBN-13 checksum validation and normalized ISBN storage.
- Implemented member email normalization, duplicate detection, and tier access checks.
- Implemented order item validation for empty and duplicate items.
- Completed the loan model with due dates, returns, and persisted late fees.
- Implemented member activity statistics and verified reports.
- Preserved the existing service/router separation and injected clock dependency.

## Architectural decisions

- Request-shape validation stays in Pydantic schemas so invalid orders fail before member or book lookups.
- Business rules and database mutations remain in services; routers only provide dependencies and serialize responses.
- Loan status is computed at read time from the injected current time, while late fees are persisted at return time.
- Order stock is validated for every item before any stock is decremented, preserving all-or-nothing behavior.

## Verification

- `py -m pytest` -> 202 passed.
- The prescribed `uv` command was unavailable in the local PowerShell PATH, so the equivalent Python test command was used.
- Verified that the application starts successfully and the API routes are available through the FastAPI application.

## Remaining work

- The Render deployment uses the default local SQLite database. The service is suitable for
	demonstration, but free instances may reset local database data after restarts or redeploys.

## AI usage

GitHub Copilot was used to inspect the existing implementation and specification, identify incomplete behavior, propose focused changes, and explain the reasoning behind each change. Every change was reviewed against the specification and verified with the test suite. The initial assumption that member statistics could reuse the loan status helper would have introduced a circular import, so that approach was replaced with the equivalent local clock-based calculation.
Verified that the full test suite passes with 202 tests.
Verified the application health endpoint and API documentation after deployment.