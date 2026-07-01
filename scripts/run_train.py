"""모델 학습 실행 스크립트입니다.

아직 실제 학습 로직은 연결하지 않았습니다.
팀원이 나중에 baseline 학습 코드를 만든 뒤 이 파일을 진입점으로 사용합니다.
"""

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(description="설정 파일을 받아 모델 학습을 실행합니다.")
    parser.add_argument("--config", required=True, help="사용할 YAML 설정 파일 경로")
    args = parser.parse_args()

    print("학습 스크립트 자리입니다.")
    print(f"사용할 설정 파일: {args.config}")
    print("TODO: 실제 학습 로직을 이 파일 또는 공통 모듈에 연결하세요.")


if __name__ == "__main__":
    main()
