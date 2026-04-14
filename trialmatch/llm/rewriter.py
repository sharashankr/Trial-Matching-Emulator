from __future__ import annotations

from typing import List
from trialmatch.schema import PatientProfile


def rewrite_query(profile: PatientProfile) -> List[str]:
    """Create retrieval-friendly queries from a structured patient profile."""
    queries: List[str] = []

    base_parts = [p for p in [profile.cancer_type, profile.stage] if p]
    if base_parts:
        queries.append(" ".join(base_parts))

    if profile.biomarkers:
        queries.append(" ".join(base_parts + profile.biomarkers))

    if profile.prior_treatments:
        queries.append(" ".join(base_parts + profile.prior_treatments))

    if not queries:
        queries.append(profile.free_text_summary)

    return list(dict.fromkeys(queries))
