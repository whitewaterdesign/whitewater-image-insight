from fastapi.testclient import TestClient
from app.__stubs__.settings import get_settings, config, Settings

import pytest

@pytest.fixture(autouse=True)
def set_test_env(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("OPEN_API_KEY", "dummy")
    monkeypatch.setenv("AGNO_API_KEY", "dummy")


@pytest.fixture
def test_client(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("app.config.settings.config", config)
    monkeypatch.setattr("app.config.settings.get_settings", get_settings)
    monkeypatch.setattr("app.config.settings.Settings", Settings)
    from app.main import app

    app.dependency_overrides[get_settings] = get_settings
    with TestClient(app) as client:
        yield client


