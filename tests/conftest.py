import logging

import pytest

from weather_service.app import create_app


@pytest.fixture(scope="module")
def log():
    """Set up logging as a pytest fixture."""
    logging.basicConfig()
    return logging.getLogger('weather-service-backend')



@pytest.fixture(scope="function")
def app():
    """
    """
    return create_app()
