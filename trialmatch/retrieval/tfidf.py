from __future__ import annotations

from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from trialmatch.retrieval.base import BaseRetriever
from trialmatch.schema import RetrievalResult, TrialDocument


class TfidfTrialRetriever(BaseRetriever):
    def __init__(self) -> None:
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.trials: List[TrialDocument] = []
        self.matrix = None

    def fit(self, trials: List[TrialDocument]) -> None:
        self.trials = trials
        corpus = [
            " ".join([
                t.title,
                t.condition,
                t.summary,
                t.inclusion_criteria,
                t.exclusion_criteria,
            ])
            for t in trials
        ]
        self.matrix = self.vectorizer.fit_transform(corpus)

    def search(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        if self.matrix is None:
            raise RuntimeError("Retriever must be fit before search.")

        query_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(query_vec, self.matrix).flatten()
        top_idx = np.argsort(-sims)[:top_k]

        return [
            RetrievalResult(trial=self.trials[i], score=float(sims[i]), query_used=query)
            for i in top_idx
        ]
