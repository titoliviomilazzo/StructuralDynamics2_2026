# 예제 3 — 수업 실습 노트북 (SDOF 진동 · Newmark · 응답스펙트럼)

```
jupyter notebook sdof_newmark_spectrum.ipynb
```

VS Code에서는 파일을 열고 커널로 Python을 고르면 됩니다. Colab에서도 그대로 돌아갑니다
(지진파 파일이 없으면 이 저장소에서 자동으로 받습니다).

필요 패키지: `pip install numpy matplotlib` (+ Jupyter 또는 VS Code Jupyter 확장)

---

## 구성

| 파트 | 주제 | 검증 셀 |
| --- | --- | --- |
| 1 | SDOF 감쇠 자유진동, 대수감쇠율로 감쇠비 역산 | Newmark vs 해석해, 감쇠비 복원 |
| 2 | 조화하중, 동적증폭계수, 공진 응답의 성장 | 피크 Rd, 정상진폭 |
| 3 | Newmark-β 안정성과 주기 늘어남 | 임계 dt/Tn = 0.551, 주기오차 이론식 |
| 4 | El Centro 1940 EW 지반운동에 대한 SDOF 응답 | — |
| 5 | 탄성 응답스펙트럼 (D, PSV, PSA) | Newmark vs 구간선형 정확해, T→0에서 PSA = PGA |

각 파트 끝에 `✏️ 실습` 셀이 있습니다. 값을 바꾸기 **전에** 결과를 예측하고 실행하세요.
모든 검증 셀은 `[PASS]`/`[FAIL]`을 찍습니다. 저장된 노트북은 전부 `[PASS]` 상태입니다.

## 데이터

`data/ElCentro_EW.txt` — 시간[s], 가속도[g] 두 열. GroundMotionScaling 저장소 예제와 같은 파일입니다.
시간열에 반올림 잡음이 있어 노트북에서 0.02 s 등간격으로 재샘플링합니다.
PGA가 약 0.18 g로 문헌에서 흔히 인용하는 값(약 0.21 g)과 달라, 처리 버전 확인이 필요합니다.
