# 06 — 오류 대응 사전

막혔을 때 여기서 **증상**을 먼저 찾으세요. 없으면 맨 아래 "그래도 안 될 때"로.

> 원칙: **같은 방법으로 두 번 실패했으면 세 번째 시도를 하지 마세요.**
> 원인을 바꿔서 접근해야 합니다. 오류 메시지 전문을 Copilot Chat에 붙여넣는 것이 가장 빠릅니다.

---

## A. 설치 / 실행

| 증상 | 원인 | 조치 |
| --- | --- | --- |
| `'python'은(는) 내부 또는 외부 명령이 아닙니다` | 설치 때 **Add to PATH** 체크 안 함 | Python 설치 파일 재실행 → Modify → PATH 체크. 또는 재설치 |
| `ModuleNotFoundError: No module named 'numpy'` | 패키지 미설치 | VS Code 하단 터미널에 `pip install numpy matplotlib` |
| VS Code Source Control에 "Git not found" | Git 미설치 또는 **재시작 안 함** | git-scm.com에서 설치 → **VS Code 완전 종료 후 재실행** |
| ▷ 실행 버튼이 없음 | Python 확장 미설치 | `Ctrl+Shift+X` → `Python`(Microsoft) 설치 |
| 실행은 되는데 한글 주석이 `??`로 깨짐 | 파일 인코딩 문제 | VS Code 우측 하단 인코딩 표시 클릭 → **Save with Encoding → UTF-8** |

## B. Copilot

| 증상 | 원인 | 조치 |
| --- | --- | --- |
| 회색 제안이 전혀 안 뜸 | 로그인 안 됨 | 좌하단 사람 아이콘 → GitHub 로그인 확인 |
| "Copilot이 활성화되지 않았습니다" | 요금제 미적용 | github.com/settings/copilot 확인. 학생 승인 전이면 무료 등급으로 진행 |
| 제안이 뜨다가 멈춤 | 무료 등급 월 한도(2,000회) 소진 | 다음 달까지 Chat 위주로 사용, 또는 학생 인증 승인 확인 |
| Chat 단축키가 안 먹음 | 다른 프로그램과 충돌 | `Ctrl+Shift+P` → `Chat: Focus on Chat View` 로 열기 |
| 답이 엉뚱함 | 맥락 부족 | 코드를 **드래그 선택한 뒤** 질문. [02 문서](02-vscode-and-copilot.md)의 템플릿 사용 |

## C. Git / GitHub

| 증상 | 원인 | 조치 |
| --- | --- | --- |
| Push했는데 브라우저에 안 보임 | Commit만 하고 Push 안 함 | Source Control → **⋯ → Push**. 파란 Sync 버튼 확인 |
| `Authentication failed` | 로그인 만료 | 좌하단 계정 → 로그아웃 후 재로그인 |
| `Updates were rejected... fetch first` | 서버에 내가 모르는 커밋이 있음 | 먼저 **Pull** → (충돌 나면 해결) → 다시 Push |
| `Please tell me who you are` | 사용자 정보 미설정 | 터미널에 아래 두 줄 (한 번만)<br>`git config --global user.name "홍길동"`<br>`git config --global user.email "본인@메일"` |
| clone이 `Repository not found` | 비공개 저장소 초대 미수락 | github.com/notifications 에서 초대 Accept |
| 파일에 `<<<<<<<` 표시가 생김 | 충돌(conflict) | [04 문서 §6](04-pull-and-collaboration.md) 참고 |
| 실수로 파일을 지웠다 | — | Source Control에서 해당 파일 **↩ Discard Changes**. 커밋 후였다면 GitHub의 **History**에서 복구 |
| `file is over 100MB` 로 push 거부 | 대용량 파일 | 파일 삭제 → `.gitignore`에 추가 → 다시 커밋. 결과 데이터는 올리지 말 것 |

## D. 동역학 계산이 이상할 때 — 자가 진단 순서

숫자가 이상하면 **코드 버그보다 입력·단위를 먼저 의심**하세요. 경험적으로 그쪽이 훨씬 많습니다.

