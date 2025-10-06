from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Test API"
    admin_email: str = "<EMAIL>"
    api_version: str = "0.0.test"
    items_per_user: int = 50
    openai_api_key: str = "dummy"
    agno_api_key: str = "dummy"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False

def get_settings():
    return Settings()

config = get_settings()