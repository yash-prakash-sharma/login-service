from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import auth
from app.core.config import settings
from app.db.database import engine, Base

import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Wait for DB to be ready with a retry loop
max_retries = 5
for i in range(max_retries):
    try:
        # Create DB tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database connected successfully.")
        break
    except Exception as e:
        logger.warning(f"Database connection failed. Retrying... ({i+1}/{max_retries}) | Error: {e}")
        time.sleep(5)
else:
    logger.error("Failed to connect to the database after maximum retries.")

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/api/openapi.json",
)

# Standard permissive CORS setup for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Backend"}
