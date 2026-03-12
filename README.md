# FastAPI Chatbot with OpenAI Integration

**A full-stack conversational AI app built from scratch — FastAPI backend with a `/chat` REST endpoint, OpenAI GPT integration, and a lightweight static frontend. Designed as a minimal, extensible base for production chatbot systems.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=flat&logo=html5&logoColor=white)

---

## What This Is

A minimal but production-structured chatbot app built from scratch using:

- **FastAPI** for the backend REST API (`/chat` endpoint)
- **OpenAI API** (GPT-4.1-mini) for LLM responses
- **Static HTML frontend** that communicates with the backend over HTTP
- **In-memory conversation history** scoped to the browser session
- **`.env` configuration** for API key management — no hardcoded credentials

The architecture is intentionally lean so it can be extended with auth, database-backed memory, RAG pipelines, or streaming responses.

---

## Project Structure

```
Chatbot/
├── backend/
│   ├── main.py             # FastAPI app — defines /chat endpoint
│   ├── requirements.txt    # Python dependencies
│   └── ...
├── frontend/
│   └── index.html          # Static chat UI — posts to localhost:8000/chat
├── .env.example            # Environment variable template
├── .gitignore
└── README.md
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend Framework | FastAPI |
| ASGI Server | Uvicorn |
| LLM Provider | OpenAI API (GPT-4.1-mini) |
| Frontend | HTML / JavaScript (static) |
| Configuration | python-dotenv / .env |
| Language | Python 3.8+ |

---

## Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/venkatasaiv/Chatbot.git
cd Chatbot
```

### 2. Set up the backend

```bash
cd backend
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure your OpenAI API key

```bash
# From the project root
copy .env.example .env        # Windows
cp .env.example .env          # Mac/Linux
```

Edit `.env` and set your key:

```
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini
```

### 4. Start the backend

```bash
uvicorn main:app --reload --port 8000
```

The API will be live at `http://localhost:8000`.

### 5. Open the frontend

Open `frontend/index.html` directly in your browser. It sends chat messages to `http://localhost:8000/chat` and displays responses in the UI.

---

## API

### `POST /chat`

Accepts a user message and returns a GPT-generated response.

**Request body:**
```json
{
  "message": "What is machine learning?"
}
```

**Response:**
```json
{
  "response": "Machine learning is a subset of artificial intelligence..."
}
```

Conversation history is maintained in-memory for the duration of the browser session.

---

## Extending This Project

This repo is deliberately minimal. Natural next steps:

- **Database memory** — persist conversation history with PostgreSQL or Redis
- **Auth** — add user sessions with JWT or OAuth
- **Streaming** — use OpenAI's streaming API for real-time token-by-token responses
- **RAG pipeline** — connect a vector database (e.g. Pinecone, ChromaDB) for document-grounded responses
- **Deployment** — containerize with Docker and deploy to GCP Cloud Run or AWS Lambda

---

## Why This Matters

Building a working REST API that wraps an LLM and serves a frontend demonstrates core skills for ML Engineering roles: API design, LLM integration, environment configuration, and a path to production deployment. This is the foundational pattern behind most production AI products.

---

## Author

**Venkatasai Vudatha** — Data Analyst & ML Engineer
📧 Vudatha.sai@gmail.com
🔗 [linkedin.com/in/venkatasaivudatha04](https://www.linkedin.com/in/venkatasaivudatha04/)
📍 Dallas, TX

---

## License

MIT License
