from dataclasses import dataclass
from random import random
from enum import Enum
import openfoodfacts
from requests import ConnectionError
import logging
from dependency_sdk import SDKBuilder, SDKVersion, Product

logger = logging.getLogger(__name__)

NO_BUILDER_PROVIDED = None

class OpenfoodfactAdapter:
    def __init__(self, sdk_builder: SDKBuilder=NO_BUILDER_PROVIDED):
        if sdk_builder is NO_BUILDER_PROVIDED:
            self.sdk_builder = SDKBuilder()
        else:
            self.sdk_builder = sdk_builder

    def _get_product_id(self, product_name: str):
        return {
            "nutella": "3017620422003",
            "cantal": "3560070753741",
            "flocons d'avoines": "3229820019307",
        }[product_name]

    def get_data(self, product_name: str) -> Product:
        api = self.sdk_builder.build(SDKVersion.v1)
        product_id = self._get_product_id(product_name)
        product = api.product.get(product_id)
        return product
