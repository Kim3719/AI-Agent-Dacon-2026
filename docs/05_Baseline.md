# 베이스라인

## 목적

재현 가능한 첫 모델을 만들고, 학습부터 제출 파일 생성까지 전체 흐름을 확인합니다.

## 이 문서는 무엇인가

첫 번째 기준 모델을 어떻게 만들지 정리하는 문서입니다. 여기서 말하는 baseline은 높은 점수를 내는 최종 모델이 아니라, 데이터 로딩부터 제출 파일 생성까지 전체 파이프라인이 연결되는지 확인하기 위한 출발점입니다.

아직 baseline 코드는 구현하지 않았습니다. 아래 명령어와 표는 앞으로 구현할 기준 구조입니다.

## 베이스라인 입력

- `current_prompt`
- `history`
- `session_meta`
- `workspace`

## 후보 접근법

| 접근법 | 상태 | 비고 |
| --- | --- | --- |
| 최빈 클래스 baseline | 예정 | sanity check |
| TF-IDF + Logistic Regression | 예정 | 빠르고 강한 기본선 |
| TF-IDF + LightGBM | 예정 | sparse/text-derived feature 활용 |
| Sentence embedding + classifier | 예정 | 의미 기반 표현 활용 |

## 검증 설정

TBD

기록할 항목:

- Split 전략
- Random seed
- Metric
- Class balance 처리 방식
- 전처리 단계

## 재현 명령

```bash
pip install -r requirements.txt
python -m src.training.train_baseline
python -m src.inference.predict
```

위 명령은 예정이며, 실제 코드 구현 후 변경될 수 있습니다.

## 결과

| 모델 | Validation Score | Public Score | 비고 |
| --- | ---: | ---: | --- |
| TBD | TBD | TBD | TBD |
