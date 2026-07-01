# 오류 분석

## 목적

모델의 실패 사례를 이해하고 다음 개선 작업으로 연결합니다.

## 이 문서는 무엇인가

모델 예측 결과가 나온 뒤, 어떤 action을 자주 혼동하는지 정리하는 문서입니다. 단순 점수 비교만으로는 다음 개선 방향을 잡기 어렵기 때문에, class별 오답 유형을 기록하는 용도로 사용합니다.

아직 모델 예측 결과가 없으므로 실제 오류 사례는 없습니다. 첫 validation prediction 이후 채웁니다.

## 오류 분석 체크리스트

- [ ] action class별 confusion matrix
- [ ] 가장 흔한 false positive
- [ ] 가장 흔한 false negative
- [ ] high-confidence 오답
- [ ] `turn_index`별 오류 패턴
- [ ] `language_pref`별 오류 패턴
- [ ] history 길이별 오류 패턴

## Confusion Matrix

![Confusion matrix placeholder](../results/figures/confusion_matrix.svg)

## 오류 유형

| 유형 | 설명 | 예시 | 다음 작업 |
| --- | --- | --- | --- |
| 검색 vs 읽기 | 탐색과 파일 확인을 혼동 | TBD | history/workspace feature 추가 |
| edit vs patch | 수정 방식 구분 실패 | TBD | label 기준과 history context 점검 |
| ask vs plan | 질문과 계획 수립을 혼동 | TBD | prompt intent feature 강화 |

## 발견 사항

TBD

## 노트북

- [오류 분석 노트북](../notebooks/Error_Analysis.ipynb)
