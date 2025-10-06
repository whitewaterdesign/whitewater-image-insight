from fastapi import APIRouter
from app.model.health import Health
router = APIRouter()

@router.get("/health")
async def health() -> Health:
    return {"status": "ok"}