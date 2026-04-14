from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


class PatientProfile(BaseModel):
    age: Optional[int] = None
    sex: Optional[str] = None
    cancer_type: Optional[str] = None
    stage: Optional[str] = None
    biomarkers: List[str] = Field(default_factory=list)
    prior_treatments: List[str] = Field(default_factory=list)
    ecog: Optional[int] = None
    comorbidities: List[str] = Field(default_factory=list)
    free_text_summary: str


class TrialDocument(BaseModel):
    trial_id: str
    title: str
    condition: str
    summary: str
    inclusion_criteria: str = ""
    exclusion_criteria: str = ""


class RetrievalResult(BaseModel):
    trial: TrialDocument
    score: float
    query_used: Optional[str] = None


class RankedTrial(BaseModel):
    trial: TrialDocument
    retrieval_score: float
    rerank_score: float
    final_score: float


class EligibilityAssessment(BaseModel):
    trial_id: str
    label: str
    rationale: str
    supporting_evidence: List[str] = Field(default_factory=list)
    groundedness_score: Optional[float] = None
