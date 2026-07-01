# src 폴더 안내

이 폴더는 대회 코드가 들어가는 공간입니다.

현재는 실제 모델이 구현된 상태가 아니라, 앞으로 코드를 작성할 위치와 역할을 정리한 초기 뼈대입니다.

## 구조

| 경로 | 역할 |
| --- | --- |
| `src/data/` | JSONL/CSV 로딩, 데이터 검증, train-label 병합 |
| `src/features/` | 텍스트, history, metadata 기반 피처 생성 |
| `src/models/` | 모델 정의 또는 모델 wrapper |
| `src/training/` | 학습 스크립트와 validation split 관리 |
| `src/inference/` | test 예측과 submission 생성 |
| `src/evaluation/` | metric, confusion matrix, error report |
| `src/utils/` | 설정 로딩, seed 고정, 공통 유틸 |

## 작성 원칙

- 노트북에서 검증한 코드를 이곳으로 옮깁니다.
- 입력과 출력 경로는 가능하면 `configs/default.yaml`에서 관리합니다.
- 실험마다 변경된 내용은 `experiments/`에 기록합니다.
