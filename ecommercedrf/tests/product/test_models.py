# Using the AAA methodology for testing
# Arrange ( hardcoding or dynamically generate data using factory)
# Act
# Assert
import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange and Act - create dynamic data using factory
        factory_obj = category_factory(name="test_category")
        # Assert
        assert factory_obj.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange and Act - create dynamic data using factory
        factory_obj = brand_factory(name="test_brand")
        # Assert
        assert factory_obj.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange and Act - create dynamic data using factory
        factory_obj = product_factory(name="test_product")
        # Assert
        assert factory_obj.__str__() == "test_product"
