# Competition Analysis

## Summary

This document tracks competition rules, evaluation assumptions, submission format, and important constraints.

## Problem Type

- Type: Multi-class classification
- Number of classes: 14
- Training size: 70,000 samples
- Public test file: 5 format-check samples
- Private evaluation size: 30,000 samples

## Data Files

| File | Purpose | Status |
| --- | --- | --- |
| `data/train.jsonl` | Training input | Provided externally |
| `data/train_labels.csv` | Training labels | Provided externally |
| `data/test.jsonl` | Public format sample | Provided externally |
| `data/sample_submission.csv` | Submission format | Provided externally |
| `baseline_submit.zip` | Baseline submission reference | Provided externally |

## Evaluation

TBD after confirming the official metric from the competition page.

## Submission Format

```csv
id,action
sample_id,respond_only
```

The `action` value must exactly match one of the 14 class names.

## Rules Checklist

- [ ] Confirm final evaluation metric
- [ ] Confirm allowed external data and pretrained models
- [ ] Confirm submission packaging requirements
- [ ] Confirm daily submission limit
- [ ] Confirm team and code sharing rules

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Private test distribution shift | Lower leaderboard score | Use robust validation splits |
| Overfitting prompt templates | Weak generalization | Review errors by session pattern |
| Class imbalance | Poor minority-class recall | Weighted loss or sampling |

## References

- [Competition Rules](https://dacon.io/competitions/official/236694/overview/rules)
- [Competition Description](https://dacon.io/competitions/official/236694/overview/description)
