# 03 — 첫 커밋 따라하기

**목표:** 내 저장소를 만들고 → 내 컴퓨터로 가져오고 → 코드를 짜고 → 서버에 올린다.
**소요:** 20분. 이 문서를 끝내면 GitHub의 80%를 쓸 줄 아는 상태가 됩니다.

> 이 문서는 **한 줄도 건너뛰지 말고** 순서대로 따라 하세요. 개념 설명은 [00 문서](00-why-github.md)에 있습니다.

---

## STEP 0 — Git 엔진 설치 (5분, 딱 한 번)

VS Code는 **계기판**이고, 실제 이력 관리를 하는 **엔진**이 Git입니다.
엔진을 깔아야 계기판이 동작합니다. **설치만 하고 이 프로그램을 열 일은 없습니다.**

1. **https://git-scm.com/download/win** 접속 → 자동으로 다운로드 시작
2. 설치 파일 실행 → **선택지가 계속 나와도 전부 Next**, 마지막에 Install
   (기본값으로 충분합니다. 뭘 고를지 고민하지 마세요)
3. 설치 후 **VS Code를 완전히 껐다가 다시 켭니다** ← 이거 안 하면 인식 안 됩니다

### 확인
VS Code 왼쪽 세로 막대에 **가지 갈라진 아이콘**(Source Control, `Ctrl+Shift+G`)을 눌렀을 때
"Git이 설치되지 않았습니다" 경고가 없으면 성공입니다.

---

## STEP 1 — 내 실습 저장소 만들기 (3분)

수업 저장소와 별개로, **본인이 마음껏 실험할 개인 저장소**를 하나 만듭니다.

1. 브라우저에서 **https://github.com/new**
2. 입력
   - **Repository name**: `dynamics-practice`
   - **Description**: `응용동역학 실습` (선택)
   - **Public / Private**: ⚠️ **Private** 선택 (개인 연습용)
   - ☑ **Add a README file** ← **반드시 체크.** 안 하면 빈 저장소라 clone이 까다로워집니다
   - **Add .gitignore**: 드롭다운에서 **Python** 선택
3. **Create repository**

만들어진 페이지 주소가 `https://github.com/내아이디/dynamics-practice` 입니다. 이 주소를 씁니다.

## STEP 2 — 내 컴퓨터로 가져오기 (Clone, 3분)

1. VS Code에서 `Ctrl + Shift + P` → 명령 팔레트가 위에 뜸
2. `git clone` 이라고 치고 → **Git: Clone** 선택
3. 저장소 주소 붙여넣기: `https://github.com/내아이디/dynamics-practice`
4. **저장할 폴더 위치**를 묻습니다
   - 권장: `C:\Users\<본인계정>\Documents\GitHub`
   - ⚠️ **OneDrive·구글드라이브 동기화 폴더 안에는 두지 마세요.** 동기화 충돌로 파일이 깨집니다
5. 다 받으면 "Would you like to open the cloned repository?" → **Open**

### 확인
VS Code 왼쪽 탐색기(Explorer)에 `DYNAMICS-PRACTICE` 폴더와 그 안의 `README.md`가 보이면 성공.

## STEP 3 — 코드 작성하기 (5분)

실제 동역학 계산을 하나 만들어 봅니다.

1. 탐색기 영역에서 **새 파일 아이콘** 클릭 → 파일명 `sdof.py` 입력 후 Enter
2. 아래 내용을 그대로 붙여넣고 `Ctrl + S` 저장

```python
"""SDOF 감쇠 자유진동 — 고유주기와 감쇠 특성 계산"""
import numpy as np

# --- 입력 (SI 기본단위로 통일: kg, N, m, s) ---
m_kg = 1.0e5           # 100 ton = 1.0e5 kg
k_N_per_m = 4.0e6      # 4,000 kN/m = 4.0e6 N/m
zeta = 0.05            # 감쇠비 5% (무차원)

# --- 단위 방어 (틀린 단위를 넣으면 여기서 멈춘다) ---
assert 1e3 < m_kg < 1e8, f"m_kg={m_kg}: kg 단위가 맞는가? (ton을 그대로 넣지 않았는가)"
assert 1e5 < k_N_per_m < 1e10, f"k_N_per_m={k_N_per_m}: N/m가 맞는가? (kN/m를 그대로 넣지 않았는가)"
assert 0.0 <= zeta < 1.0, f"zeta={zeta}: 저감쇠 범위가 아니다"

# --- 계산 ---
wn_rad_per_s = np.sqrt(k_N_per_m / m_kg)
Tn_s = 2 * np.pi / wn_rad_per_s
wd_rad_per_s = wn_rad_per_s * np.sqrt(1 - zeta**2)
c_Ns_per_m = 2 * zeta * np.sqrt(k_N_per_m * m_kg)

print(f"고유각진동수 wn = {wn_rad_per_s:.4f} rad/s")
print(f"고유주기     Tn = {Tn_s:.4f} s")
print(f"감쇠고유주기 Td = {2*np.pi/wd_rad_per_s:.4f} s")
print(f"감쇠계수      c = {c_Ns_per_m:.3e} N*s/m")
```

3. **▷ 실행 버튼**(오른쪽 위) 클릭

