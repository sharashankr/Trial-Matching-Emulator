from __future__ import annotations

from typing import Iterable, Set


def recall_at_k(retrieved_ids: Iterable[str], relevant_ids: Set[str], k: int) -> float:
    top_k = list(retrieved_ids)[:k]
    if not relevant_ids:
        return 0.0
    return len(set(top_k) & relevant_ids) / len(relevant_ids)


def hit_at_k(retrieved_ids: Iterable[str], relevant_ids: Set[str], k: int) -> float:
    top_k = list(retrieved_ids)[:k]
    return 1.0 if set(top_k) & relevant_ids else 0.0
