import pytest

from pages.change_password_page import ChangePasswordPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


@pytest.mark.regression
@pytest.mark.smoke
class TestChangePassword(BaseTest):
    """
    TestChangePassword class inherits from the BaseTest class and represents the test suite for the change password functionality.
    It provides a test method to verify the change password functionality with invalid new password and confirmation password.
    """

    def test_changing_password(self):
        """
        Test method to verify the change password functionality with invalid new password and confirmation password.
        It creates instances of the LoginPage and ChangePasswordPage classes, sets the email address and password, clicks the login button,
        clicks the "Password" page on the right menu, changes the password with invalid new password and confirmation password,
        gets the confirmation error message, and asserts that the confirmation error message is "Password confirmation does not match password!".
        """
        login_page = LoginPage(self.driver)
        change_password_page = ChangePasswordPage(self.driver)
        expected_message = "Password confirmation does not match password!"
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        my_account_page = login_page.click_login_button()
        my_account_page.click_right_menu_page("Password")
        change_password_page.change_password(
            "InvalidPassword", "InvalidConfirmPassword")
        actual_message = change_password_page.get_confirmation_error_message()
        assert actual_message == expected_message
