from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FilterPage(BasePage):
    URL = "https://lun.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(FilterPage.URL)

    time.sleep(3)

    def toggle_and_check_currency(self, currency):

        click_on = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/uk/нерухомість-києва']"))
        )
        click_on.click()

        btn_elem = self.driver.find_element(
            By.XPATH, "//div[@data-modal-trigger='filters']"
        )
        btn_elem.click()

        check_box = self.driver.find_element(
            By.XPATH, "//input[@name='currency_switcher_checkbox']"
        )
        toggler = check_box.find_element(By.XPATH, "./..")
        toggler.click()

        min_price_el = toggler.find_element(By.XPATH, "./../..//div[@data-value-min]")

        assert currency in min_price_el.text

    def check_price(self, currency):

        div_element = self.driver.find_element(By.CLASS_NAME, "ButtonRefresh-content")
        div = div_element.find_element(By.XPATH, "//div")

        assert currency in div.text
