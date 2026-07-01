# AI-Agent-Dacon-2026

[![Competition](https://img.shields.io/badge/DACON-AI%20Agent%20Action%20Prediction-blue)](https://dacon.io/competitions/official/236694/overview/description)
![Status](https://img.shields.io/badge/status-team%20workflow%20setup-lightgrey)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB)
![License](https://img.shields.io/badge/license-MIT-green)

DACON AI Agent Action Prediction 대회를 위한 팀 공식 저장소입니다.

이 저장소의 목표는 단순합니다.

> 팀원들은 각자 자유롭게 실험하고, Main Repository에는 다른 팀원이 이해할 수 있는 변경사항과 좋은 결과만 Pull Request로 올립니다.

현재 이 저장소는 **팀 협업 구조를 세팅한 단계**입니다. 아직 확정된 최고 모델, 검증 점수, 제출 점수는 없습니다.

## 목차

- [이 저장소는 무엇인가](#이-저장소는-무엇인가)
- [팀 운영 방식](#팀-운영-방식)
- [개인 Repository 사용 방식](#개인-repository-사용-방식)
- [폴더 구조](#폴더-구조)
- [팀원이 작업하는 순서](#팀원이-작업하는-순서)
- [실험 기록 방식](#실험-기록-방식)
- [PR 작성 방식](#pr-작성-방식)
- [매일 Best Model merge 방식](#매일-best-model-merge-방식)
- [팀원에게 공유할 짧은 안내문](#팀원에게-공유할-짧은-안내문)

## 이 저장소는 무엇인가

이 저장소는 팀의 공식 기준 저장소입니다.

들어오는 내용:

- 팀이 같이 사용할 코드
- 의미 있는 실험 결과
- 제출 파일 기록
- 매일 best model 판단에 필요한 정보
- 팀원이 이해할 수 있는 PR 설명

들어오면 안 되는 내용:

- 개인 실험 중간 산출물
- 설명 없는 코드
- 대용량 원본 데이터
- 큰 모델 파일
- 본인 컴퓨터에서만 되는 임시 코드

## 팀 운영 방식

브랜치는 아래처럼 사용합니다.

| 브랜치 | 역할 |
| --- | --- |
| `main` | 팀 공식 안정 브랜치입니다. 매일 가장 좋은 모델 또는 팀 공통 변경만 들어옵니다. |
| `experiment/*` | 실험용 브랜치입니다. 예: `experiment/EXP001-baseline` |
| `feature/*` | 기능 개발 브랜치입니다. 예: `feature/data-loader` |
| `docs/*` | 문서 수정 브랜치입니다. 예: `docs/update-readme` |
| `fix/*` | 버그 수정 브랜치입니다. 예: `fix/submission-format` |

중요 규칙:

- `main`에 직접 push하지 않습니다.
- 작업은 개인 레포 또는 새 브랜치에서 합니다.
- Main Repository에는 PR로 올립니다.
- PR에는 직접 요약 또는 AI 요약을 붙입니다.

## 개인 Repository 사용 방식

팀원 개인 레포는 자유 실험 공간입니다.

예상 레포 이름:

| 팀원 | 개인 레포 이름 예시 |
| --- | --- |
| HAK | `AI-Agent-Dacon-2026-HAK` |
| SEOK | `AI-Agent-Dacon-2026-SEOK` |
| JUN | `AI-Agent-Dacon-2026-JUN` |
| HEUN | `AI-Agent-Dacon-2026-HEUN` |
| YOUNG | `AI-Agent-Dacon-2026-YOUNG` |

개인 레포에서는 자유롭게 해도 됩니다.

- 실패한 실험
- 임시 노트북
- 여러 모델 테스트
- 정리 전 코드

Main Repository에 올릴 때만 팀원이 이해할 수 있게 정리합니다.

## 폴더 구조

```text
AI-Agent-Dacon-2026/
|-- README.md
|-- CONTRIBUTING.md
|-- requirements.txt
|-- .github/
|   |-- PULL_REQUEST_TEMPLATE.md
|   `-- ISSUE_TEMPLATE/
|       |-- bug_report.md
|       |-- experiment.md
|       |-- analysis.md
|       `-- todo.md
|-- configs/
|   |-- README.md
|   `-- exp_template.yaml
|-- data/
|   `-- README.md
|-- experiments/
|   |-- README.md
|   `-- experiment_log.csv
|-- scripts/
|   |-- README.md
|   |-- run_train.py
|   |-- run_predict.py
|   |-- make_submission.py
|   `-- register_experiment.py
|-- submissions/
|   |-- README.md
|   `-- submission_log.csv
|-- reports/
|   |-- README.md
|   `-- daily/
|       |-- README.md
|       `-- YYYY-MM-DD_template.md
|-- models/
|   `-- README.md
`-- logs/
    `-- README.md
```

## 각 폴더가 하는 일

| 폴더 | 역할 |
| --- | --- |
| `.github/` | PR 템플릿과 Issue 템플릿을 저장합니다. GitHub에서 PR/Issue를 만들 때 자동으로 양식이 뜹니다. |
| `configs/` | 실험 설정 파일을 저장합니다. 어떤 모델, 어떤 피처, 어떤 seed를 썼는지 남기는 곳입니다. |
| `data/` | 대회 데이터를 로컬에서 둘 위치를 설명합니다. 원본 데이터는 GitHub에 올리지 않습니다. |
| `experiments/` | 중요한 실험 결과를 한 줄씩 기록합니다. 긴 보고서 대신 `experiment_log.csv`를 사용합니다. |
| `scripts/` | 팀원이 실행할 명령어 파일을 둡니다. 현재는 학습/예측/제출/실험기록용 기본 틀입니다. |
| `submissions/` | DACON 제출 기록을 관리합니다. 어떤 실험에서 나온 제출인지 추적합니다. |
| `reports/` | 매일 best model을 정할 때 필요한 짧은 일일 기록을 남깁니다. |
| `models/` | 모델 파일 관리 위치입니다. 큰 모델 파일은 GitHub에 올리지 않고 설명만 남깁니다. |
| `logs/` | 실행 로그 위치입니다. 긴 로그는 올리지 않고 중요한 내용만 요약합니다. |

## 팀원이 작업하는 순서

처음 한 번:

```bash
git clone https://github.com/Kim3719/AI-Agent-Dacon-2026.git
cd AI-Agent-Dacon-2026
pip install -r requirements.txt
```

작업할 때:

```bash
git checkout main
git pull origin main
git checkout -b experiment/EXP001-baseline
```

작업 후:

```bash
git status
git add .
git commit -m "exp: add EXP001 baseline summary"
git push origin experiment/EXP001-baseline
```

그다음 GitHub에서 PR을 만듭니다.

## 실험 기록 방식

중요한 실험은 [experiments/experiment_log.csv](experiments/experiment_log.csv)에 한 줄로 기록합니다.

긴 문서를 매번 쓰지 않아도 됩니다.

기록 예시:

```csv
EXP001,2026-07-02,HAK,experiment/EXP001-baseline,TF-IDF LR,current_prompt,0.7123,0.8012,TBD,첫 baseline 실험,TBD
```

실험 기록을 자동으로 추가하고 싶으면 아래 명령을 사용할 수 있습니다.

```bash
python scripts/register_experiment.py --experiment-id EXP001 --date 2026-07-02 --owner HAK --branch experiment/EXP001-baseline --model "TF-IDF LR" --features current_prompt --validation-f1 TBD --accuracy TBD --public-score TBD --summary "첫 baseline 실험"
```

## PR 작성 방식

PR에는 긴 보고서를 쓰지 않습니다.

대신 아래 중 하나를 적습니다.

- 본인이 직접 쓴 변경 요약
- AI에게 변경사항을 요약시켜 받은 내용

AI에게 요약을 부탁할 때는 이렇게 물어보면 됩니다.

```text
아래 git diff를 보고 PR에 넣을 변경 요약을 한국어로 짧게 작성해줘.
팀원이 이해할 수 있게 무엇을 바꿨고, 왜 바꿨고, 실행 방법이 있는지 정리해줘.
```

PR 템플릿은 [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)에 있습니다.

## 매일 Best Model merge 방식

매일 마지막에 팀이 PR과 실험 기록을 보고 하나를 정합니다.

main에 merge 가능한 것:

- 오늘 기준 validation score가 가장 좋은 모델
- public score가 개선된 모델
- 점수는 비슷하지만 더 안정적이고 재현 쉬운 모델
- 제출 형식 오류 같은 중요한 수정

main에 merge하지 않는 것:

- 설명 없는 모델 변경
- 실행 방법이 없는 코드
- 점수가 불명확한 실험
- 개인 실험 중간 결과

하루 기록은 [reports/daily/YYYY-MM-DD_template.md](reports/daily/YYYY-MM-DD_template.md)를 복사해서 작성합니다.

## 팀원에게 공유할 짧은 안내문

아래 문장을 그대로 팀원에게 보내면 됩니다.

```text
이 저장소는 팀 공식 Main Repository입니다.
각자 개인 레포에서는 자유롭게 실험해도 됩니다.
하지만 Main Repository에는 좋은 결과나 팀이 같이 쓸 코드만 PR로 올려주세요.

작업할 때는 main에 직접 push하지 말고 새 브랜치를 만들어주세요.
예: experiment/EXP001-baseline, feature/data-loader

PR을 만들 때는 무엇을 바꿨는지 짧게 적어주세요.
직접 적어도 되고, AI에게 변경사항을 요약시켜 붙여넣어도 됩니다.

실험 결과가 있으면 experiments/experiment_log.csv에 한 줄로 기록해주세요.
DACON 제출을 했다면 submissions/submission_log.csv에도 기록해주세요.

매일 팀이 PR과 점수를 확인해서 가장 좋은 모델만 main에 merge합니다.
```
