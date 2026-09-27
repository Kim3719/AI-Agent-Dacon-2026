# Version Map

| 순서 | 버전 | 핵심 변경 | 결과 또는 판정 |
|---:|---|---|---|
| 1 | 10차 | XLM-R Baseline | `0.7412` |
| 2 | 11차 | 이전 Action one-hot | 개선 없음 |
| 3 | 12차 | 2-stage 11/4-class | 클래스 축소 착시·전문 모델 개선 없음 |
| 4 | 13차 | Supervised Contrastive Loss | 개선 없음 |
| 5 | 14차 | 규칙 신호와 uncertainty tag | 일부 신호만 유효 |
| 6 | v15 | Pre-tokenization | 메모리 비용으로 실패 |
| 7 | v15b | 실시간 tokenization 복귀 | 안정화 |
| 8 | v15c | 오류 CSV·epoch 요약 | 분석 표준화 |
| 9 | 16~18차 | 레이어 융합·전문 모델·Large | Large는 Teacher로 전환 |
| 10 | v19 | 메모리 안전장치·Attention·IG | `0.7456` |
| 11 | 20차 | Prompt 위치·class weight 검토 | `0.7458` |
| 12 | 21~24차 | Re-ranking·Gating·Stacking | 복잡화로 해결되지 않음 |
| 13 | 25차 | 12-class 통합 | `0.7785`, 비교 불가 착시 |
| 14 | 26차 | 14-class 복원 | `0.7463` |
| 15 | 27차 | 32차원 메타피처 | `0.7351` |
| 16 | 28차 | 기록 미확보 | 추측하지 않음 |
| 17 | 29차 | Margin sample weighting | `0.7481~0.7499` |
