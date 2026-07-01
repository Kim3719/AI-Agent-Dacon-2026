# 팀 협업 규칙

이 문서는 팀원이 GitHub에 코드를 올릴 때 지켜야 하는 최소 규칙입니다.

목표는 단순합니다.

> 각자 자유롭게 실험하되, Main Repository에는 팀이 볼 수 있는 형태로 정리된 변경사항만 올립니다.

## 1. 저장소 역할

### Main Repository

- 주소: `https://github.com/Kim3719/AI-Agent-Dacon-2026.git`
- 역할: 팀 공식 저장소
- 들어와야 하는 것:
  - 같이 쓸 코드
  - 좋은 실험 결과
  - 제출 파일 기록
  - 팀원이 이해할 수 있는 변경 설명

### 개인 Repository

팀원 개인 레포는 자유 실험 공간입니다.

예상 이름:

| 팀원 | 개인 레포 이름 예시 |
| --- | --- |
| HAK | `AI-Agent-Dacon-2026-HAK` |
| SEOK | `AI-Agent-Dacon-2026-SEOK` |
| JUN | `AI-Agent-Dacon-2026-JUN` |
| HEUN | `AI-Agent-Dacon-2026-HEUN` |
| YOUNG | `AI-Agent-Dacon-2026-YOUNG` |

개인 레포에서는 실패 실험, 임시 코드, 지저분한 노트북을 자유롭게 관리해도 됩니다.

Main Repository에는 다른 팀원도 이해할 수 있게 정리된 내용만 PR로 올립니다.

## 2. 브랜치 규칙

`main`에는 직접 push하지 않습니다.

작업할 때는 아래 형식으로 브랜치를 만듭니다.

| 목적 | 브랜치 이름 예시 |
| --- | --- |
| 실험 | `experiment/EXP001-baseline` |
| 기능 추가 | `feature/data-loader` |
| 문서 수정 | `docs/update-readme` |
| 버그 수정 | `fix/submission-format` |

## 3. 커밋 메시지 규칙

커밋 메시지는 짧고 명확하게 씁니다.

예시:

```text
feat: add baseline training script
exp: add EXP001 result summary
docs: update team workflow
fix: correct submission column order
chore: update requirements
```

## 4. PR 규칙

PR에는 긴 보고서를 쓰지 않아도 됩니다.

대신 아래 둘 중 하나는 반드시 적습니다.

1. 본인이 직접 적은 변경 요약
2. AI에게 git diff를 보여주고 받은 변경 요약

팀원이 PR을 봤을 때 아래 질문에 답할 수 있으면 충분합니다.

- 무엇을 바꿨는가?
- 왜 바꿨는가?
- 성능이나 제출 결과가 바뀌었는가?
- 다른 팀원이 실행하려면 어떻게 해야 하는가?

## 5. main merge 기준

`main`에는 매일 가장 좋은 모델 또는 팀 전체가 써야 하는 안정된 변경만 merge합니다.

merge 가능:

- 기존보다 성능이 좋아진 실험
- 팀 공통 코드로 쓰기 좋은 기능
- 제출 형식 오류 수정
- README, 규칙, 실행법처럼 팀 전체에 필요한 문서

merge 보류:

- 본인 환경에서만 되는 코드
- 변경 설명이 없는 PR
- 대용량 데이터나 모델 파일이 포함된 PR
- 실험 결과가 불명확한 모델 변경

## 6. 대용량 파일 규칙

아래 파일은 기본적으로 GitHub에 올리지 않습니다.

- 원본 데이터
- 큰 모델 파일
- 긴 로그 파일
- 임시 캐시 파일

필요한 경우 파일 자체 대신 `README`나 로그 CSV에 위치와 설명만 남깁니다.
