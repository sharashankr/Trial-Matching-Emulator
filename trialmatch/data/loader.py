from __future__ import annotations

from typing import List
from trialmatch.data.models import TrialRecord


SAMPLE_TRIALS = [
    TrialRecord(
        trial_id="NCT-DEMO-001",
        title="Pembrolizumab in Advanced Endometrial Cancer",
        condition="Endometrial Cancer",
        summary="Phase III study of immunotherapy plus chemotherapy.",
        inclusion_criteria="Advanced or recurrent endometrial cancer; ECOG 0-1; measurable disease.",
        exclusion_criteria="Prior checkpoint inhibitor therapy may exclude some participants.",
    ),
    TrialRecord(
        trial_id="NCT-DEMO-002",
        title="Targeted Therapy in HR+/HER2- Breast Cancer",
        condition="Breast Cancer",
        summary="Study of targeted therapy in metastatic HR+/HER2- disease.",
        inclusion_criteria="HR positive, HER2 negative metastatic breast cancer; prior endocrine therapy allowed.",
        exclusion_criteria="Uncontrolled CNS metastases.",
    ),
    TrialRecord(
        trial_id="NCT-DEMO-003",
        title="Adjuvant Chemotherapy in Stage II Colon Cancer",
        condition="Colon Cancer",
        summary="Trial evaluating adjuvant chemotherapy strategies.",
        inclusion_criteria="Resected stage II colon adenocarcinoma.",
        exclusion_criteria="Prior systemic therapy for colon cancer.",
    ),
]


def load_sample_trials() -> List[TrialRecord]:
    return SAMPLE_TRIALS.copy()
