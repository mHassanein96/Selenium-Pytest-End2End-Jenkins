from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_lambda_ecommerce():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH,
                        "//input[@placeholder='Search For Products']") \
        .send_keys("iPhone")
    driver.find_element(By.XPATH,
                        "//button[text()='Search']").click()
    search_value = driver.find_element(By.XPATH,
                                       "//h1[contains(text(),'Search')]").text
    assert "iPhone" in search_value

    driver.quit()


def test_add_to_cart():
    result = 1
    print("Add To Cart")
    assert result == 3

