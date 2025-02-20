from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from db.init_db import Database
from routes.auth import router as auth_router
from routes.deepfake_route import deepfake_router
from contextlib import asynccontextmanager
from util.kafka_handler import KafkaHandler
# from util.newsfetcher import NewsFetcher
import asyncio
from kafka import KafkaConsumer
import json
import nest_asyncio
nest_asyncio.apply()
from pydantic import BaseModel
from Gemini.final import get_gemini_analysis
import os
from tempfile import NamedTemporaryFile
from routes.news_fetch import news_router
from routes.user_inputs import input_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create background tasks set
    background_tasks = set()
    yield
    # Shutdown: Clean up tasks
    for task in background_tasks:
        task.cancel()

# Update FastAPI initialization to use lifespan
app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=["authentication"])
app.include_router(deepfake_router, tags=["deepfake"])
app.include_router(news_router, tags=["news"])
app.include_router(input_router, tags=["user_inputs"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}

class NewsInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_news(news: NewsInput):
    try:
        gemini_analysis = get_gemini_analysis(news.text)
        return {
            "detailed_analysis": gemini_analysis
        }
    except Exception as e:
        return {"error": str(e)}, 500
    