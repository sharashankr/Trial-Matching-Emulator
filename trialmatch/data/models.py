from dataclasses import dataclass


@dataclass
class TrialRecord:
    trial_id: str
    title: str
    condition: str
    summary: str
    inclusion_criteria: str
    exclusion_criteria: str
