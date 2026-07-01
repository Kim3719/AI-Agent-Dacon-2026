# 모델 최적화

## 목적

모델 선택, 튜닝 전략, 성능과 비용의 trade-off를 기록합니다.

## 이 문서는 무엇인가

여러 모델 후보를 비교하고 최종적으로 어떤 모델을 선택할지 판단하기 위한 문서입니다. 점수뿐 아니라 학습 시간, 추론 비용, 구현 복잡도, 오류 개선 여부를 함께 기록합니다.

아직 모델 최적화 실험은 진행하지 않았습니다. baseline 이후 후보 모델을 하나씩 비교하면서 채웁니다.

## 후보 모델

| 모델 | 장점 | 리스크 | 상태 |
| --- | --- | --- | --- |
| Logistic Regression | 빠르고 해석 가능 | 비선형 상호작용 한계 | 예정 |
| LightGBM | tabular feature에 강함 | text feature 처리 설계 필요 | 예정 |
| XGBoost / CatBoost | 강한 baseline 후보 | 학습 비용 증가 | 예정 |
| Transformer classifier | 텍스트 이해력 우수 | compute cost와 overfitting 리스크 | 예정 |
| Ensemble | 안정성 개선 가능 | 복잡도 증가 | 예정 |

## 튜닝 계획

- [ ] 기준 validation split 확정
- [ ] 텍스트 표현 방식 튜닝
- [ ] class weight 튜닝
- [ ] 모델 hyperparameter 튜닝
- [ ] 추론 비용 비교
- [ ] 오류 분석 기반 재검증

## 추적 표

| Run | Model | Features | Validation Score | Public Score | 결정 |
| --- | --- | --- | ---: | ---: | --- |
| TBD | TBD | TBD | TBD | TBD | TBD |

## 최종 모델 선택

TBD
