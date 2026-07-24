from fastapi import APIRouter

from backend.app.api.routes.agent import router as agent_router
from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.info import router as info_router


api_router = APIRouter()

api_router.include_router(agent_router, tags=["agents"])
api_router.include_router(health_router, tags=["health"])
api_router.include_router(info_router, tags=["info"])