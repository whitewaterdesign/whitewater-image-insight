from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from typing import Any, Callable, Dict
from agno.tools.function import ToolResult
from agno.media import Image
from agno.tools import Toolkit

from app.agentic.instructions.agents import analysis_instructions
from app.repositories.image import ImageRepository
from app.config.settings import config


# W.I.P.!!

class ImageTools(Toolkit):
    image_repository: ImageRepository

    def __init__(self, image_repository: ImageRepository):
        super().__init__(name="image_tools", tools=[self.get_image_by_id, self.get_image_by_url])
        self.image_repository = image_repository

    def __return_image_artifact(self, image: bytes | None, image_id: str) -> ToolResult:
        if image is None:
            return ToolResult(
                success=False,
                message="Image not found"
            )

        image_artifact = Image(
            id=image_id,
            content=image
        )

        return ToolResult(
            success=True,
            message="Image found",
            data=image_artifact
        )

    @tool(
        name="get_image_by_id",
        description="Use this function to get images by id",
    )
    def get_image_by_id(self, image_id: str) -> ToolResult:
        """
        Use this function to get images by id

        Args:
            image_id (str): the id of the image - e.g. 258c86a5-4aea-490c-89f5-33441784bdd2

        Returns:
            ToolResult: the image artifact
        """
        image = self.image_repository.get_image_by_id(image_id)

        return self.__return_image_artifact(image, image_id)


    def get_image_by_url(self, image_url: str) -> ToolResult:
        """
        Use this function to get images by id

        Args:
            image_url (str): the url of the image - e.g. https://example.com/image

        Returns:
            ToolResult: the image artifact
        """
        image = self.image_repository.get_image_by_url(image_url)

        return self.__return_image_artifact(image, image_url)

def get_image_by_id(image_repository: ImageRepository):
    def _get_image_by_id(image_id: str) -> ToolResult:


if __name__ == "__main__":
    image_repository = ImageRepository()
    image_tools = ImageTools(image_repository)
    agent = Agent(
        name="Image analysing agent",
        model=OpenAIChat(
            id="gpt-4o",
            api_key=config.openai_api_key,
        ),
        tools=[image_tools],
        description=analysis_description,
        instructions=analysis_instructions,
        markdown=True,
    )
    agent.run("https://www.gov.pl/web/gov/fundusze-europejskie-portal-informacyjny")