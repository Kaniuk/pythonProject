from modules.ui.page_objects.product_page import ProductPage
import pytest


@pytest.mark.ui
def test_check_product():

    check_click_link = ProductPage()

    check_click_link.go_to()

    check_click_link.check_product()

    check_click_link.close()
