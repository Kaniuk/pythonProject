from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Find_post_office(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Find_post_office.URL)

    def try_find_post_office(self):
        hide_adv = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, "popup_info"))
        )
        button_elem = hide_adv.find_element(By.CLASS_NAME, "btn_x")
        button_elem.click()

        click_on_page = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[@class='timetable']",
                )
            )
        )
        click_on_page.click()

    def enter_info(self, city_id, city_name, post_office):
        find_input = self.driver.find_element(By.ID, "oCityFilter")
        find_input.send_keys(city_name)

        enter_city = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//li[@id='{city_id}']",
                )
            )
        )
        enter_city.click()

        time.sleep(5)

        enter_post_office = self.driver.find_element(By.ID, "oWarehouseFilter")
        enter_post_office.send_keys(post_office)

        enter_address = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//li[@data-warehouse-number='{post_office}']",
                )
            )
        )
        enter_address.click()

    def check_title(self, expected_title):
        assert self.driver.title == expected_title
