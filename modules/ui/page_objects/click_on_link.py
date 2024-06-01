from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Click_on_link(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Click_on_link.URL)

    def try_click_on_link(self):
        hide_adv = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, "popup_info"))
        )
        button_elem = hide_adv.find_element(By.CLASS_NAME, "btn_x")
        button_elem.click()

        check_page = self.driver.find_element(
            By.XPATH, "//a[@href='https://novaposhta.ua/all_jobs']"
        )
        check_page.click()

    def check_title(self, expected_title):
        print(f"Expected - {self.driver.title}")
        assert self.driver.title == expected_title
