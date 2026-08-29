---
layout: default
title: "VS Code · Python · Copilot"
subtitle: "환경 구축"
---

# 02 — VS Code 설치와 Copilot 사용법

**목표:** 프로그램 하나(VS Code)만 깔고, 그 안에서 코드 작성·AI·GitHub을 전부 처리한다.
**소요:** 설치 15분 + 사용법 익히기 10분

> 이 수업에서는 **VS Code 하나만** 씁니다. Git을 따로 설치하거나 터미널에 명령어를 칠 일은 없습니다.

---

## STEP 1 — Python 설치 (5분)

이미 Anaconda나 Python이 깔려 있으면 건너뛰세요.

1. **https://www.python.org/downloads/** → 큰 노란 버튼(Download Python 3.x) 클릭
2. 설치 파일 실행
3. ⚠️ **첫 화면 맨 아래 `Add python.exe to PATH` 체크박스를 반드시 켤 것**
   (이거 안 켜면 나중에 "python을 찾을 수 없습니다" 오류가 납니다. 가장 흔한 실수)
4. **Install Now** → 완료

## STEP 2 — VS Code 설치 (5분)

1. **https://code.visualstudio.com/** → **Download** 클릭
2. 설치 중 나오는 체크박스에서 아래 두 개를 켜면 편합니다
   - `Add "Open with Code" action to Windows Explorer file context menu`
   - `Add to PATH`
3. 실행 → 처음 뜨는 환영 화면은 닫아도 됩니다

### 화면이 영어라 불편하면

`Ctrl + Shift + X` → 검색창에 `Korean` → **Korean Language Pack** 설치 → 재시작.

> 다만 이 문서와 대부분의 오류 검색 결과는 영어 기준입니다.
> **영어 UI 그대로 두는 것을 권합니다.** 쓰는 단어는 열 개 남짓입니다.

## STEP 3 — 확장(Extension) 3개 설치 (5분)

VS Code 왼쪽 세로 막대에서 **네모 4개 아이콘**(Extensions)을 누르거나 `Ctrl + Shift + X`.
검색창에 아래를 하나씩 넣고 **Install**.

| 검색어 | 만든 곳 | 역할 |
| --- | --- | --- |
| `Python` | Microsoft | 파이썬 실행·문법 검사 |
| `GitHub Copilot` | GitHub | 코드 자동 제안 |
| `GitHub Copilot Chat` | GitHub | AI에게 대화로 질문 |

> 이름이 비슷한 가짜 확장이 있습니다. **게시자(Publisher)가 Microsoft / GitHub 인지** 확인하세요.

## STEP 4 — GitHub 로그인 (2분)

1. VS Code **왼쪽 아래 사람 모양 아이콘**(Accounts) 클릭
2. `Sign in with GitHub to use GitHub Copilot` 클릭
3. 브라우저가 열리면 **Authorize** → VS Code로 돌아옴
4. 오른쪽 아래 상태바에 **Copilot 아이콘**이 생기면 성공

로그인이 되면 이후 clone·push에서 아이디/비밀번호를 다시 묻지 않습니다.

---

## Copilot 쓰는 법 — 세 가지

### ① 인라인 제안 — 타이핑하면 회색 글씨가 따라옴

파이썬 파일에 주석이나 함수 첫 줄을 쓰면, 나머지를 회색으로 제안합니다.

```python
# 질량 m, 강성 k로부터 고유주기 Tn을 계산하는 함수
def natural_period(m_kg, k_N_per_m):
```

여기서 Enter를 치면 아래처럼 회색 글씨가 뜹니다.

| 키 | 동작 |
| --- | --- |
| `Tab` | 제안 수락 |
| `Esc` | 제안 무시 |
| `Alt + ]` / `Alt + [` | 다른 제안 보기 |

### ② Copilot Chat — 대화로 묻기

`Ctrl + Alt + I` (Mac은 `Ctrl + Cmd + I`) 로 오른쪽에 채팅창을 엽니다.

코드를 **드래그로 선택한 뒤** 물어보면 그 부분을 보고 답합니다. 이게 핵심입니다.

### ③ 인라인 채팅 — 코드 위에서 바로 고치기

