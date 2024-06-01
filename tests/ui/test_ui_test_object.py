from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


# @pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Creation page object
    sign_in_page = SignInPage()

    # Open  gitHub login page https://github.com/login
    sign_in_page.go_to()

    # Enter invalid data in user name field or email address field
    sign_in_page.try_login("name@mistakeinemail.com", "wrong password")

    # Check that page name is awaited page name
    sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close the browser
    sign_in_page.close()
