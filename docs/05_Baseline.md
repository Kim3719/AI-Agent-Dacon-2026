# Baseline

## Objective

Track the baseline approach and establish a reproducible starting point.

## Baseline Inputs

- `current_prompt`
- `history`
- `session_meta`
- `workspace`

## Baseline Candidates

| Approach | Status | Notes |
| --- | --- | --- |
| Majority class baseline | Planned | Sanity check |
| TF-IDF + Logistic Regression | Planned | Strong lightweight baseline |
| TF-IDF + LightGBM | Planned | Handles sparse/text-derived features |
| Sentence embeddings + classifier | Planned | Semantic prompt/history representation |

## Validation Setup

TBD

Recommended fields to record:

- Split strategy
- Random seed
- Metric
- Class balance handling
- Preprocessing steps

## Reproduction Steps

```bash
pip install -r requirements.txt
python -m src.training.train_baseline
python -m src.inference.predict
```

Commands are planned and may change when source code is implemented.

## Results

| Model | Validation Score | Public Score | Notes |
| --- | ---: | ---: | --- |
| TBD | TBD | TBD | TBD |
