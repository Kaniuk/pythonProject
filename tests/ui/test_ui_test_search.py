from modules.ui.page_objects.search_field import SearchPage
import pytest


@pytest.mark.ui
def test_check_search_field_with_valid_data():

    search_functionality = SearchPage()

    search_functionality.go_to()

    search_functionality.try_search("Kuchenki indukcyjne")

    search_functionality.check_title(
        "▷ Kup kuchenki indukcyjne z E-Katalog - wszystkie ceny w sklepach internetowych Polski w Warszawie, Krakowie, Łodzi, Wrocławiu, Poznaniu"
    )

    search_functionality.close()
