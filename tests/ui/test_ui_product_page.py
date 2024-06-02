from modules.ui.page_objects.product_page import ProductPage
import pytest


@pytest.mark.ui
def test_check_click_on_link_to_product_page():

    check_product = ProductPage()

    check_product.go_to()

    check_product.check_product()

    check_product.close()