`numpy를 찾을 수 없다`는 오류가 나면, 아래 터미널에 이 한 줄만 치세요.
```
pip install numpy
```

### 나오는 결과
```
고유각진동수 wn = 6.3246 rad/s
고유주기     Tn = 0.9935 s
감쇠고유주기 Td = 0.9947 s
감쇠계수      c = 6.325e+04 N*s/m
```

> 여기서 `assert` 세 줄이 이 코드의 핵심입니다.
> 만약 `k_N_per_m = 4000` (kN/m를 그대로 넣은 실수)이었다면 프로그램이 **그 자리에서 멈추고**
> 잘못된 주기 31초를 출력하지 않습니다. 이것이 수업 원칙 2번의 실제 모습입니다.

## STEP 4 — 커밋하기 (3분)

지금까지는 **내 컴퓨터에만** 있습니다. 이력에 남기고 서버에 올립니다.

1. 왼쪽 세로 막대 **가지 아이콘**(Source Control) 클릭 — 또는 `Ctrl + Shift + G`
2. **Changes** 목록에 `sdof.py` 가 `U`(Untracked) 표시로 보임
3. 파일 이름 위에 마우스를 올리면 **`+` 버튼**이 나타남 → 클릭
   → 파일이 **Staged Changes** 로 이동
   > `+` 는 "이번 커밋에 이 파일을 포함시킨다"는 뜻입니다. 도면 개정에 포함할 시트를 고르는 것.
4. 맨 위 **Message** 입력창에 커밋 메시지를 씁니다
   ```
   SDOF 고유주기·감쇠계수 계산 스크립트 추가
   ```
5. **✓ Commit** 버튼 클릭

### 좋은 커밋 메시지 / 나쁜 커밋 메시지

| ✓ 좋음 | ✗ 나쁨 |
| --- | --- |
| `SDOF 고유주기 계산 추가` | `수정` |
| `단위 검증 assert 3개 추가` | `ㅇㅇ` |
| `과제2: 대수감쇠율로 감쇠비 역산 구현` | `asdf` |
| `감쇠비 오타 수정 (0.5 → 0.05)` | `final_final` |

기준: **3주 뒤의 내가 읽고 무슨 작업이었는지 알 수 있는가.**

## STEP 5 — 서버에 올리기 (Push, 1분)

1. Source Control 패널 상단의 **⋯**(점 세 개) → **Push**
   또는 파란 **Sync Changes** 버튼 클릭
2. 처음이면 GitHub 인증 창이 뜰 수 있습니다 → 허용

### 확인 — 여기까지가 진짜 완료입니다
브라우저에서 `https://github.com/내아이디/dynamics-practice` 를 **새로고침**하세요.
`sdof.py` 가 보이고, 파일 옆에 방금 쓴 커밋 메시지가 보이면 **성공**입니다.

> ⚠️ **Commit만 하고 Push를 안 하는 것**이 초보자의 1위 실수입니다.
> Commit = 내 컴퓨터 이력에 도장. Push = 서버에 반영.
> 과제는 **Push까지 되어야** 제출로 인정됩니다.

---

## STEP 6 — 되돌리기 연습 (2분, 꼭 해 보세요)

이걸 한 번 해 봐야 "실수해도 괜찮다"는 감각이 생깁니다.

1. `sdof.py` 에서 `zeta = 0.05` 를 `zeta = 0.5` 로 바꾸고 저장
2. Source Control 패널에 `sdof.py` 가 `M`(Modified)로 나타남
3. 파일 이름 위 **↩ (Discard Changes)** 버튼 클릭 → 경고에 **Discard**
4. 파일이 **커밋했던 상태로 되돌아감**

이번엔 이미 커밋·푸시한 것을 되돌려 봅니다.

1. 브라우저에서 저장소 → 파일 위의 **History**(시계 아이콘) 클릭
2. 커밋 목록에서 아무거나 클릭하면 **그 시점의 전체 내용**을 볼 수 있음
3. 우측 **⋯ → View file** 로 그때 파일을 그대로 열람 / 복사

**이력이 남아 있는 한 잃어버리는 것은 없습니다.** 그래서 자주 커밋하는 겁니다.

---

## 앞으로의 반복 루틴 — 이것만 외우세요

```
1. Pull   (작업 시작 전, 최신화)
2. 작업   (코딩, Ctrl+S 자유롭게)
3. +      (커밋에 포함할 파일 선택)
4. 메시지 (한 줄로 무엇을 왜)
5. ✓      (Commit)
6. Push   (서버 반영)   ← 여기까지 해야 끝
```

하루에 3~5번 반복하면 몸에 붙습니다.

---

## 완료 체크리스트

- [ ] Git 설치 후 VS Code 재시작함
- [ ] 개인 저장소 `dynamics-practice`가 GitHub에 있다
- [ ] 내 컴퓨터 폴더에 clone 되어 있다 (OneDrive 밖에)
- [ ] `sdof.py` 실행해서 Tn = 0.9935 s 를 확인했다
- [ ] **브라우저에서** `sdof.py` 가 보인다 ← 이게 최종 증거
- [ ] Discard Changes로 되돌리기를 해 봤다

**다음:** [04 — Pull과 협업](04-pull-and-collaboration.md)
