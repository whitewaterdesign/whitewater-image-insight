from app.agentic.tools.image import ImageTools
from app.repositories.image import ImageRepository
from unittest.mock import create_autospec

def test_image_repository_create():
    repository_stub = create_autospec(ImageRepository, instance=True)
    repository_stub.get_image_by_id.return_value = b'fake_image_bytes'
    repository_stub.get_image_by_url.return_value = b'fake_image_bytes'


def test_gets_image_by_url_returns_tool_result_with_image():
    # Arrange
    repository_stub = create_autospec(ImageRepository, instance=True)
    repository_stub.get_image_by_url.return_value = b"image_bytes"
    image_tools = ImageTools(repository_stub)

    # Act
    result = image_tools.get_image_by_url("https://example.com/image")

    # Assert
    assert result.success is True
    assert result.message == "Image found"
    assert result.data.id == "https://example.com/image"
    assert result.data.content == b"image_bytes"

