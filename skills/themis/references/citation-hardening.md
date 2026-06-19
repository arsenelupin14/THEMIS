# Citation Hardening

Themis must prevent hallucinated citations and unsupported evidence claims.

## Core rule

No verified source, no evidence claim.

## Claim statuses

- VERIFIED
- UNVERIFIED
- NEEDS_CITATION
- CITATION_FAILED
- DISPUTED
- QUARANTINED
- RETRACTED

## Source tiers

Tier 1:
Peer-reviewed papers, official datasets, textbooks, standards bodies.

Tier 2:
Preprints, arXiv, technical reports, institutional reports.

Tier 3:
Documentation, lab notes, reputable news, official project pages.

Tier 4:
Blogs, forums, model inference, unsupported claims.

## Citation audit process

1. Extract claims.
2. Mark whether each claim requires a source.
3. Search or inspect candidate sources when tools are available.
4. Verify title, author, year, venue, DOI/URL when available.
5. Check whether the source actually supports the claim.
6. Downgrade unsupported claims.
7. Quarantine failed claims.
8. Only pass verified claims to the clean draft.

## Forbidden behavior

- Do not invent citations.
- Do not cite a real paper for a claim it does not support.
- Do not use vague “studies show” phrasing.
- Do not keep [EVIDENCE] labels for unverified claims.
