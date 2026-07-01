# submissions 폴더

DACON에 제출한 파일과 제출 기록을 관리하는 곳입니다.

제출 파일 자체를 올릴지 여부는 파일 크기와 대회 규칙을 보고 결정합니다.

중요한 것은 **어떤 실험에서 나온 제출인지 기록하는 것**입니다.

## submission_log.csv 컬럼 설명

| 컬럼 | 의미 |
| --- | --- |
| `submission_id` | 제출 번호입니다. 예: `SUB001` |
| `date` | 제출 날짜입니다. |
| `experiment_id` | 어떤 실험에서 나온 제출인지 적습니다. |
| `owner` | 제출한 사람입니다. |
| `file_name` | 제출 파일 이름입니다. |
| `public_score` | DACON Public Score입니다. |
| `memo` | 특이사항입니다. |

## 기록 예시

```csv
SUB001,2026-07-02,EXP001,HAK,EXP001_submission.csv,TBD,첫 제출 테스트
```
