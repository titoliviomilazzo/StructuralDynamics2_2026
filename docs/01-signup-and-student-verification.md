---
layout: default
title: "가입 + 학생 인증"
subtitle: "Copilot 무료화까지"
---

# 01 — GitHub 계정 생성과 학생 인증

**목표:** GitHub 계정을 만들고, 학생 인증을 신청해서 **Copilot을 무료로** 쓸 자격을 확보한다.
**소요:** 신청까지 20분. 승인은 신청 후 별도 대기.

> ⚠️ **먼저 읽을 것**
> 학생 인증은 **사람이 검토**합니다. 신청 즉시 되지 않습니다.
> 오늘 안에 신청만 해 두고, 승인 대기 중에 [02 문서](02-vscode-and-copilot.md)로 넘어가세요.
> 승인 전에도 Copilot **무료 등급**(월 2,000회 코드 제안 + 기본 채팅)은 쓸 수 있어서 수업 진행에 지장 없습니다.

---

## 준비물 (신청 전에 미리 챙기기)

- [ ] 본인 이메일 (개인 메일이어도 됨)
- [ ] 학교 이메일이 있다면 그것도 (`@dankook.ac.kr` 등)
- [ ] **재학 증명 서류 사진 또는 스캔 1장** — 아래 중 하나
  - 학생증 (현재 등록 학기·유효기간이 **보이게** 찍을 것)
  - 재학증명서 / 재적증명서
  - 수강신청 내역서 (이름·학교명·학기 표시)
  - 성적증명서
- [ ] 서류에 **본인 이름 · 학교명 · 현재 학기(또는 유효기간)** 세 가지가 다 보이는지 확인

> 계약학과라 학생증 발급이 늦어질 수 있습니다. 그럴 땐 **재학증명서(포털 출력)** 가 가장 확실합니다.

---

## STEP 1 — 계정 만들기 (5분)

1. 브라우저에서 **https://github.com/signup** 접속
2. 순서대로 입력
   - **Email**: 평소 쓰는 메일 (나중에 학교 메일 추가 가능)
   - **Password**: 15자 이상 권장
   - **Username**: ⚠️ **신중하게.** 이건 공개 주소가 됩니다 (`github.com/내아이디`)
3. 이메일로 온 **8자리 코드** 입력 → 가입 완료
4. 요금제 선택 화면이 나오면 **Free** 선택

### Username 정하는 법

이건 나중에 이력서·명함에 적히는 주소입니다. 처음에 제대로 정하세요.

| 권장 | 피할 것 |
| --- | --- |
| `jtnoh`, `jt-noh`, `noh-jungtae` | `xXdarkstarXx`, `asdf1234` |
| `jtnoh-dku` (소속 표시) | `kim` 같은 너무 흔한 것 (이미 선점됨) |
| 영문 소문자 + 하이픈 | 언더스코어·특수문자 남발 |

> 변경은 가능하지만, 이전 주소로 걸린 링크가 전부 깨집니다. 처음에 정하세요.

## STEP 2 — 학교 이메일 추가 (3분, 선택이지만 강력 권장)

학교 메일이 등록돼 있으면 인증 통과율이 올라갑니다.

1. 우측 상단 프로필 사진 → **Settings**
2. 좌측 **Emails**
3. **Add email address** 에 학교 메일 입력 → **Add**
4. 학교 메일함에서 확인 링크 클릭

## STEP 3 — 학생 인증(GitHub Education) 신청 (10분)

1. **https://github.com/settings/education** 접속
   (또는 Settings → 좌측 메뉴 아래쪽 **Education benefits**)
2. **Start an application** 클릭
3. 양식 작성
   - **학교명**: `Dankook University` (한글 아닌 영문. 목록에서 자동완성되면 그걸 선택)
   - **학교 이메일**: STEP 2에서 등록한 것 선택 (없으면 개인 메일 + 서류로 진행)
   - **본인 신분**: `Student` 선택
   - **용도**: 한 줄이면 충분. 예시 →
     `Graduate coursework in structural dynamics; using Git for assignment version control and Copilot for Python scripting.`
4. **서류 업로드**: 준비물에서 찍어 둔 사진 첨부
   - 흐릿하거나 잘리면 반려됩니다. 업로드 전 **글씨가 읽히는지** 확인
5. 브라우저가 **위치 권한**을 요청하면 **허용**
   (학교 위치와 대조하는 절차가 있을 수 있습니다. 캠퍼스나 자택에서 신청하면 무난)
6. **Submit** → 접수 메일 도착

### 승인되면 무엇이 생기나

- **GitHub Copilot Student** — 무료. 이 수업에서 쓸 AI가 여기 포함됩니다.
- Student Developer Pack — 여러 개발 도구 무료 이용권 묶음 (수업 필수는 아님)

승인 메일은 등록한 주소로 옵니다. 스팸함도 확인하세요.

## STEP 4 — 승인 후 Copilot 켜기 (2분)

1. **https://github.com/settings/copilot** 접속
2. 학생 요금제가 활성 상태인지 확인
3. 활성화 버튼이 보이면 클릭 (결제수단 요구되면 학생 인증이 아직 반영 안 된 것 — 하루 기다렸다 재확인)

---

## 반려되면

반려 메일에 사유가 적혀 옵니다. 대개 셋 중 하나입니다.

| 사유 | 조치 |
| --- | --- |
| 서류가 안 읽힘 / 날짜 안 보임 | 밝은 곳에서 정면으로 다시 촬영. 유효기간·학기가 나오게 |
| 현재 등록 여부 확인 불가 | 학생증 대신 **이번 학기 발급 재학증명서**로 교체 |
| 학교 도메인 미인식 | 서류 재제출로 진행. 그래도 안 되면 GitHub Education Support에 학교명·홈페이지·도메인 기재해 문의 |

재신청에 횟수 제한은 없습니다. **서류만 바꿔서 다시 넣으면 됩니다.**

---

## 완료 확인 체크리스트

- [ ] `github.com/내아이디` 주소로 내 프로필이 열린다
- [ ] Settings → Emails 에 메일이 **Verified** 로 표시된다
- [ ] Settings → Education benefits 에 신청 상태가 보인다
- [ ] (승인 후) Settings → Copilot 에 학생 요금제가 표시된다

---

### 출처 및 확인일

- GitHub Docs, *Apply to GitHub Education as a student* — 자격 요건·인정 서류·신청 경로
  https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student
- GitHub Docs, *Plans for GitHub Copilot* — 학생 무료 요금제, 무료 등급 월 2,000회 제한
  https://docs.github.com/en/copilot/get-started/plans
- 확인일: **2026-08-29**

> 심사 기간, 위치 권한 요구 여부는 공식 문서에 명시돼 있지 않습니다. 위 안내 중 그 두 항목은
> 운영 경험에 근거한 조언이며 확정 사실이 아닙니다. 화면 문구가 바뀌었다면 **버튼 위치가 아니라
> 단어**(Education, Start an application, Copilot)를 기준으로 찾으세요.

**다음:** [02 — VS Code와 Copilot 설치](02-vscode-and-copilot.md)
