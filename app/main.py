import uvicorn
from fastapi import FastAPI

from app.config.settings import config
from app.routes import info, health

app = FastAPI()

app.include_router(health.router)
app.include_router(info.router)

def main() -> None:
    uvicorn.run("app.main:app", host=config.host, port=config.port, reload=config.reload)

if __name__ == "__main__":
    main()