import pytest

from apps.customers.models import Customer


@pytest.fixture
def customers_mock_data(db, mixer):
    return mixer.cycle(4).blend(Customer)