고칠 코드를 선택하고 `Ctrl + I`. 작은 입력창이 뜹니다.
`감쇠비를 인자로 받도록 바꿔줘` 같이 적으면 그 자리에서 수정안을 보여 줍니다.
**Accept / Discard** 로 결정합니다.

---

## 질문 잘 쓰는 법 — 구조동역학용 템플릿

Copilot은 **맥락을 주는 만큼** 정확해집니다. 그냥 "안 돼요"는 최악의 질문입니다.

### 오류가 났을 때

```
아래 코드를 실행했더니 오류가 납니다.

[코드]
(코드 붙여넣기)

[오류 전문]
(터미널에 빨간 글씨로 나온 것 전부 복사)

[하려던 것]
감쇠비 5%인 SDOF의 자유진동 변위 응답을 그리려고 합니다.

원인과 고친 코드를 알려주세요.
```

### 개념을 물을 때

```
구조동역학 수강생 기준으로 설명해 주세요.
대수감쇠율(logarithmic decrement)로 감쇠비를 구하는 식이 왜
delta = 2*pi*zeta/sqrt(1-zeta^2) 인지, 유도 과정을 단계별로 보여주세요.
```

### 코드를 만들 때

```
단자유도계 감쇠 자유진동을 Newmark-beta(gamma=0.5, beta=0.25)로 푸는
파이썬 함수를 만들어 주세요.

조건:
- 입력: m_kg, k_N_per_m, zeta, x0_m, v0_m_per_s, dt_s, t_end_s
- 모든 변수 이름에 단위를 표기할 것 (SI 기본단위: kg, N, m, s)
- numpy만 사용
- 함수 안에서 이론 해석해와 비교해 최대 상대오차를 함께 반환할 것
```

마지막 항목이 중요합니다. **검증을 코드에 심어 두면 AI가 틀렸을 때 즉시 드러납니다.**

---

## ⚠️ AI를 쓸 때의 수업 규칙 3가지

**규칙 1 — 숫자를 AI에게 계산시키지 않는다.**
"m=100ton, k=4000kN/m일 때 고유주기는?" 이렇게 묻지 마세요.
**계산하는 코드를 짜게 하고, 숫자는 그 코드가 내게** 하세요.
AI는 그럴듯한 숫자를 만들어 내며, 그게 맞는지 스스로 검사하지 않습니다.

**규칙 2 — 식·기준·상수는 출처를 확인한다.**
AI가 제시한 계수나 조항 번호(예: "KDS 41 17 00 4.3.2에 따르면")는
**교재나 원문을 직접 확인하기 전까지 가설**입니다. 실제로 존재하지 않는 조항을 만들어 내는
경우가 있습니다. 확인 못 하면 과제에 쓰지 마세요.

**규칙 3 — 단위는 변수 이름에 박는다.**
```python
k = 4000              # ✗ kN/m? N/m? N/mm? 다음 주의 나는 모른다
k_N_per_m = 4.0e6     # ✓ 읽는 순간 명확
assert k_N_per_m > 1e5, "N/m 단위인지 확인 — kN/m를 그대로 넣지 않았는가?"
```
동역학 과제 오답의 대부분은 이론이 아니라 **단위 환산**에서 나옵니다.

---

## 잘 되는지 확인 (2분)

1. `Ctrl + Shift + N` 으로 새 창 → `Ctrl + N` 으로 새 파일
2. `Ctrl + S` 로 바탕화면에 `test.py` 로 저장
3. 아래 한 줄을 타이핑
   ```python
   # 1부터 10까지 제곱수를 출력
   ```
4. Enter → **회색 글씨 제안이 뜨면 Copilot 정상**
5. `Tab` 으로 수락 → 오른쪽 위 **▷ 실행 버튼** 클릭 → 아래 터미널에 결과가 뜨면 Python 정상

둘 중 하나라도 안 되면 [06 — 오류 대응 사전](06-error-handbook.md) 을 보세요.

---

### 출처 및 확인일

- GitHub Docs, *Quickstart for GitHub Copilot* — 확장 설치, 로그인, Tab 수락, 채팅 단축키
  https://docs.github.com/en/copilot/get-started/quickstart
- 확인일: **2026-08-29**. 단축키·메뉴 이름은 VS Code 버전에 따라 달라질 수 있습니다.

**다음:** [03 — 첫 커밋 따라하기](03-first-commit-walkthrough.md)
