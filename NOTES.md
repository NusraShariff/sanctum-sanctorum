Live URL: https://sanctum-sanctorum-1n4b.onrender.com/

The application automatically adds demo members when the database is empty. The seeded members are Wong Li (Supreme, ID 1), Christine Palmer (Master, ID 2), Jonathan Pangborn (Adept, ID 3), and Sara Lin (Apprentice, ID 4).

## Completed

- Implemented ISBN-13 checksum validation and normalized ISBN storage.
- Implemented member email normalization, duplicate detection, and tier access checks.
- Implemented order item validation for empty and duplicate items.
- Implemented the loan model with due dates, returns, and saved late fees.
- Implemented member activity statistics and verified the reports.
- Preserved the existing service/router separation and clock dependency.
- Implemented paginated `GET /members` results with total, limit, and offset information.
- Implemented atomic stock reservation with a conditional database update, preventing concurrent orders from reserving the same final copy.
- Added focused optional tests for member pagination and all-or-nothing stock reservation.

## Architectural decisions

- Request validation stays in Pydantic schemas so invalid orders fail before member or book lookups.
- Business rules and database changes stay in services, while routers only handle dependencies and responses.
- Loan status is calculated when the data is read using the current time, while late fees are saved when a loan is returned.
- Stock is checked for every order item before any stock is reduced, keeping the all-or-nothing behavior.

## Verification

- `uv run pytest` -> 204 passed.
- Verified the application health endpoint and API documentation after deployment.

## Remaining work

- The Render deployment uses the default local SQLite database. The service is suitable for demonstration, but free instances may reset local database data after restarts or redeploys.

## Spec notes

No significant ambiguities or inconsistencies were found in the specification.

## AI usage

GitHub Copilot and Claude were used to inspect the existing implementation and specification, find incomplete parts, suggest focused changes, and help explain the reasoning behind them. I reviewed each change against the specification and test results. One suggested approach was to reuse the loan status helper for member statistics, but this could have caused a circular import, so I did not use that approach and instead used the existing clock dependency for the calculation.