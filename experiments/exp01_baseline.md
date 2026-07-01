# exp01_baseline

## 실험 상태

- 상태: 예정
- 담당자: TBD
- 작성일: TBD

## 이 파일은 무엇인가

첫 번째 베이스라인 실험을 기록하기 위한 템플릿입니다.

아직 실험은 진행하지 않았습니다. 향후 가장 단순한 모델부터 학습해보고, 데이터 로딩부터 제출 파일 생성까지 전체 파이프라인이 정상적으로 동작하는지 확인한 뒤 이 문서를 채웁니다.

## 실험 목적

- 데이터 로딩 코드가 정상적으로 동작하는지 확인합니다.
- 학습 데이터와 라벨이 올바르게 연결되는지 확인합니다.
- 첫 validation split을 만들고 기준 점수를 확보합니다.
- 이후 실험과 비교할 baseline score를 기록합니다.

## 가설

TBD

예시:

- `current_prompt`만 사용해도 일부 action은 구분 가능할 것이다.
- history action 정보를 추가하면 `run_tests`, `lint_or_typecheck`, `respond_only` 구분이 개선될 수 있다.

## 변경 사항

아직 없음.

향후 기록 예시:

- TF-IDF 기반 텍스트 피처 추가
- Logistic Regression 모델 사용
- Stratified validation split 적용

## 데이터 / Split

| 항목 | 값 |
| --- | --- |
| Train data | TBD |
| Validation split | TBD |
| Random seed | TBD |
| Metric | TBD |

## 모델 설정

| 항목 | 값 |
| --- | --- |
| 알고리즘 | TBD |
| 텍스트 표현 | TBD |
| 메타데이터 피처 | TBD |
| 클래스 불균형 처리 | TBD |

## Validation Score

TBD

## Public Score

TBD

## 결과 요약

TBD

## 배운 점

TBD

## 다음 작업

- [ ] 데이터 로딩 코드 구현
- [ ] 공식 metric 확인
- [ ] 첫 validation split 결정
- [ ] baseline 모델 학습
- [ ] submission 파일 생성

## 관련 산출물

- 노트북: [EDA](../notebooks/EDA.ipynb)
- 그래프: [results/figures](../results/figures/)
- 제출 파일: [results/submissions](../results/submissions/)
