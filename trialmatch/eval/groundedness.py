from __future__ import annotations

from trialmatch.schema import EligibilityAssessment


def simple_groundedness_score(assessment: EligibilityAssessment) -> float:
    if not assessment.supporting_evidence:
        return 0.0
    return min(1.0, 0.25 * len(assessment.supporting_evidence))
