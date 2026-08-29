# 응용동역학 (2026학년도 2학기)

초고층내진계약학과 · 수업 저장소

**수강생 안내 페이지 → https://titoliviomilazzo.github.io/StructuralDynamics2_2026/**
(로그인 없이 열립니다. 0주차 안내는 이 주소를 공유하세요.)

이 저장소는 **강의자료 배포 + 과제 제출 + 코드 공유**를 한 곳에서 처리합니다.
GitHub을 처음 써 보는 분을 기준으로 만들었습니다. 순서대로만 따라오면 됩니다.

---

## 지금 바로 할 일 (0주차, 총 40~60분)

| 순서 | 할 일 | 문서 | 소요 |
| --- | --- | --- | --- |
| 1 | GitHub 계정 만들고 **학생 인증** 신청 | [01](docs/01-signup-and-student-verification.md) | 20분 |
| 2 | VS Code + Python 설치, **Copilot 켜기** | [02](docs/02-vscode-and-copilot.md) | 20분 |
| 3 | 내 실습 저장소 만들고 **첫 커밋** 올리기 | [03](docs/03-first-commit-walkthrough.md) | 20분 |

학생 인증은 승인까지 시간이 걸립니다. **1번은 오늘 안에 신청하세요.**
승인을 기다리는 동안 2·3번은 그대로 진행할 수 있습니다.

---

## 문서 목록

| 문서 | 내용 | 언제 읽나 |
| --- | --- | --- |
| [00 — 왜 GitHub을 쓰는가](docs/00-why-github.md) | 개념·용어 6개. 설치 없이 읽기만 | 제일 먼저 |
| [01 — 계정 생성과 학생 인증](docs/01-signup-and-student-verification.md) | 가입 → 학생 인증 → Copilot 무료 | 0주차 |
| [02 — VS Code와 Copilot](docs/02-vscode-and-copilot.md) | 설치 → 로그인 → AI 쓰는 법 | 0주차 |
| [03 — 첫 커밋 따라하기](docs/03-first-commit-walkthrough.md) | 저장소 만들기 → commit → push | 0주차 |
| [04 — Pull과 협업](docs/04-pull-and-collaboration.md) | 자료 받기 → 브랜치 → Pull Request | 1~2주차 |
| [05 — 과제 제출 규칙](docs/05-assignment-submission.md) | 폴더·파일명·커밋 규칙, 채점 기준 | 과제 전 |
| [06 — 오류 대응 사전](docs/06-error-handbook.md) | 증상별 조치표 | 막혔을 때 |
| [99 — 치트시트](docs/99-cheatsheet.md) | 1장 요약. 인쇄해서 옆에 두기 | 상시 |

## 예제 코드

| 폴더 | 주제 | 다루는 것 |
| --- | --- | --- |
| [examples/01_sdof_free_vibration](examples/01_sdof_free_vibration/) | SDOF 감쇠 자유진동 | 고유주기, 감쇠비, 대수감쇠율 |
| [examples/02_harmonic_response](examples/02_harmonic_response/) | 조화하중 정상응답 | 동적증폭계수, 공진, 위상각 |

두 예제 모두 **이론해와 수치해를 나란히 계산해서 서로 검증**하도록 짜여 있습니다.
"돌아가니까 맞겠지"가 아니라 **틀렸으면 즉시 드러나게** 만드는 방식을 예제로 익히세요.

## 폴더 구조

```
StructuralDynamics2_2026/
├─ README.md              ← 지금 이 파일
├─ docs/                  ← 튜토리얼 (00~99)
├─ examples/              ← 강의용 예제 코드
├─ assignments/           ← 과제 제출 위치
│   └─ <학번>_<이름>/      ← 본인 폴더에만 작업
└─ .gitignore
```

---

## 이 수업의 3대 원칙

1. **숫자는 코드가 계산한다.** AI도, 사람도 암산하지 않습니다. 손으로 옮겨 적은 수치는 오류의 1순위 원인입니다.
2. **단위는 변수 이름에 쓴다.** `k = 4000`이 아니라 `k_N_per_m = 4.0e6`. 단위 혼동(kN↔N, mm↔m, tonf)은 동역학 과제 오답의 절대 다수를 차지합니다.
3. **AI 답은 검증 전까지 가설이다.** Copilot이 준 식·상수·API는 반드시 교재나 실행 결과로 확인한 뒤 씁니다.

## 도움이 필요할 때

1. [06 — 오류 대응 사전](docs/06-error-handbook.md)에서 증상 검색
2. Copilot Chat에 붙여넣고 질문 ([02 문서](docs/02-vscode-and-copilot.md)의 질문 템플릿 사용)
3. 그래도 막히면 이 저장소 **Issues** 탭에 새 이슈 등록
   - 제목: `[주차] 한 줄 증상`
   - 본문: 무엇을 했는지 / 기대한 결과 / 실제 나온 오류 전문(스크린샷 아닌 텍스트)
