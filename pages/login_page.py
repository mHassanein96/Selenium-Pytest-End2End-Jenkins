from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage


class LoginPage(BasePage):
    """
    LoginPage class inherits from the BasePage class and represents the login page of the application.
    It provides methods to interact with the login page elements and perform actions like setting email address,
    setting password, clicking the login button, and getting the warning message.
    """

    # Locators for the elements on the login page
    email_address_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//div[@id='content']//input[@value='Login']")
    warning_message = (By.CSS_SELECTOR, "#account-login .alert-danger")

    def __init__(self, driver):
        """
        Constructor method to initialize LoginPage class.
        It calls the constructor of the BasePage class and passes the driver to it.
        """
        super().__init__(driver)

    def set_email_address(self, email_address):
        """
        Method to set the email address in the email address field.
        :param email_address: str
        """
        self.set(self.email_address_field, email_address)

    def set_password(self, password):
        """
        Method to set the password in the password field.
        :param password: str
        """
        self.set(self.password_field, password)

    def click_login_button(self):
        """
        Method to click the login button.
        After clicking the login button, it returns an instance of the MyAccountPage class.
        :return: MyAccountPage
        """
        self.click(self.login_button)
        return MyAccountPage(self.driver)

    def log_into_application(self, email, password):
        """
        Method to log into the application.
        It sets the email address, sets the password, and then clicks the login button.
        :param email: str
        :param password: str
        """
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_message(self):
        """
        Method to get the text of the warning message.
        :return: str
        """
        return self.get_text(self.warning_message)
