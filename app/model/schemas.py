from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from enum import Enum, IntEnum
from agno.media import Image

ResultStatus = Literal["pass", "fail", "error", "suspect"]

class CheckResult(BaseModel):
    ac_name: str
    result: ResultStatus
    confidence_level: float = Field(ge=0, le=1)
    reasoning_summary: Optional[str] = None
    notes: Optional[str] = None

class ImageSchema(BaseModel):
    url: str = Field(description="The image url")
    image: Image = Field(description="The image content in agno media format")