### 1단계 — 단위부터
| 흔한 실수 | 증상 | 확인 |
| --- | --- | --- |
| kN/m를 N/m 자리에 넣음 | 주기가 **√1000 ≈ 31.6배** 길게 나옴 | `k_N_per_m`가 1e5보다 큰가? |
| ton을 kg 자리에 넣음 | 주기가 **31.6배 짧게** 나옴 | `m_kg`가 1e3보다 큰가? |
| mm를 m 자리에 넣음 | 변위가 1000배 | 값이 0.001~1 m 범위인가? |
| 감쇠비 5%를 `5`로 입력 | 진동이 사라지거나 `sqrt(음수)` 오류 | `zeta`가 0~1 사이인가? |

> 이 네 가지는 `assert` 로 미리 막을 수 있습니다. [03 문서 STEP 3](03-first-commit-walkthrough.md) 참고.

### 2단계 — 물리적 타당성 (숫자 보기 전에 감으로 걸러내기)
| 확인 항목 | 정상 범위 (건물 기준) |
| --- | --- |
| 고유주기 Tₙ | 저층 0.1~0.5 s / 중층 0.5~1.5 s / 초고층 3~8 s |
| 감쇠비 ζ | RC 3~5%, 강구조 1~3%. 0.5나 5가 나왔으면 입력 실수 |
| 자유진동 진폭 | 시간이 갈수록 **단조 감소**. 커지면 부호 오류 |
| 공진 시 증폭 | Rd_max ≈ 1/(2ζ). ζ=0.05면 약 10배 |

### 3단계 — 수치해가 이상할 때
| 증상 | 원인 | 조치 |
| --- | --- | --- |
| 응답이 발산 | 시간간격 dt가 너무 큼 | `dt ≤ Tₙ/20`, 권장 `Tₙ/100~Tₙ/200` |
| 이론해와 어긋남 | 초기조건·부호 | v₀ 항 `(v₀ + ζωₙx₀)/ω_d` 를 그대로 썼는지 |
| 주기가 미세하게 다름 | ω_d와 ωₙ 혼동 | 감쇠계에서 관측 주기는 **T_d = 2π/ω_d** |
| 그래프가 각져 보임 | 샘플 수 부족 | 주기당 최소 100점 |

### 4단계 — 그래도 모르면: 최소 재현 예제로 줄이기
전체 코드를 붙들고 씨름하지 말고, **문제가 되는 부분만 10줄 이하로 잘라내서** 실행해 보세요.
그 10줄을 Copilot에 주면 답이 훨씬 정확합니다. 잘라내는 과정에서 스스로 원인을 찾는 경우가 많습니다.

---

## 그래도 안 될 때 — 질문하는 법

이 저장소 **Issues** 탭 → **New issue**. 아래를 그대로 채우세요.

```markdown
### 무엇을 하려고 했나
감쇠비 5% SDOF의 자유진동 변위를 그리려고 했습니다.

### 무엇을 했나 (재현 순서)
1. examples/01_sdof_free_vibration/sdof_free.py 를 실행
2. zeta 값만 0.05 → 0.10 으로 바꿈

### 기대한 결과
진폭이 더 빨리 줄어드는 그래프

### 실제로 나온 것 (오류 전문을 텍스트로)
```
Traceback (most recent call last):
  File "sdof_free.py", line 27, in <module>
    ...
ValueError: math domain error
```

### 환경
Windows 11 / Python 3.12 / VS Code 1.9x

### 이미 시도한 것
- pip install numpy 재실행 → 변화 없음
- Copilot Chat에 물어봄 → dt 문제라고 했으나 dt를 줄여도 동일
```

> **오류는 스크린샷 말고 텍스트로.** 스크린샷은 검색·복사가 안 되고, 잘린 부분에 원인이 있는 경우가 많습니다.
> "이미 시도한 것"을 적으면 같은 답을 두 번 듣지 않습니다.

**다음:** [99 — 치트시트](99-cheatsheet.md)
