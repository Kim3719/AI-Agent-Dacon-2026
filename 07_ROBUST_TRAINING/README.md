# Step 07. Label noise에 덜 흔들리게 학습할 수 있는가?

## 어떤 문제가 있었는가

후처리, Teacher 교체, 구조 복잡화가 안정적인 개선을 만들지 못했습니다. 취약 클래스의 낮은 margin과 반복되는 혼동은 경계 근처 표본에 모델이 과도하게 맞춰질 가능성을 보여줬습니다.

## 왜 이 방법을 선택했는가

모델 용량 대신 학습 레시피를 개선하는 축이 상대적으로 덜 탐색되어 있었습니다. 텍스트 임베딩에 작은 적대적 perturbation을 적용하는 연구를 참고해 FGM을 선택하고, 사전학습 하위 레이어를 천천히 조정하기 위해 LLRD를 결합했습니다.

## 어떻게 적용했는가

- 기본 loss를 계산해 backward했습니다.
- 임베딩 파라미터에 gradient 방향 perturbation을 추가했습니다.
- perturbed embedding에서 두 번째 loss를 backward했습니다.
- 원래 파라미터로 복구한 뒤 optimizer step을 수행했습니다.
- 아래쪽 Transformer 레이어로 갈수록 학습률을 `0.95`씩 줄였습니다.
- KD Student 학습에 `FGM eps=1.0`을 결합했습니다.

원 논문은 텍스트 임베딩 공간의 adversarial perturbation이라는 근거를 제공했고, 이 프로젝트에서는 이를 XLM-R 기반 KD 학습에 맞게 직접 통합했습니다.

## 결과가 어땠는가

- KD + FGM + LLRD Validation: 약 `0.7723`
- 이전 Distillation 대비: 약 `+0.0067`
- Large Teacher `0.7691`도 상회
- 단일 Public: `0.7745`
- `eps=1.5`: 약 `0.7709`로 하락

## 왜 성공하거나 실패했는가

`eps=1.0`은 작은 입력 변화에 대한 민감도를 줄이는 데 도움이 된 것으로 해석했습니다. `eps=1.5`는 perturbation이 지나쳐 원래 분포의 유용한 신호까지 흐렸을 가능성이 있습니다. 이는 현재 실험에 대한 해석이며 FGM의 보편적 우수성을 주장하지 않습니다.

## 다음에는 어떻게 활용할 것인가

- 여러 Seed에서 효과 크기와 분산을 확인합니다.
- FGM, LLRD, KD를 각각 제거하는 ablation을 수행합니다.
- annotator agreement와 clean subset을 만들어 label noise 가설을 직접 검증합니다.
- Generalized Cross Entropy, Co-teaching 등 noise-robust 방법과 비교합니다.
- 강건성과 calibration, OOD 성능을 함께 측정합니다.
