from __future__ import annotations

import re
from trialmatch.schema import PatientProfile


CANCER_KEYWORDS = [
    "endometrial cancer",
    "breast cancer",
    "colon cancer",
    "lung cancer",
]


def extract_patient_profile(raw_text: str) -> PatientProfile:
    """Rule-based placeholder for structured extraction.

    Replace this with a real LLM client that returns strict JSON.
    """
    lower = raw_text.lower()
    age_match = re.search(r"(\d{2})\s*-?year-old", lower)
    ecog_match = re.search(r"ecog\s*(\d)", lower)

    cancer_type = next((k.title() for k in CANCER_KEYWORDS if k in lower), None)
    sex = "female" if any(t in lower for t in ["female", "woman"]) else None

    biomarkers = []
    for marker in ["hr+", "her2-", "dmmr", "msi-h", "p53"]:
        if marker in lower:
            biomarkers.append(marker)

    return PatientProfile(
        age=int(age_match.group(1)) if age_match else None,
        sex=sex,
        cancer_type=cancer_type,
        stage="advanced" if "advanced" in lower else None,
        biomarkers=biomarkers,
        prior_treatments=["chemotherapy"] if "chemotherapy" in lower else [],
        ecog=int(ecog_match.group(1)) if ecog_match else None,
        free_text_summary=raw_text,
    )
