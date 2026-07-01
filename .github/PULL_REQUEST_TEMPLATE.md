# Pull Request

아래 항목은 팀원이 변경 내용을 빠르게 이해하기 위한 최소 양식입니다.

길게 쓰지 않아도 됩니다. 직접 적어도 되고, AI에게 변경사항을 요약시켜 붙여넣어도 됩니다.

## 1. 변경 요약

<!--
예시:
- 데이터 로딩 함수 초안 추가
- EXP001 baseline 설정 파일 추가
- submission 생성 스크립트 수정
-->

-

## 2. 왜 바꿨나요?

<!--
이 변경이 필요한 이유를 적습니다.
모르면 "실험을 위해 추가", "팀 실행 편의를 위해 수정"처럼 간단히 적어도 됩니다.
-->

-

## 3. 실험 / 성능 결과

실험이 없으면 `해당 없음`이라고 적습니다.

| 항목 | 값 |
| --- | --- |
| Experiment ID | TBD |
| Model | TBD |
| Validation F1 | TBD |
| Accuracy | TBD |
| Public Score | TBD |

## 4. 실행 방법

<!--
팀원이 같은 결과를 확인하려면 어떤 명령을 실행해야 하는지 적습니다.
아직 실행 스크립트가 없으면 "해당 없음"이라고 적습니다.
-->

```bash
# 예시
python scripts/run_train.py --config configs/exp_template.yaml
```

## 5. AI 요약 붙여넣기

<!--
선택 항목입니다.
ChatGPT, Claude, Copilot 등에게 변경사항을 요약시킨 경우 여기에 붙여넣습니다.
팀원들이 빠르게 읽는 용도입니다.
-->

해당 없음

## 6. 체크리스트

- [ ] main 브랜치에 직접 push하지 않았습니다.
- [ ] 불필요한 대용량 파일을 올리지 않았습니다.
- [ ] 변경 내용을 위에 요약했습니다.
- [ ] 실험 결과가 있다면 `experiments/experiment_log.csv`에 기록했습니다.
- [ ] 제출 결과가 있다면 `submissions/submission_log.csv`에 기록했습니다.
