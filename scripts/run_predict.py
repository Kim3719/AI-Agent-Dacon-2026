"""모델 예측 실행 스크립트입니다.

학습된 모델과 test 데이터를 이용해 예측값을 만드는 진입점입니다.
현재는 팀원이 구현할 위치를 알려주는 기본 틀입니다.
"""

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(description="설정 파일을 받아 예측을 실행합니다.")
    parser.add_argument("--config", required=True, help="사용할 YAML 설정 파일 경로")
    args = parser.parse_args()

    print("예측 스크립트 자리입니다.")
    print(f"사용할 설정 파일: {args.config}")
    print("TODO: 실제 예측 로직을 이 파일 또는 공통 모듈에 연결하세요.")


if __name__ == "__main__":
    main()
