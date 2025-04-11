from fastapi import FastAPI, Request
from app.api.endpoints import rooms
import logging

app = FastAPI(
    title="Dormitory Room API",
    description="API для керування кімнатами гуртожитку",
    version="1.0.0"
)

# Логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_requests")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Роутери
app.include_router(rooms.router, prefix="/rooms", tags=["Rooms"])
