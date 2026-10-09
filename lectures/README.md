# 주차별 강의 노트북

수업 시간에 화면에 띄우고 같이 실행하는 Jupyter 노트북입니다.
주차 번호는 임시 순서입니다. 강의계획서가 확정되면 폴더 이름이 바뀔 수 있습니다.

## 실행 준비 (처음 한 번)

```bash
pip install numpy scipy matplotlib sympy pandas jupyter
```

VS Code에서 `.ipynb`를 열고 오른쪽 위 커널을 Python으로 고른 뒤 **Run All**을 누르세요.
노트북은 **자기 폴더 안의 데이터 파일**(`elcentro.txt` 등)을 읽습니다. 폴더 밖으로 노트북만 옮기면 `FileNotFoundError`가 납니다.

## 주차별 내용

| 폴더 | 노트북 | 다루는 것 | 데이터 |
| --- | --- | --- | --- |
| `W01_sdof_forced_vibration` | `01_Free_Forced_Vib_simulation` | 조화하중을 받는 M·C·K 응답, 동적증폭계수, 응답 애니메이션 | 없음 |
| `W02_mdof_eigen` | `02_eigenvalue` | 2층 전단건물 고유치·고유벡터, 초기조건 자유진동 | 없음 |
| `W03_response_spectrum` | `W03_응답스펙트럼_실습` | 응답스펙트럼 만들기 → 설계스펙트럼 → 건물주기 → 감쇠비(점성댐퍼) | 없음 (합성파) |
| | `6_ResponseSpectrum` | El Centro 시간이력, 변위·유사가속도 스펙트럼, 감쇠비 비교 | `elcentro.txt` |
| `W04_rs_analysis` | `7_RSAnalysis` | 다자유도 응답스펙트럼 해석, 모드별 응답과 SRSS 조합 | `elcentro.txt`, `elcenspec_xi005.dat` |
| `W05_newmark_beta` | `08_newmarkbeta` | 테일러급수 시각화 → Newmark-β 시간이력 해석 | `elcentro.txt` |
| `W06_fourier_psd` | `10_Fourier_PSD` | FFT 크기 → 진폭 → 파워 → Welch PSD, 자기상관 | `elcentro.txt` (계측 데이터는 아래 참고) |

## 참고

- `W06`의 계측 가속도 `setup2.txt`(4채널, 200 Hz, 11.6 MB)는 저장소에 넣지 않았습니다. 파일이 없으면 같은 형식의 **교육용 합성 데이터**로 자동 대체되어 끝까지 실행됩니다.
- `6_ResponseSpectrum`, `7_RSAnalysis`는 2026-10 수정본입니다(노트북 안 `[수정 2026-10]` 표시 참고).
- `examples/` 폴더의 `.py` 예제는 과제 형식(이론해 vs 수치해 검증)의 견본이고, 여기 `lectures/`는 수업 시연용입니다.
