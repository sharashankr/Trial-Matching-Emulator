from __future__ import annotations

from trialmatch.schema import EligibilityAssessment, PatientProfile, TrialDocument


def assess_eligibility(profile: PatientProfile, trial: TrialDocument) -> EligibilityAssessment:
    """Simple grounded heuristic. Replace with real evidence-grounded LLM reasoning."""
    evidence = []
    label = "possible_match"

    if profile.cancer_type and profile.cancer_type.lower() in trial.condition.lower():
        evidence.append(f"Condition match: {trial.condition}")
    else:
        label = "unlikely_match"

    if profile.ecog is not None and profile.ecog <= 1 and "ECOG 0-1" in trial.inclusion_criteria:
        evidence.append("Performance status likely compatible")

    rationale = (
        "Patient appears broadly aligned with the trial condition and at least some criteria."
        if label == "possible_match"
        else "Cancer type or key trial condition appears mismatched."
    )

    return EligibilityAssessment(
        trial_id=trial.trial_id,
        label=label,
        rationale=rationale,
        supporting_evidence=evidence,
    )
