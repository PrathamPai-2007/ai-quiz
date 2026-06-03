# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```powershell
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py

# Run all tests
python -m unittest discover -s tests

# Run a single test file
python -m unittest tests.test_quiz_engine
```

## Architecture

The app is a Streamlit quiz generator powered by Google Gemini. All state lives in `st.session_state`; there is no database for the core quiz flow (Supabase is used only for optional quiz history via `services/history_service.py`).

### Phase machine

The app routes UI by a `phase` string stored in session state. Valid phases are defined in `services/quiz_engine.py:QUIZ_PHASES`:

```
setup → generating → ready → in_progress → completed
```

`main.py` reads `phase` each render cycle and delegates to the appropriate screen renderer in `ui/`.

### Layered architecture

```
ui/           — Streamlit render functions only; no business logic
state.py      — Thin bridge: reads/writes QuizSession ↔ st.session_state
services/
  quiz_service.py   — Streamlit-aware orchestration (calls engine + state)
  quiz_engine.py    — Pure Python logic; no Streamlit imports
  gemini_service.py — Gemini API calls and prompt builders
  question_io.py    — JSON/CSV parsing and question validation
  export_service.py — JSON/PDF export (ReportLab)
  history_service.py — Supabase quiz-attempt persistence (requires auth_service)
models.py     — Question dataclass
constants.py  — Gemini model names, difficulty configs, scoring constants
```

**Key invariant**: `services/quiz_engine.py` must stay free of Streamlit imports. All engine functions operate on `QuizSession` (a plain dataclass) and return values or mutate the session in place. `state.py` is the only place that converts between `QuizSession` and `st.session_state`.

### Generation flow

Quiz generation is asynchronous within Streamlit's single-threaded model:

1. UI calls `quiz_service.queue_generation()` — sets `is_generating = True`, stores params in `pending_generation`, sets phase to `"generating"`.
2. Next render cycle, `main.py` detects `is_generating`, shows a loading overlay, and calls `quiz_service.process_pending_generation()`.
3. `process_pending_generation` calls Gemini, stores results, clears `pending_generation`, then calls `st.rerun()`.

Hint generation follows the same pattern via `queue_hint_generation` / `process_pending_hint_generation`.

### Scoring

- Correct answer: `+4`
- Incorrect answer: `−1`
- Unanswered: `0`

Each question can only be answered once (enforced in `quiz_engine.submit_answer_selection`).

## API Key Setup

Set `GEMINI_API_KEY` in `.streamlit/secrets.toml` or as an environment variable:

```powershell
$env:GEMINI_API_KEY = "your-key"
```

## Input Formats

**JSON**: array of `{question, options: [4 strings], correct_answer}` objects.  
**CSV**: columns `question, option1, option2, option3, option4, correct_answer`. `correct_answer` may be the option string or `A`/`B`/`C`/`D`.

## Notes

- `services/history_service.py` imports `services.auth_service`, which does not currently exist in the repo — history features will fail until that module is added.
- Generation is capped at 1–5 questions per request (enforced in `quiz_service.py`).
- `DESIGN-vercel.md` contains a Vercel-inspired design-language reference used to inform the app's UI styling.
