"""설정 파일 로딩 유틸이 들어갈 파일입니다."""

from pathlib import Path


def load_config(path: str | Path):
    """YAML 설정 파일을 로드하는 함수 자리입니다.

    TODO:
    - PyYAML 의존성 추가 여부 결정
    - 기본 config와 실험별 config 병합 방식 결정
    """
    raise NotImplementedError("설정 로딩 로직은 아직 구현 전입니다.")
