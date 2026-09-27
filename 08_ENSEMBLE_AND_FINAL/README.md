# Step 08. 서로 다르게 틀리는 모델을 어떻게 결합했는가?

## 어떤 문제가 있었는가

성능이 높은 모델끼리 결합해도 같은 샘플에서 함께 틀리면 Ensemble 이득이 작았습니다. 반대로 단일 점수가 조금 낮은 모델이 다른 오류를 만들면 조합에는 더 유용할 수 있었습니다.

## 왜 이 방법을 선택했는가

Seed만 바꾸는 방식보다 입력 표현과 학습 레시피가 다른 모델을 결합해 오류 상관을 낮추려 했습니다.

## 어떻게 적용했는가

- v3 KD+FGM 모델
- 최근 상태를 앞에 배치한 v3b FGM 모델
- Action을 special token으로 표현한 struct Student
- 후보 풀의 조합과 가중치를 탐색하되 Random/Group dual split으로 확인
- 제한적으로 검증된 ID lookup 적용

## 결과가 어땠는가

최종 구성은 다음과 같습니다.

```text
base_distill_v4_fgm        0.2
v3b_fgm_s42                0.1
struct_s123                0.7
+ id lookup
```

최종 Public Macro-F1은 **`0.7776644`**였습니다.

## 왜 성공하거나 실패했는가

구성원들은 가장 높은 단일 점수 순으로 선택된 것이 아니라 다른 입력 표현으로 서로 다른 오류를 만들었기 때문에 선택됐습니다. 다만 Validation에서 관찰된 가중치 이득 대부분이 Public에서는 줄어들어, Ensemble weight search도 Validation에 과적합될 수 있음을 확인했습니다.

## 다음에는 어떻게 활용할 것인가

다음 프로젝트에서는 단일 점수 외에 prediction disagreement, error overlap, pairwise correlation을 Registry에 기록합니다. 가중치는 nested validation 또는 독립 Holdout에서만 결정하고, 조합 수가 많을수록 선택 편향을 별도로 추정합니다.

## 결과 해석 시 주의

초기 `0.6XXX`는 초기 Public 제출, `0.7412`는 정리된 Baseline Validation, `0.7776644`는 최종 Public 결과입니다. 서로 다른 평가 구간의 수치를 동일 조건의 절대 향상으로 계산하지 않습니다.
