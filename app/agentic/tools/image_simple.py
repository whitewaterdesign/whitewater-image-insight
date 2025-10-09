from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.function import ToolResult
from agno.tools.reasoning import ReasoningTools

from app.agentic.instructions.agents import analysis_instructions, analysis_description
from app.config.settings import config
from app.repositories.image import ImageRepository


def return_image_artifact(image: bytes | None, image_id: str) -> ToolResult:
    if image is None:
        return ToolResult(
            content="Image not found"
        )

    image_artifact = Image(
        id=image_id,
        content=image
    )

    return ToolResult(
        images=[image_artifact],
        content="Image found"
    )

image_repository = ImageRepository()

@tool(
    name="get_image_by_id",
    description="Use this function to get images by id",
)
def get_image_by_id(image_id: str) -> ToolResult:
    """
    Use this function to get images by id

    Args:
        image_id (str): the id of the image - e.g. 258c86a5-4aea-490c-89f5-33441784bdd2

    Returns:
        ToolResult: the image artifact
    """
    image = image_repository.get_image_by_id(image_id)

    return return_image_artifact(image, image_id)

@tool(
    name="get_image_by_url",
    description="Use this function to get images by url",
)
def get_image_by_url(image_url: str) -> ToolResult:
    """
    Use this function to get images by id

    Args:
        image_url (str): the url of the image - e.g. https://example.com/image

    Returns:
        ToolResult: the image artifact
    """
    image = image_repository.get_image_by_url(image_url)

    return return_image_artifact(image, image_url)


if __name__ == "__main__":
    agent = Agent(
        name="Image analysing agent",
        model=OpenAIChat(
            id="gpt-4o-mini",
            api_key=config.openai_api_key,
        ),
        tools=[get_image_by_id, get_image_by_url, ReasoningTools(add_instructions=True,enable_analyze=True)],
        description=analysis_description,
        stream_intermediate_steps=True,
        instructions=analysis_instructions,
        markdown=True,
    )
    agent.print_response("7faa2eca-b948-427f-8b0b-fef54c416407", stream=True)