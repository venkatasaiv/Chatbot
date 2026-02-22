import os
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

app = FastAPI(title="chat_app")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[Message] = []


class ChatResponse(BaseModel):
    reply: str


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not set")
    return OpenAI(api_key=api_key)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    messages = [
        {
            "role": "system",
            "content": "You are a concise and helpful assistant.",
        }
    ]

    for m in req.history[-12:]:
        messages.append({"role": m.role, "content": m.content})

    messages.append({"role": "user", "content": req.message})

    client = get_client()

    try:
        result = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.3,
        )
        reply = result.choices[0].message.content or ""
        return ChatResponse(reply=reply)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Chat request failed: {exc}")
