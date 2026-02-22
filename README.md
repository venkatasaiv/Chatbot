# Chat App (from scratch)

Minimal chatbot starter with:
- `FastAPI` backend (`/chat`)
- simple static frontend (`frontend/index.html`)
- OpenAI API integration

## 1) Setup

```bash
cd chat_app/backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create env file:

```bash
copy ..\\.env.example .env
```

Set your key in `.env`:

```env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini
```

## 2) Run backend

```bash
uvicorn main:app --reload --port 8000
```

## 3) Open frontend

Open `chat_app/frontend/index.html` in your browser.

The page posts to `http://localhost:8000/chat`.

## Notes
- In-memory history is session-local in browser.
- This is intentionally minimal so you can extend it with auth, DB memory, and RAG.
