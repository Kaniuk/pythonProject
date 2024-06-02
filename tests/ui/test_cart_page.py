from modules.ui.page_objects.cart_page import CartPage
import pytest


@pytest.mark.ui
def test_check_product_added_to_cart():

    check_add_to_cart = CartPage()

    check_add_to_cart.go_to()

    check_add_to_cart.add_to_cart()

    check_add_to_cart.close()
