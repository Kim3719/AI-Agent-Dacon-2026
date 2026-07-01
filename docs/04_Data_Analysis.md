# Data Analysis

## Objective

Document dataset structure, distributions, and early insights.

## Dataset Schema

### `train.jsonl` and `test.jsonl`

| Field | Description | Example / Notes |
| --- | --- | --- |
| `id` | Sample identifier | `sess_sim_...-step_02` |
| `session_meta` | Session and workspace metadata | User tier, language, budget, workspace |
| `history` | Previous user and assistant actions | 0 to 12 turns |
| `current_prompt` | Latest user message | Prediction target context |

### `train_labels.csv`

| Field | Description |
| --- | --- |
| `id` | Sample identifier |
| `action` | One of 14 target classes |

## Analysis Plan

- [ ] Load JSONL and labels
- [ ] Validate ID alignment
- [ ] Check missing values
- [ ] Plot target distribution
- [ ] Analyze prompt length and history length
- [ ] Analyze metadata by target action
- [ ] Save figures to `results/figures/`

## Figures

Planned figure slots:

![Action distribution placeholder](../results/figures/action_distribution.png)

![History length placeholder](../results/figures/history_length_by_action.png)

## Initial Findings

TBD

## Notebook

- [EDA Notebook](../notebooks/EDA.ipynb)
