import softest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Hard Assertions - Stop the test execution if the assertion fails and moves to the next annotation
# Soft Assertions - Continue execution after a failure and then fail the test at the end of the test

class AssertionsTest(softest.TestCase):
    def test_lambda_radio_button(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
        driver.find_element(By.XPATH,
                            "//h4[contains(text(),'Gender')]"
                            "//following::input[@value='Male']").click()
        driver.find_element(By.XPATH,
                            "//h4[contains(text(),'Age')]//following::input[@value='15 - 50']").click()
        driver.find_element(By.XPATH,
                            "//button[text() = 'Get values']").click()

        gender = driver.find_element(By.CSS_SELECTOR,
                                     ".genderbutton").text
        age_group = driver.find_element(By.CSS_SELECTOR,
                                        ".groupradiobutton").text

        self.soft_assert(self.assertEqual,
                         "Male", gender, "Gender Is Not Correct")
        self.soft_assert(self.assertTrue,
                         driver.title.__contains__("Selenium Grid Online"))
        self.soft_assert(self.assertIn,
                         "50", age_group, "Age Group Is Not Correct")
        self.assert_all()

        driver.quit()