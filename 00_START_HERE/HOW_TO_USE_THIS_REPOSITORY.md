# 이 Repository의 활용 목적

이 저장소는 아래 일곱 가지 목적으로 사용합니다.

## 1. 첫 AI 대회 학습 기록

초기 `0.6XXX` 제출부터 최종 Public Macro-F1 `0.7776644`까지, 처음 접한 문제와 시행착오를 숨기지 않고 남깁니다.

## 2. AI 연구 방법론 포트폴리오

모델 이름을 나열하는 대신 문제 정의, 가설, 실험, 분석, 다음 판단이 어떻게 연결되는지 보여줍니다.

## 3. 재현 가능한 실험 설계 참고 자료

고정할 조건, 변경할 변수, Group 기반 검증, 반복 실험, 실험 ID, 설정과 결과 연결 방식을 기록합니다. 별도의 재현 단계는 두지 않으며 필요한 정보는 각 실험 문서에 함께 둡니다.

## 4. 후속 AI Agent 연구의 출발점

Session-aware modeling, action hierarchy, uncertainty estimation, label-noise robust learning 등 다음 연구 질문을 도출하는 기반으로 사용합니다.

## 5. Validation Leakage 사례 연구

동일 세션이 Train과 Validation에 동시에 포함될 때 발생할 수 있는 착시와, Group 단위 분할이 필요했던 이유를 실제 경험으로 설명합니다.

## 6. Knowledge Distillation 사례

성능이 좋은 Large 모델을 제출 크기와 시간 제약 때문에 직접 사용하지 못한 문제, Teacher의 soft target을 Base Student에 전달한 과정, 자기증류와 OOF 증류가 실패한 이유를 함께 다룹니다.

## 7. Label Noise와 Robust Training 사례

구분이 모호한 클래스와 낮은 margin 샘플을 분석하고, FGM·LLRD·sample weighting을 적용해 노이즈에 덜 민감한 학습을 시도한 과정을 정리합니다.
