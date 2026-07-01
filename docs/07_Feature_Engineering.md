# Feature Engineering

## Objective

Track candidate features and their measured impact.

## Feature Groups

| Group | Examples | Status |
| --- | --- | --- |
| Prompt text | TF-IDF, embeddings, length, keywords | Planned |
| History actions | Last action, action counts, sequence n-grams | Planned |
| History text | Previous user intents, result summaries | Planned |
| Session metadata | Token budget, turn index, elapsed time | Planned |
| Workspace metadata | Language mix, LOC, git dirty, CI status | Planned |

## Candidate Features

- [ ] `current_prompt` length
- [ ] `current_prompt` language markers
- [ ] Last assistant action
- [ ] Count of previous actions by class
- [ ] History length
- [ ] Workspace language top-1
- [ ] `budget_tokens_remaining` buckets
- [ ] `last_ci_status`
- [ ] `git_dirty`

## Experiment Tracking

| Feature Set | Experiment | Validation Score | Notes |
| --- | --- | ---: | --- |
| TBD | TBD | TBD | TBD |

## Notebook

- [Feature Engineering Notebook](../notebooks/Feature_Engineering.ipynb)
