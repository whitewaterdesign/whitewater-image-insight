from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team

from app.config.settings import config
from app.model.schemas import CheckResult
from app.agentic.agents.check_result import structured_output_agent
from app.agentic.agents.analyser import image_analysing_agent

image_analysis_team = Team(
    name="Image analysis team",
    model=OpenAIChat(
        id="gpt-4o-mini",
        api_key=config.openai_api_key,
        temperature=0.25
    ),
    members=[image_analysing_agent, structured_output_agent],
    instructions=[
        'You are a team of image analysis agents.',
        'After analyzing an image, you return a structured output.'
    ],
    markdown=True,
    debug_mode=True
)

if __name__ == "__main__":
    image_analysis_team.print_response("875bd890-f968-48da-ad8d-c8fe74a1f8bf", )