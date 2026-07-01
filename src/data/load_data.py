"""데이터 로딩 함수가 들어갈 파일입니다.

아직 실제 데이터 로딩 로직은 구현하지 않았습니다.
향후 `train.jsonl`, `train_labels.csv`, `test.jsonl`을 읽고
모델 학습에 사용할 형태로 변환하는 함수를 이 파일에 작성합니다.
"""

from pathlib import Path


def load_jsonl(path: str | Path):
    """JSONL 파일을 읽는 함수 자리입니다.

    TODO:
    - 한 줄씩 JSON 객체를 읽기
    - `id`, `session_meta`, `history`, `current_prompt` 필드 검증
    - pandas DataFrame 또는 list[dict] 형태로 반환
    """
    raise NotImplementedError("데이터 로딩 로직은 아직 구현 전입니다.")


def load_train_data(config: dict):
    """학습 입력과 라벨을 함께 로드하는 함수 자리입니다."""
    raise NotImplementedError("학습 데이터 로딩 로직은 아직 구현 전입니다.")
