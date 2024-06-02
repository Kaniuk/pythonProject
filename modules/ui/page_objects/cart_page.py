from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    URL = "https://allo.ua/ua/fitnes-braslety/mi-smart-band-8-champagne-gold-bhr7166gl.html"

    def __init__(self, width=1920, height=1080) -> None:
        super().__init__(width, height)

    def go_to(self):
        self.driver.get(CartPage.URL)

    def add_to_cart(self):
        btn = self.driver.find_element(
            By.XPATH,
            "//button[@id='product-buy-button']",
        )
        btn.click()

        modal_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='v-modal__cmp cart-popup checkout_modal']//ul",
                )
            )
        )

        list_items = modal_cart.find_elements(By.TAG_NAME, "li")

        assert len(list_items) > 0
