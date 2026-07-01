# src/models 폴더 안내

이 폴더는 모델 정의 또는 모델 wrapper 코드를 작성하는 위치입니다.

## 현재 상태

아직 실제 모델 코드는 없습니다.

## 앞으로 작성할 내용

- scikit-learn baseline model wrapper
- LightGBM / XGBoost / CatBoost 모델 설정
- Transformer 기반 classifier wrapper
- 모델 저장 및 로딩 인터페이스

## 사용 원칙

- 학습 실행 로직은 `src/training/`에 둡니다.
- 모델 구조 또는 모델 생성 함수는 이 폴더에 둡니다.
- 어떤 모델을 사용했는지는 `experiments/` 문서에 반드시 기록합니다.
