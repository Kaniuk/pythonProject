from modules.ui.page_objects.filter_page import FilterPage
import pytest


@pytest.mark.ui
def test_filter():

    filter_page = FilterPage()

    filter_page.go_to()

    filter_page.toggle_and_check_currency("$")

    filter_page.close()
