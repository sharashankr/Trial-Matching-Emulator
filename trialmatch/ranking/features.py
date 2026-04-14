from __future__ import annotations

from typing import Dict
from trialmatch.schema import PatientProfile, TrialDocument


def build_pair_features(profile: PatientProfile, trial: TrialDocument, retrieval_score: float) -> Dict[str, float]:
    text = f"{trial.title} {trial.condition} {trial.summary}".lower()
    cancer_match = 1.0 if profile.cancer_type and profile.cancer_type.lower() in text else 0.0
    biomarker_match = 0.0
    if profile.biomarkers:
        biomarker_match = float(any(b.lower() in text for b in profile.biomarkers))

    return {
        "retrieval_score": float(retrieval_score),
        "cancer_match": cancer_match,
        "biomarker_match": biomarker_match,
    }
