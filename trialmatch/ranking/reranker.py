from __future__ import annotations

from typing import Iterable, List
from trialmatch.ranking.features import build_pair_features
from trialmatch.schema import PatientProfile, RankedTrial, RetrievalResult


class SimpleReranker:
    """Heuristic reranker placeholder.

    Replace with a trained cross-encoder or learning-to-rank model.
    """

    def rerank(self, profile: PatientProfile, candidates: Iterable[RetrievalResult]) -> List[RankedTrial]:
        ranked: List[RankedTrial] = []
        for cand in candidates:
            feats = build_pair_features(profile, cand.trial, cand.score)
            rerank_score = (
                0.6 * feats["retrieval_score"]
                + 0.3 * feats["cancer_match"]
                + 0.1 * feats["biomarker_match"]
            )
            ranked.append(
                RankedTrial(
                    trial=cand.trial,
                    retrieval_score=cand.score,
                    rerank_score=rerank_score,
                    final_score=rerank_score,
                )
            )
        return sorted(ranked, key=lambda x: x.final_score, reverse=True)
