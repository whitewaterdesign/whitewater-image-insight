from app.repositories.image import ImageRepository


def test_image_repository_create():
    instance1 = ImageRepository()
    instance2 = ImageRepository()
    assert instance1 == instance2
    assert instance1.get_image_by_id('13880993-bc7b-4926-bef2-760a7714ae94') is None
    assert instance1.get_image_by_url('dummy url') is None
    assert isinstance(instance1.get_image_by_id('875bd890-f968-48da-ad8d-c8fe74a1f8bf'), bytes)
    assert isinstance(instance1.get_image_by_url('https://www.ans-ns.edu.pl/'), bytes)
