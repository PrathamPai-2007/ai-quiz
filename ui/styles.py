import streamlit as st  # type: ignore
import streamlit.components.v1 as components  # type: ignore


APP_STYLES = """
<style>
/* ─── Font (Inter as open-source Geist stand-in; Geist Mono → JetBrains Mono) ─── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

/* ─── Design tokens (Vercel / DESIGN.md) ─── */
:root {
    --ink:             #171717;
    --body-color:      #4d4d4d;
    --mute:            #888888;
    --hairline:        #ebebeb;
    --hairline-strong: #a1a1a1;
    --canvas:          #ffffff;
    --canvas-soft:     #fafafa;
    --canvas-soft-2:   #f5f5f5;
    --link:            #0070f3;
    --error:           #ee0000;

    --option-height:    132px;
    --option-font-size: 16px;
    --option-padding-y: 12px;
    --option-padding-x: 16px;
    --option-row-gap:   12px;
}

/* ─── Global: font & page background ─── */
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section.main {
    font-family: Inter, system-ui, -apple-system, sans-serif !important;
    background-color: var(--canvas-soft) !important;
    color: var(--ink) !important;
}

/* ─── Headings ─── */
h1, h2, h3,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    font-family: Inter, system-ui, sans-serif !important;
    font-weight: 600 !important;
    color: var(--ink) !important;
}

h1, [data-testid="stMarkdownContainer"] h1 {
    font-size: 32px !important;
    line-height: 40px !important;
    letter-spacing: -1.28px !important;
}

h2, [data-testid="stMarkdownContainer"] h2 {
    font-size: 24px !important;
    line-height: 32px !important;
    letter-spacing: -0.96px !important;
}

h3, [data-testid="stMarkdownContainer"] h3 {
    font-size: 20px !important;
    line-height: 28px !important;
    letter-spacing: -0.6px !important;
}

/* ─── Main content area top padding ─── */
[data-testid="stMainBlockContainer"] {
    padding-top: 48px !important;
    padding-bottom: 64px !important;
}

/* ─── Question box ─── */
.question-box {
    background: var(--canvas);
    color: var(--ink);
    border: 1px solid var(--hairline);
    box-shadow: 0px 1px 1px #00000005, 0px 2px 2px #0000000a;
    border-radius: 12px;
    padding: 40px 32px;
    text-align: center;
    font-size: 24px;
    font-weight: 600;
    line-height: 32px;
    letter-spacing: -0.96px;
    margin-bottom: 24px;
    font-family: Inter, system-ui, sans-serif;
}

/* ─── Global button base ─── */
.stButton > button {
    width: 100%;
    border-radius: 100px;
    font-family: Inter, system-ui, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    padding: 10px 16px;
    transition: background-color 0.12s ease, border-color 0.12s ease;
    cursor: pointer;
}

/* Primary pill — ink fill */
.stButton > button[kind="primary"] {
    background-color: var(--ink) !important;
    color: #ffffff !important;
    border: none !important;
}

.stButton > button[kind="primary"]:hover:not(:disabled) {
    background-color: #333333 !important;
}

.stButton > button[kind="primary"]:disabled {
    background-color: var(--canvas-soft-2) !important;
    color: var(--mute) !important;
    border: 1px solid var(--hairline) !important;
}

/* Secondary / default — white with hairline */
.stButton > button:not([kind="primary"]) {
    background-color: var(--canvas) !important;
    color: var(--ink) !important;
    border: 1px solid var(--hairline) !important;
}

.stButton > button:not([kind="primary"]):hover:not(:disabled) {
    background-color: var(--canvas-soft-2) !important;
    border-color: var(--hairline-strong) !important;
}

.stButton > button:not([kind="primary"]):disabled {
    background-color: var(--canvas-soft) !important;
    color: var(--mute) !important;
    border: 1px solid var(--hairline) !important;
}

/* ─── Answer option buttons — force 100% width ─── */
.st-key-answer_0,
.st-key-answer_1,
.st-key-answer_2,
.st-key-answer_3,
.st-key-empty_answer_0,
.st-key-empty_answer_1,
.st-key-empty_answer_2,
.st-key-empty_answer_3,
.st-key-answer_0 .stButton,
.st-key-answer_1 .stButton,
.st-key-answer_2 .stButton,
.st-key-answer_3 .stButton,
.st-key-empty_answer_0 .stButton,
.st-key-empty_answer_1 .stButton,
.st-key-empty_answer_2 .stButton,
.st-key-empty_answer_3 .stButton,
.st-key-answer_0 button,
.st-key-answer_1 button,
.st-key-answer_2 button,
.st-key-answer_3 button,
.st-key-empty_answer_0 button,
.st-key-empty_answer_1 button,
.st-key-empty_answer_2 button,
.st-key-empty_answer_3 button,
.st-key-answer_0 button > div,
.st-key-answer_1 button > div,
.st-key-answer_2 button > div,
.st-key-answer_3 button > div,
.st-key-empty_answer_0 button > div,
.st-key-empty_answer_1 button > div,
.st-key-empty_answer_2 button > div,
.st-key-empty_answer_3 button > div {
    width: 100% !important;
}

.st-key-option_row_1 {
    margin-bottom: var(--option-row-gap);
}

/* Answer option button style — canvas card with hairline border */
.st-key-answer_0 .stButton > button,
.st-key-answer_1 .stButton > button,
.st-key-answer_2 .stButton > button,
.st-key-answer_3 .stButton > button,
.st-key-empty_answer_0 .stButton > button,
.st-key-empty_answer_1 .stButton > button,
.st-key-empty_answer_2 .stButton > button,
.st-key-empty_answer_3 .stButton > button {
    height: var(--option-height) !important;
    padding: var(--option-padding-y) var(--option-padding-x) !important;
    font-size: var(--option-font-size) !important;
    font-weight: 500 !important;
    color: var(--ink) !important;
    background-color: var(--canvas) !important;
    border: 1px solid var(--hairline) !important;
    border-radius: 8px !important;
    white-space: normal;
    word-wrap: break-word;
    line-height: 1.4;
    display: block;
    text-align: center;
    box-shadow: 0px 1px 1px #00000005;
}

.st-key-answer_0 .stButton > button:hover,
.st-key-answer_1 .stButton > button:hover,
.st-key-answer_2 .stButton > button:hover,
.st-key-answer_3 .stButton > button:hover {
    background-color: var(--canvas-soft-2) !important;
    border-color: var(--hairline-strong) !important;
}

/* font-size passthrough for nested elements inside answer buttons */
.st-key-answer_0 .stButton > button p,
.st-key-answer_0 .stButton > button span,
.st-key-answer_1 .stButton > button p,
.st-key-answer_1 .stButton > button span,
.st-key-answer_2 .stButton > button p,
.st-key-answer_2 .stButton > button span,
.st-key-answer_3 .stButton > button p,
.st-key-answer_3 .stButton > button span,
.st-key-empty_answer_0 .stButton > button p,
.st-key-empty_answer_0 .stButton > button span,
.st-key-empty_answer_1 .stButton > button p,
.st-key-empty_answer_1 .stButton > button span,
.st-key-empty_answer_2 .stButton > button p,
.st-key-empty_answer_2 .stButton > button span,
.st-key-empty_answer_3 .stButton > button p,
.st-key-empty_answer_3 .stButton > button span {
    font-size: inherit;
    line-height: inherit;
    margin: 0;
}

/* ─── Option feedback divs (post-submit) ─── */
.option-feedback {
    height: var(--option-height);
    width: 100%;
    box-sizing: border-box;
    border-radius: 8px;
    padding: var(--option-padding-y) var(--option-padding-x);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
    font-size: var(--option-font-size);
    font-weight: 500;
    line-height: 1.4;
    word-break: break-word;
    border: 1px solid transparent;
    font-family: Inter, system-ui, sans-serif;
}

.option-feedback__label {
    display: block;
    width: 100%;
    margin: 0;
}

.option-feedback--neutral {
    background-color: var(--canvas-soft-2);
    color: var(--body-color);
    border-color: var(--hairline);
}

.option-feedback--correct {
    background-color: #dcfce7;
    color: #14532d;
    border-color: #bbf7d0;
}

.option-feedback--wrong {
    background-color: #fee2e2;
    color: #7f1d1d;
    border-color: #fecaca;
}

/* ─── Quiz nav buttons (Back / Next / Hint / Generate) ─── */
.st-key-quiz_back .stButton > button,
.st-key-quiz_next .stButton > button,
.st-key-quiz_hint .stButton > button,
.st-key-quiz_generate .stButton > button {
    height: 48px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    margin-top: 16px;
    border-radius: 100px !important;
    padding: 0 16px !important;
}

/* ─── Score display ─── */
.score-display {
    font-family: Inter, system-ui, sans-serif;
    font-size: 20px;
    font-weight: 600;
    letter-spacing: -0.6px;
    line-height: 28px;
    text-align: center;
    margin-bottom: 24px;
    padding: 16px 24px;
    background-color: var(--canvas);
    border: 1px solid var(--hairline);
    border-radius: 12px;
    color: var(--ink);
    box-shadow: 0px 1px 1px #00000005, 0px 2px 2px #0000000a;
}

/* ─── Sidebar ─── */
[data-testid="stSidebar"] {
    background-color: var(--canvas) !important;
    border-right: 1px solid var(--hairline) !important;
}

[data-testid="stSidebar"] .stButton > button {
    border-radius: 6px !important;
}

/* ─── Form inputs ─── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    border-radius: 6px !important;
    border-color: var(--hairline) !important;
    font-family: Inter, system-ui, sans-serif !important;
    font-size: 14px !important;
    color: var(--ink) !important;
    background-color: var(--canvas) !important;
}

/* ─── Captions ─── */
[data-testid="stCaptionContainer"] p,
small {
    color: var(--mute) !important;
    font-size: 12px !important;
    font-family: Inter, system-ui, sans-serif !important;
}

/* ─── Dividers ─── */
hr {
    border-color: var(--hairline) !important;
    margin: 16px 0 !important;
}

/* ─── Generation overlay ─── */
.generation-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.80);
    z-index: 999999;
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(8px);
}

.generation-overlay__panel {
    text-align: center;
    padding: 40px 48px;
    border-radius: 16px;
    background: rgba(23, 23, 23, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.10);
    box-shadow:
        0px 1px 1px #00000005,
        0px 8px 16px -4px #0000000a,
        0px 24px 32px -8px #0000000f;
}

.generation-overlay__title {
    color: #ffffff;
    font-family: Inter, system-ui, sans-serif;
    font-size: 24px;
    font-weight: 600;
    letter-spacing: -0.96px;
    margin-bottom: 8px;
}

.generation-overlay__subtitle {
    color: #888888;
    font-family: Inter, system-ui, sans-serif;
    font-size: 14px;
    font-weight: 400;
}
</style>
"""


def render_styles() -> None:
    st.markdown(APP_STYLES, unsafe_allow_html=True)


def render_generating_overlay() -> None:
    st.markdown(
        """
        <div class="generation-overlay">
            <div class="generation-overlay__panel">
                <div class="generation-overlay__title">Generating questions</div>
                <div class="generation-overlay__subtitle">Please wait...</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_close_sidebar_once() -> None:
    components.html(
        """
        <script>
        const closeSidebar = () => {
          const parentWindow = window.parent;
          if (!parentWindow) {
            return;
          }

          const sidebar = parentWindow.document.querySelector('[data-testid="stSidebar"]');
          if (!sidebar || sidebar.getAttribute('aria-expanded') !== 'true') {
            return;
          }

          const collapseButton = parentWindow.document.querySelector(
            '[data-testid="stSidebarCollapseButton"] button, button[aria-label="Close sidebar"]'
          );
          if (collapseButton) {
            collapseButton.click();
          }
        };

        requestAnimationFrame(closeSidebar);
        setTimeout(closeSidebar, 150);
        </script>
        """,
        height=0,
    )
