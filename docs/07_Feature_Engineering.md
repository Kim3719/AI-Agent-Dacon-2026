# 피처 엔지니어링

## 목적

후보 피처와 실제 성능 영향을 기록합니다.

## 이 문서는 무엇인가

모델에 어떤 정보를 넣을지 설계하고, 각 피처가 성능에 어떤 영향을 주었는지 기록하는 문서입니다.

현재는 후보 피처 목록만 정리되어 있습니다. 실제 실험 결과는 `experiments/`의 실험 기록과 연결해서 업데이트합니다.

## 피처 그룹

| 그룹 | 예시 | 상태 |
| --- | --- | --- |
| 프롬프트 텍스트 | TF-IDF, embedding, 길이, 키워드 | 예정 |
| History action | 마지막 action, action count, sequence n-gram | 예정 |
| History text | 이전 사용자 의도, result summary | 예정 |
| Session metadata | 토큰 예산, 턴 번호, 경과 시간 | 예정 |
| Workspace metadata | 언어 비율, LOC, git dirty, CI status | 예정 |

## 후보 피처

- [ ] `current_prompt` 길이
- [ ] `current_prompt` 언어 단서
- [ ] 마지막 assistant action
- [ ] 이전 action class별 count
- [ ] history 길이
- [ ] workspace 주요 언어
- [ ] `budget_tokens_remaining` 구간화
- [ ] `last_ci_status`
- [ ] `git_dirty`

## 실험 추적

| Feature Set | Experiment | Validation Score | 비고 |
| --- | --- | ---: | --- |
| TBD | TBD | TBD | TBD |

## 노트북

- [Feature Engineering 노트북](../notebooks/Feature_Engineering.ipynb)
