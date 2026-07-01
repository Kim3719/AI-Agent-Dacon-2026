"""DACON 제출 파일 생성 스크립트입니다.

예측 결과를 sample_submission.csv 형식에 맞춰 저장하는 역할을 담당할 예정입니다.
현재는 제출 생성 코드가 들어갈 위치를 표시하는 기본 틀입니다.
"""

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(description="예측 결과를 DACON 제출 파일로 변환합니다.")
    parser.add_argument("--config", required=True, help="사용할 YAML 설정 파일 경로")
    args = parser.parse_args()

    print("제출 파일 생성 스크립트 자리입니다.")
    print(f"사용할 설정 파일: {args.config}")
    print("TODO: sample_submission.csv 형식에 맞춰 submission 파일을 저장하세요.")


if __name__ == "__main__":
    main()
