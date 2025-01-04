from __future__ import annotations

from dependency_sdk import Product as SDKProduct

import pytest
from unittest.mock import Mock, patch, ANY
from foodfacts.display_facts import DisplayFacts
from foodfacts.openfoodfact_adapter import OpenfoodfactAdapter
from foodfacts.main import FoodFact
from foodfacts.model import Product


### tests mocking dependency

@pytest.fixture
def mock_input():
    with patch("foodfacts.main.input") as mock_input:
        yield mock_input

@pytest.fixture
def mock_display():
    console_patch = patch("foodfacts.display_facts.Console")
    table_patch = patch("foodfacts.display_facts.Table")
    console_patch.start()
    table_mock = table_patch.start()
    yield table_mock
    console_patch.stop()
    table_patch.stop()

def test_compile_mock_dependency(mock_input):
    mock_api = Mock()
    mock_api.product.get.return_value = SDKProduct("Nutella", "0.539", "0.0063", "-", "0.0309", "e")
    mock_sdk = Mock()
    mock_sdk.build.return_value = mock_api
    app = FoodFact(OpenfoodfactAdapter(mock_sdk), DisplayFacts())
    mock_input.return_value = "nutella"

    app.ask_and_display_data()

def test_values_are_properly_formated(mock_input, mock_display):
    mock_api = Mock()
    mock_api.product.get.return_value = SDKProduct("Nutella", "0.539", "0.0063", "-", "0.0309", "e")
    mock_sdk = Mock()
    mock_sdk.build.return_value = mock_api
    app = FoodFact(OpenfoodfactAdapter(mock_sdk), DisplayFacts())
    mock_input.return_value = "nutella"

    app.ask_and_display_data()

    mock_display.return_value.add_row.assert_any_call('energy', '0.539')
    mock_display.return_value.add_row.assert_any_call('protein', '6.300g')
    mock_display.return_value.add_row.assert_any_call('fiber', '-')
    mock_display.return_value.add_row.assert_any_call('fat', '30.900g')
    mock_display.return_value.add_row.assert_any_call('nutriscore', 'e')


class FakeOpenFoodFact:
    class FakeProduct:
        def get(self, product_id: str):
            return {
                "59032823": SDKProduct("Nutella", "0.539", "0.0063", "-", "0.0309", "e"),
                "3229820019307": SDKProduct("Flocons d'avoines", "0.539", "0.0063", "-", "0.0309", "e")
            }[product_id]
    
    @property
    def product(self) -> FakeOpenFoodFact.FakeProduct:
        return FakeOpenFoodFact.FakeProduct()

def test_display_change_according_to_input(mock_input):
    mock_sdk = Mock()
    mock_sdk.build.return_value = FakeOpenFoodFact()
    mock_display = Mock()
    app = FoodFact(OpenfoodfactAdapter(mock_sdk), mock_display)
    mock_input.return_value = "nutella"

    app.ask_and_display_data()

    mock_display.display.assert_called_once_with(Product("Nutella", "0.539", ANY, ANY, ANY, ANY))

    mock_input.return_value = "flocons d'avoines"
    mock_display.reset_mock()

    app.ask_and_display_data()    

    mock_display.display.assert_called_once_with(Product("Flocons d'avoines", "0.539", ANY, ANY, ANY, ANY))



### integration tests

def test_adapter_retrieve_successfully_nutella_data():
    adapter = OpenfoodfactAdapter()

    adapter.get_data("nutella")

def test_adapter_retrieve_properly_formatted_nutella_data():
    adapter = OpenfoodfactAdapter()

    product = adapter.get_data("nutella")

    assert product.energy == "0.539"
    assert product.protein == "0.0063"
    assert product.fiber == "0.0035"
    assert product.fat == "0.0309"
    assert product.nutriscore == "e"

def test_adapter_succeed_if_no_fiber():
    adapter = OpenfoodfactAdapter()

    product = adapter.get_data("miel")

    assert product.name == "Miel de Fleurs BIO liquide Doseur 500g"
    assert product.energy == "0.32"
    assert product.fiber == "-"

def test_adapter_retrieve_according_to_product_name():
    adapter = OpenfoodfactAdapter()

    product1 = adapter.get_data("nutella")

    assert product1.name == "nutella"

    product2 = adapter.get_data("flocons d'avoines")

    assert product2.name == "Flocons d'avoine"

