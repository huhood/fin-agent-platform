from fastapi import APIRouter
from backend.app.schemas.info import InfoResponse

router = APIRouter()

@router.get("/info", response_model=InfoResponse)
async def get_info():
    return InfoResponse(
        name="fin-agent-platform",
        version="0.1.0"
    )