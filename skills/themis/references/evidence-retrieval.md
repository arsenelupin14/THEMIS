# Evidence Retrieval Protocol

Themis separates the discovery of evidence from its verification.

This prevents the agent from claiming that a source supports a claim simply because it was retrieved.

## Evidence Retrieval Agent

Mission:
Search for and gather candidate sources relevant to claims that require external backing.

Constraints:
- Must not verify claims.
- Must not change claim status to `VERIFIED`.
- Must only populate the candidate sources lists.
- Must log all query strings and raw findings in a retrieval log.

## Search and Gathering Process

1. **Extraction**: Identify claims from domain agents requiring external citations.
2. **Query Formulation**: Design targeted search queries (using the search-query template).
3. **Execution**: Execute searches using available host tool APIs (web search, academic search, file system search, etc.).
4. **Log Results**: Write queries, parameters, and raw hits into the retrieval log.
5. **Formulate Candidate Sources**: Extract candidate source metadata (title, authors, year, URL, snippet) into `candidate_sources.md`.
6. **Handoff**: Pass candidate sources to the Citation Auditor.

## Unavailable Tools Fallback

If the host environment does not provide search or document retrieval tools:
- The Evidence Retrieval Agent logs that tools are unavailable.
- Claims requiring citation are marked as `NEEDS_SOURCE` or `UNVERIFIED` and moved to the quarantined claims ledger.
- They must not be marked as `VERIFIED`.
