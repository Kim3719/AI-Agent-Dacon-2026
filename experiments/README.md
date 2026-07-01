# experiments 폴더

실험 결과를 한곳에서 보기 위한 폴더입니다.

이전처럼 팀원이 긴 실험 보고서를 매번 직접 작성할 필요는 없습니다.

대신 아래 두 가지만 지키면 됩니다.

1. 중요한 실험은 `experiment_log.csv`에 한 줄로 기록합니다.
2. PR에는 무엇을 바꿨는지 간단히 적거나 AI 요약을 붙입니다.

## 실험 번호 규칙

팀 공식 실험은 `EXP001`, `EXP002`, `EXP003`처럼 증가시킵니다.

개인 레포에서 혼자 해본 실험은 자유롭게 이름을 붙여도 됩니다.

Main Repository에 올릴 때만 공식 번호를 사용합니다.

## experiment_log.csv 컬럼 설명

| 컬럼 | 의미 |
| --- | --- |
| `experiment_id` | 실험 번호입니다. 예: `EXP001` |
| `date` | 실험 날짜입니다. |
| `owner` | 실험한 팀원 이름입니다. |
| `branch` | 작업 브랜치 이름입니다. |
| `model` | 사용한 모델입니다. |
| `features` | 사용한 주요 피처입니다. |
| `validation_f1` | 검증 F1 점수입니다. 없으면 `TBD` |
| `accuracy` | 검증 Accuracy입니다. 없으면 `TBD` |
| `public_score` | DACON Public Score입니다. 제출 전이면 `TBD` |
| `summary` | 실험 요약입니다. |
| `pr_url` | 관련 PR 링크입니다. |

## 기록 예시

```csv
EXP001,2026-07-02,HAK,experiment/EXP001-baseline,TF-IDF LR,current_prompt,TBD,TBD,TBD,첫 baseline 실험,TBD
```
