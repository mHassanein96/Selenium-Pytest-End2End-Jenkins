from selenium import webdriver
from selenium.webdriver.common.by import By


# Hard Assertions - Stop the test execution if the assertion fails and moves to the next annotation
# Soft Assertions - Continue execution after a failure and then fail the test at the end of the test

def test_lambda_radio_button():
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

    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Male"))
    assert gender == "Male", "Gender Is Not Correct"
    assert driver.title.__contains__("Selenium Grid Online")
    assert "50" in age_group, "Age Group Is Not Correct"

    driver.quit()