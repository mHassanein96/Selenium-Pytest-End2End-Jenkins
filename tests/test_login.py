import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


@pytest.mark.integration
@pytest.mark.smoke
class TestLogin(BaseTest):
    """
    TestLogin class inherits from the BaseTest class and represents the test suite for the login functionality.
    It provides test methods to verify the login functionality with valid and invalid credentials.
    """

    def test_valid_credentials(self):
        """
        Test method to verify the login functionality with valid credentials.
        It creates an instance of the LoginPage class, sets the email address and password, clicks the login button,
        gets the title of the page, and asserts that the title is "My Account".
        """
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        actual_title = login_page.get_title()
        assert actual_title == "My Account"

    def test_invalid_credentials(self):
        """
        Test method to verify the login functionality with invalid credentials.
        It creates an instance of the LoginPage class, logs into the application with invalid email and password,
        gets the warning message, and asserts that the warning message contains "Warning".
        """
        login_page = LoginPage(self.driver)
        login_page.log_into_application(
            "Invalid Email", "Invalid Password")
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Warning")
