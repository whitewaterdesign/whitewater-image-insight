from agno.media import Image

from app.model.schemas import ImageSchema
from app.repositories.image import ImageRepository


class ImageService:

    def __init__(self, image_repository: ImageRepository):
        self.image_repository = image_repository

    def get_images(self) -> list[ImageSchema]:
        image_urls = self.image_repository.get_image_urls()

        return [
            ImageSchema(
                url=image,
                image=Image(
                    content=self.image_repository.get_image_by_url(image)
                )
            ) for image in image_urls
        ]