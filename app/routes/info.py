from typing import Annotated
from fastapi import APIRouter
from fastapi import Depends, FastAPI

from app.config.settings import Settings, get_settings

router = APIRouter(prefix="/info")

app = FastAPI()


@router.get("/")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        'app_name': settings.app_name,
        'admin_email': settings.admin_email
    }