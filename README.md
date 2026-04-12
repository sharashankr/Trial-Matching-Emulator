# Cohere-Style Clinical Trial Matching Starter

A lightweight Python starter repo for a **clinical trial matching pipeline** that is strong enough to discuss in interviews and easy to extend into a real GitHub project.

## What this is

This is a **starter scaffold**, not a finished research claim. It gives you a clean structure for:

- structured patient-profile extraction
- multi-query retrieval
- optional neural reranking
- grounded eligibility reasoning
- offline evaluation

## Why this is better than a generic chatbot repo

This repo is organized around measurable ML components:

1. **profile extraction** from free-text patient summaries
2. **query rewriting** for retrieval
3. **candidate retrieval** over trials
4. **reranking** with room for a trained model
5. **grounded reasoning** tied to evidence
6. **evaluation** with retrieval + grounding metrics

That makes it much easier to discuss as:

> Built a modular clinical trial matching pipeline that converts patient summaries into structured features, retrieves candidate studies, reranks them, and generates evidence-grounded eligibility assessments with offline evaluation.

## Suggested talking track for Cohere

Use this only after you actually implement and test the pieces.

- Built a modular LLM-assisted retrieval and ranking pipeline for clinical trial matching
- Designed separate components for extraction, retrieval, reranking, reasoning, and evaluation
- Structured the system so retrieval quality, latency, and groundedness can be benchmarked independently
- Left room for a learned reranker and small-model fine-tuning rather than relying only on prompt orchestration

## Project structure

```text
cohere_trial_matcher/
├── configs/
│   └── default.yaml
├── scripts/
│   ├── run_pipeline.py
│   └── train_reranker.py
├── tests/
│   └── test_schema.py
├── trialmatch/
│   ├── __init__.py
│   ├── schema.py
│   ├── pipeline.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── loader.py
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── extractor.py
│   │   ├── rewriter.py
│   │   └── reasoner.py
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── tfidf.py
│   ├── ranking/
│   │   ├── __init__.py
│   │   ├── features.py
│   │   ├── reranker.py
│   │   └── train.py
│   ├── eval/
│   │   ├── __init__.py
│   │   ├── groundedness.py
│   │   └── retrieval_metrics.py
│   └── utils/
│       ├── __init__.py
│       └── io.py
└── pyproject.toml
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python scripts/run_pipeline.py
```

## What to implement next

### High priority
- replace placeholder extractor with a real structured-extraction client
- replace query rewriter stub with a real prompt + JSON output
- wire in ClinicalTrials.gov data ingestion
- add a true embedding retriever or BM25 baseline
- train a reranker on relevance labels

### Medium priority
- add evidence span highlighting
- add latency instrumentation
- add better groundedness checks

### Low priority
- dashboard
- cloud deployment

## Important warning

Do **not** claim performance improvements you have not actually measured.
Use this scaffold as a clean starting point, then earn the metrics.
