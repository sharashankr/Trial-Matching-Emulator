from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
from trialmatch.schema import RetrievalResult, TrialDocument


class BaseRetriever(ABC):
    @abstractmethod
    def fit(self, trials: List[TrialDocument]) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        raise NotImplementedError
