from __future__ import annotations

from typing import Dict, List
from trialmatch.data.loader import load_sample_trials
from trialmatch.llm.extractor import extract_patient_profile
from trialmatch.llm.rewriter import rewrite_query
from trialmatch.llm.reasoner import assess_eligibility
from trialmatch.ranking.reranker import SimpleReranker
from trialmatch.retrieval.tfidf import TfidfTrialRetriever
from trialmatch.schema import TrialDocument


class TrialMatchingPipeline:
    def __init__(self, top_k: int = 5) -> None:
        self.top_k = top_k
        self.retriever = TfidfTrialRetriever()
        self.reranker = SimpleReranker()
        self.trials = self._load_trials()
        self.retriever.fit(self.trials)

    def _load_trials(self) -> List[TrialDocument]:
        raw_trials = load_sample_trials()
        return [TrialDocument(**vars(t)) for t in raw_trials]

    def run(self, raw_patient_summary: str) -> Dict:
        profile = extract_patient_profile(raw_patient_summary)
        queries = rewrite_query(profile)

        pooled = {}
        for q in queries:
            for result in self.retriever.search(q, top_k=self.top_k):
                current = pooled.get(result.trial.trial_id)
                if current is None or result.score > current.score:
                    pooled[result.trial.trial_id] = result

        ranked = self.reranker.rerank(profile, pooled.values())
        assessments = [assess_eligibility(profile, r.trial) for r in ranked[: self.top_k]]

        return {
            "profile": profile.model_dump(),
            "queries": queries,
            "ranked_trials": [r.model_dump() for r in ranked[: self.top_k]],
            "assessments": [a.model_dump() for a in assessments],
        }
