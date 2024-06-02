from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


class ProductPage(BasePage):
    URL = "https://wkruk.pl/"

    def __init__(self, width=1920, height=1080) -> None:
        super().__init__(width, height)

    def go_to(self):
        self.driver.get(ProductPage.URL)

    def check_product(self):

        accept_cookie = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, "CybotCookiebotDialog"))
        )
        button_elem = accept_cookie.find_element(
            By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
        )
        button_elem.click()

        time.sleep(1)
        a_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[@href='https://wkruk.pl/bizuteria']")
            )
        )
        li_elem = a_elem.find_element(By.XPATH, "./..")

        actions = ActionChains(self.driver)
        actions.move_to_element(li_elem).perform()

        time.sleep(1)

        a_elem_subcategory_item = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[@href='https://wkruk.pl/bizuteria/nowosci']")
            )
        )
        a_elem_subcategory_item.click()
        time.sleep(1)

        link = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//ul[@class='products js--products']//a[@class='js--gtm-product-click']",
                )
            )
        )
        link.click()

        product_page_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[@class='product__data__name']")
            )
        )
        assert product_page_element.is_displayed() is True
