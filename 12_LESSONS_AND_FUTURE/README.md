# Step 12. 이 첫 대회가 다음 연구의 거름이 된 이유

이 문서는 프로젝트의 결론이자 다음 프로젝트의 시작점입니다. 최종 점수 `0.7776644`보다 중요한 결과는, 첫 대회에서 겪은 성공과 실패를 이후에도 사용할 수 있는 연구 원칙으로 바꾼 것입니다.

## 이 대회 전에는 몰랐던 것

첫 대회였기 때문에 처음에는 좋은 Backbone과 더 많은 Feature가 점수를 올려줄 것이라고 생각했습니다. Validation 점수가 높아지면 모델도 좋아졌다고 판단했고, 실패한 코드는 최종 결과에서 제외해도 된다고 생각했습니다.

프로젝트를 끝낸 뒤에는 생각이 달라졌습니다.

```text
좋은 모델보다 신뢰할 수 있는 검증이 먼저다.
점수 상승보다 상승의 원인을 설명하는 것이 중요하다.
실패는 다음 가설을 만드는 데이터다.
학습·추론·제출의 정합성도 모델 성능의 일부다.
재현되지 않는 실험은 연구 자산으로 남기 어렵다.
```

## 문제 해결 방식으로 남은 가장 큰 자산

앞으로의 모든 연구와 프로젝트에서 다음 순서를 사용합니다.

### 1. 어떤 문제가 있었는가

느낌이 아니라 Metric, 오류 사례, 데이터 분포, 실행 로그로 문제를 정의합니다.

### 2. 왜 이 방법을 선택했는가

유명한 방법이라는 이유로 사용하지 않습니다. 관찰된 문제를 어떤 원리로 해결할 수 있는지 먼저 설명합니다.

### 3. 어떻게 적용했는가

고정 조건과 변경 변수를 분리하고, 논문 원형·공개 구현·직접 변형을 구분합니다.

### 4. 결과가 어땠는가

Validation, Group Validation, Public 결과를 섞지 않습니다. 클래스 수나 Split이 다르면 직접 비교하지 않습니다.

### 5. 왜 성공하거나 실패했는가

결과와 해석을 구분합니다. 하나의 결과만으로 원인을 확정하지 않고 대안 가설과 한계를 남깁니다.

### 6. 다음에는 어떻게 활용할 것인가

채택한 기법뿐 아니라 실패 원인, 재발 방지 규칙, 후속 실험을 자산으로 남깁니다.

## 실패가 남긴 구체적인 연구 원칙

| 경험 | 당시 문제 | 앞으로의 원칙 |
|---|---|---|
| 초기 제출 `0.6XXX` | 문제와 데이터 구조 이해 부족 | 먼저 작고 명확한 Baseline을 만든다 |
| Session leakage | Random split 점수 착시 | 데이터 생성 단위로 Group split한다 |
| Threshold 반복 실패 | 한 Split에 맞춘 후처리 | 작은 개선은 반복과 독립 Holdout으로 확인한다 |
| Checkpoint 덮어쓰기 | 파일명과 실험 자산 연결 부족 | 실험 ID, Config, Commit, Checksum을 묶는다 |
| 학습·제출 입력 불일치 | Validation `0.774` 대비 Public `0.6619` | 전처리 코드를 하나로 공유하고 E2E test한다 |
| 12-class 점수 착시 | 다른 과제를 같은 지표로 비교 | Label space와 평가 조건을 항상 명시한다 |
| Self-distillation 실패 | Local selection 과적합 | 평가셋을 모델 선택에 반복 사용하지 않는다 |
| OOF KD 실패 | 이론적 정직성보다 약한 Teacher 손실이 큼 | 방법의 장점뿐 아니라 성공 조건과 비용을 본다 |
| FGM 성공 | Vanilla 학습 축이 덜 탐색됨 | “아직 바닐라인 축”을 점검한다 |
| 다양성 Ensemble 성공 | 최고 단일 모델만으로 조합하지 않음 | 오류 상관과 disagreement를 함께 본다 |

