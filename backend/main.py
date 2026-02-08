from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Enterprise AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.post("/chat")
async def chat(data: dict):
    message = data.get("message", "")
    return {
        "reply": f"AI received your message: {message}"
    }
