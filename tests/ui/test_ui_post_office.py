from modules.ui.page_objects.find_post_office import Find_post_office
import pytest


@pytest.mark.ui
def test_post_office():

    post_office = Find_post_office()

    post_office.go_to()

    post_office.try_find_post_office()

    post_office.enter_info("lidb5c8980-391c-11dd-90d9-001a92567626", "Сміла", 6063)

    post_office.check_title(
        "Пошук відділення за номером або за населеним пунктом | «Нова Пошта»| Доставка майбутнього"
    )

    post_office.close()
