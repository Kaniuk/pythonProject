import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


@pytest.mark.ui
def test_check_incorrect_username():
    # Create a WebDriver object for managing the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Open the GitHub login page
        driver.get("https://github.com/login")

        # Find the field where we will input user name or email address
        login_elem = driver.find_element(By.ID, "login_field")

        # Enter invalid data in user name field or email address field
        login_elem.send_keys("name@mistakeinemail.com")

        pass_elem = driver.find_element(By.ID, "password")

        pass_elem.send_keys("wrong password")

        btn_elem = driver.find_element(By.NAME, "commit")

        btn_elem.click()

        # Check that page name is awaited page name
        assert driver.title == "Sign in to GitHub · GitHub"
        # time.sleep(3)

    finally:
        # Close the browser
        driver.close()
