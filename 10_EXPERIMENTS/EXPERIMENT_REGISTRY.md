# Experiment Registry

| ID | 실험 | 핵심 결과 | 판정 |
|---|---|---|---|
| EXP-001 | XLM-R Base Baseline | Validation `0.7412` | 기준점 |
| EXP-002 | Previous Action / Meta Features | 안정적 개선 없음 | 기각 |
| EXP-003 | Hierarchical / Gating | 취약 클래스 해결 실패 | 기각 |
| EXP-004 | v3b Recent-state Input | 단일보다 다양성 기여 | Ensemble 후보 |
| EXP-005 | XLM-R Large | Validation `0.7691`, 제출 제약 초과 | Teacher 채택 |
| EXP-006 | Large→Base KD | Student `0.7656`, Public Ensemble `0.7702` | 채택 |
| EXP-007 | Per-class Offset | 5회 평균 `-0.0007` | 기각 |
| EXP-008 | FGM + LLRD | Validation `0.7723`, Public `0.7745` | 채택 |
| EXP-009 | Qwen Teacher | Group split `-0.0049` | 기각 |
| EXP-010 | Model Soup | `0.5653` | 기각 |
| EXP-011 | 2-fold OOF KD | `0.7423` | 기각 |
| EXP-012 | Struct Student | 단일보다 Ensemble 기여 | 채택 |
| EXP-013 | Final Ensemble | Public `0.7776644` | 최종 |

이 표는 현재 전달된 기록의 요약입니다. 각 실험의 원본 로그와 Config가 복원되면 별도 디렉터리로 확장합니다.
