# Step 06. 복잡하거나 큰 모델은 실제로 도움이 되었는가?

첫 대회였기 때문에 논문, 공식 문서, 공개 구현을 폭넓게 탐색하기보다 필요한 문제에 맞는 핵심 자료를 소수 참고했습니다. 실험 아이디어와 적용 방향의 대부분은 제가 제안했고, 팀과 함께 결과를 검토했습니다.

## 공통 기록 기준

각 방법은 다음 여섯 가지 출처와 증거를 구분합니다.

1. 참고한 논문
2. 기술 문서
3. 공개 구현
4. 팀원의 제안 — 프로젝트에서는 제 제안이 대부분
5. 프로젝트에 맞게 직접 변형한 부분
6. 실제 실험 결과

## XLM-R Large와 Knowledge Distillation

### 어떤 문제가 있었는가

Base 모델의 한계가 보였지만 Large 모델은 약 1.12GB로 제출 제한을 넘고 추론시간도 부담됐습니다.

### 왜 이 방법을 선택했는가

Large를 직접 제출하지 않고 Teacher로 사용해 확률 분포를 Base Student에 전달하는 Knowledge Distillation을 선택했습니다.

### 어떻게 적용했는가

Hinton 등의 KD 논문을 개념적 근거로 삼아 hard-label CE와 temperature-scaled soft-target KL을 결합했습니다. `alpha=0.7`, `temperature=2.0`을 사용한 실험을 중심으로 비교했습니다.

### 결과가 어땠는가

XLM-R Large Validation은 약 `0.7691`, 증류 Base는 약 `0.7656`을 기록했고 앙상블 Public은 `0.7702`에 도달했습니다.

### 왜 성공하거나 실패했는가

Large의 class distribution을 작은 모델에 전달하면서 배포 제약을 지킬 수 있었습니다. 반면 같은 Teacher에서 나온 Student를 반복해서 추가하면 오류가 강하게 상관되어 Ensemble 이득이 작았습니다.

### 다음에는 어떻게 활용할 것인가

Teacher 성능뿐 아니라 Student와의 오류 상관, 배포 비용, soft target의 누수 가능성까지 함께 평가합니다.

## 실패 실험 요약

| 방법 | 선택 이유 | 실제 결과 | 해석 |
|---|---|---:|---|
| 계층 분류 / Gating | 취약 4클래스를 별도 전문화 | 안정적 개선 없음 | 복잡성보다 클래스 경계의 모호성이 큼 |
| Self-distillation | 현재 Champion 지식 재사용 | Local 개선 후 Public 순이득 0 | 선택 과적합과 자기복제의 한계 |
| Qwen Teacher | 다른 계열의 보완 오류 기대 | Group split에서 `-0.0049` | Random split 개선은 누수 착시 |
| XL Teacher | 더 큰 용량의 지식 기대 | 약 `0.7444` | 병목은 용량만이 아니었음 |
| Model Soup | 추가 학습 없이 모델 결합 | 약 `0.5653` | 다른 Seed는 서로 다른 loss basin |
| 2-fold OOF Teacher | Teacher가 보지 않은 soft label | 약 `0.7423` | 절반 데이터 Teacher의 약화가 더 큼 |
| Re-ranking | top-2 후보의 순위 교정 | 약 `-0.0041` | 확률만으로 뒤집을 추가 신호 부족 |

## 출처

논문과 구현 링크는 [`references/README.md`](../references/README.md)에 정리했습니다. 공개 구현은 그대로 복사한 것이 아니라 개념과 인터페이스를 확인하는 참고자료로 사용했습니다.
