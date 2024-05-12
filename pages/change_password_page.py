from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage
from utilities.locators import ChangePasswordLocatorFields


class ChangePasswordPage(BasePage):
    """
    ChangePasswordPage class inherits from the BasePage class and represents the change password page of the application.
    It provides methods to interact with the change password page elements and perform actions like changing the password,
    and getting the confirmation error message.
    """

    def __init__(self, driver):
        """
        Constructor method to initialize ChangePasswordPage class.
        It takes a driver as a parameter, assigns the ChangePasswordLocatorFields to the locate attribute,
        and calls the constructor of the BasePage class passing the driver to it.
        :param driver: WebDriver
        """
        self.locate = ChangePasswordLocatorFields
        super().__init__(driver)

    def change_password(self, password, confirm_password):
        """
        Method to change the password.
        It takes a new password and a confirmation password as parameters, sets the new password and the confirmation password,
        clicks the continue button, and then returns an instance of the MyAccountPage class.
        :param password: str
        :param confirm_password: str
        :return: MyAccountPage
        """
        self.set(self.locate.password_field, password)
        self.set(self.locate.confirm_password_field, confirm_password)
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)

    def get_confirmation_error_message(self):
        """
        Method to get the text of the confirmation error message.
        :return: str
        """
        return self.get_text(self.locate.confirmation_error_message)
