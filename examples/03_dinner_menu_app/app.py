from __future__ import annotations

import random

import streamlit as st

from menu_data import CUISINES, MENU_CATALOG, MenuItem


st.set_page_config(
    page_title="오늘 저녁 뭐 먹지?",
    page_icon="🍽️",
    layout="centered",
)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #fffdf8 0%, #fff5eb 100%);
        }
        .block-container {
            max-width: 860px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }
        .hero-card, .result-card {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(238, 180, 116, 0.45);
            border-radius: 24px;
            box-shadow: 0 20px 45px rgba(148, 90, 38, 0.08);
            padding: 1.4rem 1.4rem 1.6rem;
        }
        .result-card {
            margin-top: 1rem;
        }
        .badge {
            display: inline-block;
            background: #fff1d6;
            color: #8a4b14;
            border-radius: 999px;
            padding: 0.3rem 0.85rem;
            font-size: 0.92rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        .result-title {
            font-size: 2rem;
            font-weight: 800;
            color: #40210f;
            margin-bottom: 0.25rem;
        }
        .result-subtitle {
            color: #70411b;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        .food-art {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 0.5rem;
            margin-bottom: 0.25rem;
            padding: 0.75rem;
            background: linear-gradient(180deg, #fffdf6 0%, #fff3db 100%);
            border-radius: 20px;
        }
        .food-art svg {
            width: min(100%, 280px);
            height: auto;
        }
        div[data-baseweb="radio"] > div {
            gap: 0.5rem;
        }
        div[data-baseweb="radio"] label {
            background: rgba(255, 250, 242, 0.95);
            border: 1px solid #efc38f;
            border-radius: 999px;
            padding: 0.4rem 0.95rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


if "selected_cuisine" not in st.session_state:
    st.session_state.selected_cuisine = CUISINES[0]
if "recommendation" not in st.session_state:
    st.session_state.recommendation = None
if "recommended_cuisine" not in st.session_state:
    st.session_state.recommended_cuisine = None


def pick_menu(cuisine: str) -> MenuItem:
    return random.choice(MENU_CATALOG[cuisine])


def recommend_selected_menu() -> None:
    st.session_state.recommendation = pick_menu(st.session_state.selected_cuisine)
    st.session_state.recommended_cuisine = st.session_state.selected_cuisine


def render_food_image(item: MenuItem) -> None:
    if item.image_path.exists():
        svg = item.image_path.read_text(encoding="utf-8")
        st.markdown(f'<div class="food-art">{svg}</div>', unsafe_allow_html=True)
        return

    st.warning("이미지 파일을 찾지 못했어요. 아래 메뉴 이름으로 먼저 골라 보세요.")
    st.markdown('<div class="food-art" style="font-size: 4rem;">🍲</div>', unsafe_allow_html=True)


st.markdown(
    """
    <div class="hero-card">
        <h1 style="margin-bottom:0.25rem; color:#40210f;">오늘 저녁 뭐 먹지? 🍽️</h1>
        <p style="margin:0; color:#70411b; line-height:1.7;">
            먹고 싶은 분위기를 고른 뒤 <strong>추천하기</strong>를 누르면
            오늘 저녁 메뉴를 한국어로 바로 추천해 드려요.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.subheader("1. 먹고 싶은 종류를 골라 주세요")
selected = st.radio(
    "저녁 종류 선택",
    CUISINES,
    key="selected_cuisine",
    horizontal=True,
    label_visibility="collapsed",
)

st.caption(f"선택한 메뉴 종류: **{selected}**")

recommend_col, again_col = st.columns([1, 1])
with recommend_col:
    st.button("추천하기", type="primary", use_container_width=True, on_click=recommend_selected_menu)
with again_col:
    st.button("다시 추천받기", use_container_width=True, on_click=recommend_selected_menu)

recommendation = st.session_state.recommendation
if recommendation is None:
    st.info("아직 추천 결과가 없어요. 원하는 종류를 고르고 추천을 시작해 보세요!")
else:
    recommended_cuisine = st.session_state.recommended_cuisine or selected
    st.markdown(
        f"""
        <div class="result-card">
            <div class="badge">{recommended_cuisine}</div>
            <div class="result-title">오늘의 추천: {recommendation.name}</div>
            <div class="result-subtitle">{recommendation.subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_food_image(recommendation)
    st.success("마음에 들면 오늘 저녁은 이 메뉴로 결정해 보세요!")
