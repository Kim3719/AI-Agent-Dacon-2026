# scripts 폴더

팀원이 명령어로 실행할 파일을 모아두는 곳입니다.

`scripts/`는 사람이 직접 실행하는 진입점입니다.

나중에 코드가 커지면 공통 로직을 별도 모듈로 분리할 수 있지만, 지금은 팀원이 이해하기 쉬운 실행 파일부터 둡니다.

현재 파일들은 아직 실제 모델 학습 코드를 완성한 것이 아니라, 앞으로 구현할 기준 틀입니다.

## 파일 설명

| 파일 | 역할 |
| --- | --- |
| `run_train.py` | 설정 파일을 받아 모델 학습을 실행하는 진입점 |
| `run_predict.py` | 학습된 모델로 예측을 실행하는 진입점 |
| `make_submission.py` | 예측 결과를 DACON 제출 형식으로 만드는 진입점 |
| `register_experiment.py` | 실험 결과를 `experiments/experiment_log.csv`에 추가하는 도구 |

## 사용 예시

```bash
python scripts/run_train.py --config configs/exp_template.yaml
python scripts/run_predict.py --config configs/exp_template.yaml
python scripts/make_submission.py --config configs/exp_template.yaml
```
