from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FastAPI"
    admin_email: str = "<EMAIL>"
    items_per_user: int = 50
    openai_api_key: str
    agno_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()