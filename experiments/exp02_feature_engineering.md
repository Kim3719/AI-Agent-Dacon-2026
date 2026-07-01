# exp02_feature_engineering

## 실험 상태

- 상태: 예정
- 담당자: TBD
- 작성일: TBD

## 이 파일은 무엇인가

피처 엔지니어링 실험을 기록하기 위한 템플릿입니다.

아직 피처 실험은 진행하지 않았습니다. baseline 이후 어떤 정보를 추가했을 때 성능이 좋아지거나 나빠지는지 기록하기 위해 사용합니다.

## 실험 목적

- `current_prompt` 외에 history, session metadata, workspace metadata가 성능에 주는 영향을 확인합니다.
- action class별로 어떤 피처가 도움이 되는지 분석합니다.
- 불필요하거나 과적합을 유발하는 피처를 제거합니다.

## 가설

TBD

예시:

- 이전 assistant action sequence는 다음 action 예측에 도움이 될 것이다.
- `last_ci_status`는 `run_tests` 또는 `lint_or_typecheck` 예측에 영향을 줄 수 있다.
- `budget_tokens_remaining`이 낮을수록 `respond_only` 비율이 높아질 수 있다.

## 변경 사항

아직 없음.

향후 기록 예시:

- history 길이 피처 추가
- 마지막 action class 피처 추가
- workspace language mix 피처 추가

## Feature Set

| Feature Group | 포함 여부 | 설명 |
| --- | --- | --- |
| Prompt text | TBD | 현재 사용자 발화 기반 피처 |
| History actions | TBD | 이전 action sequence 기반 피처 |
| Session metadata | TBD | 토큰 예산, turn index, elapsed time |
| Workspace metadata | TBD | 언어 비율, LOC, git dirty, CI status |

## 데이터 / Split

| 항목 | 값 |
| --- | --- |
| Train data | TBD |
| Validation split | TBD |
| Random seed | TBD |
| Metric | TBD |

## Validation Score

TBD

## Public Score

TBD

## 결과 요약

TBD

## 배운 점

TBD

## 다음 작업

- [ ] baseline 대비 개선 여부 확인
- [ ] class별 성능 변화 확인
- [ ] 오류 분석 문서에 주요 패턴 반영

## 관련 산출물

- 노트북: [Feature Engineering](../notebooks/Feature_Engineering.ipynb)
- 문서: [피처 엔지니어링](../docs/07_Feature_Engineering.md)
