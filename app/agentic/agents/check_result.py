from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from textwrap import dedent

from app.agentic.tools.image_simple import get_image_by_id, get_image_by_url
from app.config.settings import config
from app.model.schemas import CheckResult

structured_output_agent = Agent(
    name="CheckResult Structured Output Agent",
    model=OpenAIChat(
        id="gpt-4o-mini",
        api_key=config.openai_api_key,
        temperature=0.25

    ),
    description="You return a structured output from the result of an image analysis",
    output_schema=CheckResult
)