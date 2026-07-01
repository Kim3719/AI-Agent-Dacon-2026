# notebooks 폴더 안내

이 폴더는 빠른 분석과 실험 검증을 위한 Jupyter Notebook 작업 공간입니다.

## 노트북 목록

| 파일 | 목적 | 현재 상태 |
| --- | --- | --- |
| `EDA.ipynb` | 데이터 구조, 분포, 라벨 비율, 메타데이터 패턴을 확인합니다. | 템플릿 |
| `Error_Analysis.ipynb` | 모델 예측 결과가 생긴 뒤 오답 패턴과 confusion matrix를 분석합니다. | 템플릿 |
| `Feature_Engineering.ipynb` | 후보 피처를 만들고 간단한 성능 변화를 확인합니다. | 템플릿 |

## 사용 원칙

- 노트북은 탐색과 검증을 위한 공간입니다.
- 반복 사용되는 로직은 `src/`로 옮겨 재사용 가능하게 만듭니다.
- 생성한 그래프는 `results/figures/`에 저장하고 문서에서 링크합니다.
- 점수나 결론은 반드시 `experiments/`에도 함께 기록합니다.
