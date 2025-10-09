from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools

from app.agentic.tools.image_simple import get_image_by_id, get_image_by_url
from app.config.settings import config
from app.agentic.instructions.agents import analysis_instructions, analysis_description
from app.model.schemas import CheckResult

image_analysing_agent = Agent(
    name="Image analysing agent",
    model=OpenAIChat(
        id="gpt-4o-mini",
        api_key=config.openai_api_key,
    ),
    tools=[get_image_by_id, get_image_by_url, ReasoningTools(add_instructions=True, enable_analyze=True)],
    description=analysis_description,
    stream_intermediate_steps=True,
    instructions=analysis_instructions,
    output_schema=CheckResult
)

if __name__ == "__main__":
    image_analysing_agent.print_response("7faa2eca-b948-427f-8b0b-fef54c416407", stream=True)