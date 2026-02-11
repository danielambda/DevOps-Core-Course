import pytest
from app import app


@pytest.fixture
def client():
    """
    Creates a Flask test client for each test.
    """
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client
