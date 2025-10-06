from pydantic import BaseModel

from agno.media import Image

class Health(BaseModel):
    status: str