"""피처 생성 함수가 들어갈 파일입니다.

이 대회에서는 현재 사용자 발화, 이전 대화/행동 기록, 세션 메타데이터,
작업공간 정보를 함께 활용할 수 있습니다.
"""


def build_features(records):
    """모델 입력 피처를 만드는 함수 자리입니다.

    TODO:
    - `current_prompt` 텍스트 피처
    - history 길이와 이전 action 피처
    - token budget, turn index 같은 session metadata 피처
    - workspace 언어 비율, git_dirty, last_ci_status 피처
    """
    raise NotImplementedError("피처 생성 로직은 아직 구현 전입니다.")
