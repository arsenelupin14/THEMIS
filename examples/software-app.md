# Simulation: Software App

PROMPT:
Build a SaaS dashboard for uploaded CSV analytics.

GENERATED WORKROOM:
- Product Strategist
- UX Reviewer
- Backend Contract Reviewer
- Data Validation Reviewer
- QA Skeptic

CHALLENGE:
Data Validation Reviewer challenges Product Strategist:
[QUESTION] What CSV size, schema variability, and invalid-row behavior must be supported?

CONFLICT:
Frontend wants immediate analytics after upload.
Backend/Data reviewer requires async processing for large files.

DECISION:
Use async upload job with job status endpoint.

THEMIS_STATE_V1

G: SaaS dashboard for uploaded CSV analytics
D: software/product/data
C: local MVP, no fake certainty
R: Product, UX, Backend, Data Validation, QA
F: CSV analytics request is under-specified
A: User expects upload and dashboard
Q: max file size, expected analytics, schema rules
K: immediate vs async processing
V: choose async job status flow
T: define API contract, define validation rules, define test cases
X: unclear schema can break UX and backend
N: ask user for max CSV size and analytics type
