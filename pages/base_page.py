from selenium.webdriver.common.by import By


class BasePage:
    """
    BasePage class represents a base page object that contains methods common to all page objects.
    It provides methods to interact with the web elements and perform actions like finding an element,
    clicking an element, setting a value to an element, getting the text of an element, and getting the title of the page.
    """

    def __init__(self, driver):
        """
        Constructor method to initialize BasePage class.
        It takes a driver as a parameter and assigns it to the self.driver attribute.
        :param driver: WebDriver
        """
        self.driver = driver

    def find(self, *locator):
        """
        Method to find a web element on the page.
        It takes a locator as a parameter and returns the web element that matches the locator.
        :param locator: tuple
        :return: WebElement
        """
        return self.driver.find_element(*locator)

    def click(self, locator):
        """
        Method to click a web element on the page.
        It takes a locator as a parameter and clicks the web element that matches the locator.
        :param locator: tuple
        """
        self.find(*locator).click()

    def set(self, locator, value):
        """
        Method to set a value to a web element on the page.
        It takes a locator and a value as parameters, finds the web element that matches the locator,
        clears its current value, and sets the new value.
        :param locator: tuple
        :param value: str
        """
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        """
        Method to get the text of a web element on the page.
        It takes a locator as a parameter, finds the web element that matches the locator, and returns its text.
        :param locator: tuple
        :return: str
        """
        return self.find(*locator).text

    def get_title(self):
        """
        Method to get the title of the page.
        :return: str
        """
        return self.driver.title

    def click_right_menu_page(self, page_name):
        """
        Method to click a page on the right menu.
        It takes a page name as a parameter, finds the page on the right menu that matches the page name, and clicks it.
        :param page_name: str
        """
        page = By.XPATH, "//aside[@id='column-right']//a[text()=' " + page_name + "']"
        self.click(page)

    def page(self, page_name):
        """
        Method to get the locator of a page on the right menu.
        It takes a page name as a parameter and returns the locator of the page on the right menu that matches the page name.
        :param page_name: str
        :return: tuple
        """
        return By.XPATH, "//aside[@id='column-right']//a[text()=' " + page_name + "']"
