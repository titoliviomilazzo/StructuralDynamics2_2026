# 예제 3 — 한국어 저녁 메뉴 추천 앱

작은 Streamlit 앱으로, **한식 / 중식 / 양식 / 일식** 중 하나를 고른 뒤 `추천하기`를 누르면
해당 종류에서 저녁 메뉴 하나를 무작위로 추천합니다.

이 앱은 기존 구조동역학 예제와 분리된 **독립 데모 앱**이며,
기존 `01_sdof_free_vibration`, `02_harmonic_response` 예제 파일은 변경하지 않습니다.

---

## 실행 방법

```bash
cd /home/runner/work/StructuralDynamics2_2026/StructuralDynamics2_2026/examples/03_dinner_menu_app
pip install -r requirements.txt
streamlit run app.py
```

브라우저가 열리면 한국어 UI에서 메뉴 종류를 선택하고 `추천하기`를 누르세요.
`다시 추천받기` 버튼으로 같은 종류 안에서 다시 추천받을 수 있습니다.

---

## 파일 구성

```text
examples/03_dinner_menu_app/
├─ app.py                # Streamlit UI
├─ menu_data.py          # 메뉴/이미지 매핑 데이터
├─ requirements.txt      # 앱 실행 의존성
├─ test_menu_data.py     # 경량 데이터 검증 테스트
└─ assets/
   ├─ *.svg              # 로컬 음식 이미지 자산
   └─ ATTRIBUTION.md     # 이미지 출처 및 라이선스
```

---

## 테스트 / 검증

```bash
cd /home/runner/work/StructuralDynamics2_2026/StructuralDynamics2_2026
python -m unittest examples/03_dinner_menu_app/test_menu_data.py
python -m compileall examples/03_dinner_menu_app
```

---

## 이미지 출처

앱 이미지는 [Twemoji](https://github.com/twitter/twemoji) 저장소의 SVG 자산을 내려받아
로컬 `assets/` 폴더에 포함했습니다.
자세한 파일별 출처와 라이선스는 `assets/ATTRIBUTION.md`를 참고하세요.
