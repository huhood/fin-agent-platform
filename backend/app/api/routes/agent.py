from fastapi import APIRouter
from backend.app.schemas.agent import AgentCreate

router = APIRouter()

@router.post("/agents", response_model=AgentCreate, response_model_exclude_unset=True)
async def create_agent(agent: AgentCreate):
    return agent