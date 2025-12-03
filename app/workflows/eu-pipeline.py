from prefect import flow, task

from app.repositories.image import ImageRepository
from app.service.image import ImageService

image_repository = ImageRepository()
image_service = ImageService(image_repository)

@task
def get_images():
    return image_service.get_images()

@flow
def run_eu_pipeline():
    images = get_images()
    print(images)

run_eu_pipeline()