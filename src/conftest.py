import pytest


@pytest.fixture
def valid_id():
    return "63d04bc2-179b-423b-98fe-7573fdee7363"


@pytest.fixture
def valid_full_url():
    return "http://sgh.com.sa/Organization/bff3aa1fbd3648619ac082357bf135db"


@pytest.fixture
def valid_datetime():
    return "2023-01-23T21:56:57.024682"


@pytest.fixture
def valid_date():
    return "2023-01-23"
