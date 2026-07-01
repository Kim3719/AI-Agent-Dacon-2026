# Model Optimization

## Objective

Document model selection, tuning strategy, and performance trade-offs.

## Candidate Models

| Model | Strength | Risk | Status |
| --- | --- | --- | --- |
| Logistic Regression | Fast, interpretable | Limited nonlinear interaction | Planned |
| LightGBM | Strong tabular features | Requires careful text handling | Planned |
| XGBoost / CatBoost | Robust baselines | Training cost | Planned |
| Transformer classifier | Strong text understanding | Higher compute and overfitting risk | Planned |
| Ensemble | Better robustness | More complexity | Planned |

## Tuning Plan

- [ ] Establish baseline split
- [ ] Tune text representation
- [ ] Tune class weights
- [ ] Tune model hyperparameters
- [ ] Compare inference cost
- [ ] Validate with error analysis

## Tracking Table

| Run | Model | Features | Validation Score | Public Score | Decision |
| --- | --- | --- | ---: | ---: | --- |
| TBD | TBD | TBD | TBD | TBD | TBD |

## Final Model Selection

TBD