## 후속 AI Agent 연구 질문

### 1. Session-aware Action Modeling

현재 방식은 History를 하나의 긴 텍스트로 직렬화합니다. 후속 연구에서는 Action sequence와 자연어 Prompt를 분리해 인코딩하고, 세션 상태 전이를 명시적으로 모델링할 수 있습니다.

### 2. Hierarchical Action Ontology

14개 Action을 단순 평면 클래스로만 다루지 않고 `file navigation`, `editing`, `verification`, `communication` 같은 상위 목적과 세부 행동의 계층으로 정의합니다. 과거 Gating 실패를 반복하지 않도록 라벨 정의와 평가 방식부터 다시 설계합니다.

### 3. Label Quality와 Uncertainty

모호한 표본에 대해 복수 Annotator의 동의율을 측정하고, 단일 정답 대신 soft label 또는 ambiguity flag를 검토합니다. Confidence calibration과 selective prediction으로 “모를 때 모른다고 말하는” 모델도 평가합니다.

### 4. Noise-robust Learning

FGM 결과를 여러 Seed와 Dataset에서 재검증하고, Generalized Cross Entropy와 Co-teaching 같은 방법을 비교합니다. 현재 프로젝트의 label-noise 해석은 가설이므로 clean subset을 만들어 직접 검증합니다.

### 5. Generalization과 OOD

새로운 Repository, 새로운 언어, 보지 못한 도구 조합에서 성능을 측정합니다. 동일 분포의 평균 점수뿐 아니라 행동별 failure mode와 calibration drift를 분석합니다.

## 후속 엔지니어링 프로젝트

- Config 기반 재실행과 experiment registry 자동화
- MLflow 또는 Weights & Biases를 이용한 Metric·Artifact 추적
- 데이터와 모델용 checksum 및 model card
- 학습·평가·추론 전처리의 단일 모듈화
- Unit test, smoke test, GitHub Actions
- Docker 기반 실행 환경
- FastAPI 추론 API와 간단한 Streamlit/Gradio Demo
- Hugging Face Hub를 통한 허용 가능한 모델·문서 공개

이 기능들은 Repository를 화려하게 보이게 하기 위한 장식이 아닙니다. 이번 대회에서 실제로 겪은 재현성, 정합성, 자산 유실 문제를 방지하기 위한 다음 단계입니다.

## 성장의 기준

이 프로젝트를 “첫 대회인데도 완벽했다”는 이야기로 포장하지 않습니다. 오히려 다음 질문에 더 잘 답할 수 있게 된 과정을 보여줍니다.

- 이 점수를 믿을 수 있는가?
- 이 변화만이 결과를 만들었는가?
- 실패가 구현 문제인가, 가설 문제인가, 검증 문제인가?
- 다른 데이터에서도 같은 결론이 유지될까?
- 다른 사람이 실험을 이어갈 수 있는가?

## 최종 회고

이 대회는 하나의 종료된 프로젝트가 아니라 앞으로의 연구 방식을 만든 첫 번째 실험실이었습니다.

초기 `0.6XXX`에서 최종 `0.7776644`까지의 숫자도 중요하지만, 더 큰 성과는 점수를 올리는 과정에서 검증 누수, Label noise, Knowledge Distillation, Robust Training, Ensemble diversity, 재현성 문제를 실제로 경험했다는 점입니다.

앞으로 새로운 논문을 읽고 새로운 프로젝트를 시작할 때도 이 저장소의 여섯 질문으로 돌아옵니다.

> 어떤 문제가 있었는가 → 왜 선택했는가 → 어떻게 적용했는가 → 결과는 어땠는가 → 왜 성공하거나 실패했는가 → 다음에는 어떻게 활용할 것인가

이 질문을 반복하는 습관이 이번 첫 대회가 남긴 가장 좋은 거름입니다.
