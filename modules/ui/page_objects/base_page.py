from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self, width=1024, height=1080) -> None:
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )
        self.driver.set_window_size(width, height)

    def close(self):
        self.driver.close()
