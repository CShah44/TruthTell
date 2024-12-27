from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from db.init_db import Database
from routes.auth import router as auth_router
from routes.fax import fax_router
from contextlib import asynccontextmanager
from .util.kafka_handler import KafkaHandler
from .util.newsfetcher import NewsFetcher
import asyncio
from kafka import KafkaConsumer
import json

kafka_handler = None
news_fetcher = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start up
    await Database.connect_db()
    global kafka_handler, news_fetcher
    
    kafka_handler = KafkaHandler()
    news_fetcher = NewsFetcher()
    
    # Start background tasks
    asyncio.create_task(kafka_handler.process_news())
    asyncio.create_task(news_fetcher.fetch_and_produce())
    
    yield
    # Shut down
    await Database.close_db()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=["authentication"])
app.include_router(fax_router, tags=["factcheck"])

@app.websocket("/ws/factcheck-stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    consumer = KafkaConsumer(
        'factcheck_results',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    try:
        for message in consumer:
            await websocket.send_json(message.value)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

@app.get("/health")
async def health_check():
    return {"status": "ok"}