import os
import json

TMP_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "tmp")

class ImageRepositoryMeta(type):
    """
    This is a metaclass for ImageRepository, setting up a singleton instance
    and appropriate connection to the source of images
    """

    _instances = {}
    data = None

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            # mocking out a connection to db
            if ImageRepositoryMeta.data is None:
                with open(f"{TMP_DIR}/db/img-db.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    ImageRepositoryMeta.data = {img['id']: img['file_name'] for img in data}
                    ImageRepositoryMeta.data.update({img['url']: img['file_name'] for img in data})
            print("Creating new instance")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print("Using existing instance")
        return cls._instances[cls]

class ImageRepository(metaclass=ImageRepositoryMeta):
    """
    Image repository that can be used to get images by id or url
    and will be used as a tool for image processing
    """
    def get_image_by_url(self, url: str) -> bytes | None:
        if url not in ImageRepositoryMeta.data:
            return None
        # naive implementation, would be substituted by DB or s3 call
        with open(f"{TMP_DIR}/img/{ImageRepository.data[url]}", "rb") as image:
            f = image.read()
            return bytes(f)


    def get_image_by_id(self, id: str) -> bytes | None:
        if id not in ImageRepositoryMeta.data:
            return None
        # naive implementation, would be substituted by DB or s3 call
        with open(f"{TMP_DIR}/img/{ImageRepository.data[id]}", "rb") as image:
            f = image.read()
            return bytes(f)