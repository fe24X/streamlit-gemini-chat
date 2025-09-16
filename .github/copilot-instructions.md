# Copilot Instructions for My Streamlit AI App

## Project Overview
- This is a Streamlit-based AI chat app integrating Google Gemini for conversational and NLU tasks.
- Main files:
  - `GenAiApp.py`: Streamlit UI, chat logic, Gemini model integration, NLU invocation.
  - `nlu.py`: NLU service using Gemini to extract intent/entities from user prompts.
  - `requirements.txt`: Lists dependencies (`streamlit`, `google.generativeai`).

## Architecture & Data Flow
- User interacts via Streamlit chat UI (`GenAiApp.py`).
- Each user message is processed by `get_intent` (from `nlu.py`) to extract intent/entities.
- Both NLU output and Gemini model response are shown in the chat.
- Chat history is managed in `st.session_state.messages`.
- Gemini API key is loaded from `st.secrets["GEMINI_API_KEY"]` (see `.streamlit/secrets.toml`).

## Developer Workflows
- **Run app:** `streamlit run GenAiApp.py`
- **Install dependencies:** `pip install -r requirements.txt`
- **Configure secrets:** Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add your Gemini API key.
- **Test NLU logic:** Run `python nlu.py` for CLI-based NLU extraction tests.

## Project-Specific Patterns
- All Gemini API calls use the `gemini-1.5-flash-latest` model by default (can be changed in code).
- NLU extraction is always performed before generating model responses.
- Chat history is persisted in Streamlit session state for multi-turn context.
- Error handling for NLU JSON parsing returns `{intent: "parsing_error"}` with raw response.

## Integration Points
- External: Google Gemini API (via `google.generativeai`), Streamlit secrets for API key.
- Internal: `get_intent` function in `nlu.py` is the only NLU entry point.

## Conventions
- All user-facing logic is in `GenAiApp.py`.
- NLU logic is isolated in `nlu.py` for modularity/testing.
- Use markdown and JSON output for clarity in chat UI.

## Example: Adding a New Intent
- Update NLU prompt in `nlu.py` to describe new intent/entity extraction.
- No need to change UI logic unless new output format is required.

---
For questions or unclear patterns, review `GenAiApp.py`, `nlu.py`, and `README.md` for current conventions. If new workflows or patterns are introduced, update this file accordingly.
