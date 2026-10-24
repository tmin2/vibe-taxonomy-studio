import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="VIBE TAXONOMY STUDIO",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 여백 제거 및 헤더/푸터 숨김
st.markdown(
    """
    <style>
        /* 기본 여백 완전 제거 */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header[data-testid="stHeader"] {
            display: none;
        }
        footer {
            visibility: hidden;
        }
        #MainMenu {
            visibility: hidden;
        }
        iframe {
            border: none;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML 파일 로드
html_path = Path(__file__).parent / "index.html"
if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # iframe 전체 화면 렌더링
    components.html(html_content, height=1350, scrolling=True)
else:
    st.error("index.html 파일을 찾을 수 없습니다.")
