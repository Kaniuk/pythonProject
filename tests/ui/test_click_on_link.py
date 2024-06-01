from modules.ui.page_objects.click_on_link import Click_on_link
import pytest


# @pytest.mark.ui
def test_check_click_link():

    check_click_link = Click_on_link()

    check_click_link.go_to()

    check_click_link.try_click_on_link()

    check_click_link.check_title("Вакансії – «Нова Пошта»| Доставка майбутнього")

    check_click_link.close()
