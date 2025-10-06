import uvicorn
from fastapi import FastAPI
from typing import Annotated
from fastapi import Depends

from app.config.settings import config, Settings, get_settings
from app.routes import info, health

app = FastAPI()

app.include_router(health.router)
app.include_router(info.router)

@app.get("/")
async def root(settings: Annotated[Settings, Depends(get_settings)]):
    return {"message": f"Welcome to version {settings.api_version} of {settings.app_name}"}

def main() -> None:
    uvicorn.run("app.main:app", host=config.host, port=config.port, reload=config.reload)

if __name__ == "__main__":
    main()