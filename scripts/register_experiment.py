"""실험 결과를 experiments/experiment_log.csv에 추가하는 간단한 도구입니다.

팀원이 실험을 마친 뒤 아래처럼 사용할 수 있습니다.

python scripts/register_experiment.py ^
  --experiment-id EXP001 ^
  --date 2026-07-02 ^
  --owner HAK ^
  --branch experiment/EXP001-baseline ^
  --model "TF-IDF Logistic Regression" ^
  --features current_prompt ^
  --validation-f1 TBD ^
  --accuracy TBD ^
  --public-score TBD ^
  --summary "첫 baseline 실험"
"""

from argparse import ArgumentParser
import csv
from pathlib import Path


LOG_PATH = Path("experiments/experiment_log.csv")


def main() -> None:
    parser = ArgumentParser(description="실험 결과를 experiment_log.csv에 추가합니다.")
    parser.add_argument("--experiment-id", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--features", required=True)
    parser.add_argument("--validation-f1", default="TBD")
    parser.add_argument("--accuracy", default="TBD")
    parser.add_argument("--public-score", default="TBD")
    parser.add_argument("--summary", default="TBD")
    parser.add_argument("--pr-url", default="TBD")
    args = parser.parse_args()

    row = {
        "experiment_id": args.experiment_id,
        "date": args.date,
        "owner": args.owner,
        "branch": args.branch,
        "model": args.model,
        "features": args.features,
        "validation_f1": args.validation_f1,
        "accuracy": args.accuracy,
        "public_score": args.public_score,
        "summary": args.summary,
        "pr_url": args.pr_url,
    }

    with LOG_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row))
        writer.writerow(row)

    print(f"실험 기록을 추가했습니다: {LOG_PATH}")


if __name__ == "__main__":
    main()
