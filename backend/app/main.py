from fastapi import FastAPI
from backend.app.api.router import api_router
from backend.app.core.config import settings

app = FastAPI(title=settings.APP_NAME)
app.include_router(api_router, prefix="/api")

