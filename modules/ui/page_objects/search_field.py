from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    URL = "https://e-katalog.pl/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SearchPage.URL)

    def try_search(self, word):
        search_elem = self.driver.find_element(By.ID, "ek-search")

        search_elem.send_keys(word)

        btn_elem = self.driver.find_element(By.CLASS_NAME, "header_search_btn-submit")

        btn_elem.click()

    def check_title(self, expected_title):
        assert self.driver.title == expected_title
