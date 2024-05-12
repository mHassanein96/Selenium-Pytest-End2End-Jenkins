import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print("Start Test With Automatic Fixture")


@pytest.fixture(scope="function")   # scope of the fixture (class, module, package, session) shows when the fixture
# run and ends, if it's function it will run and end for every function.
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.ID, "input-email") \
        .send_keys("mhassanein@gmail.com")
    driver.find_element(By.ID, "input-password") \
        .send_keys("123456")
    driver.find_element(By.XPATH,
                        "//input[@value='Login']").click()
    print("Log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Logout").click()
    print("Log Out")


@pytest.mark.usefixtures("setup_teardown")
def test1_order_history_title():
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Order").click()
    assert driver.title == "Order History"
    print("Test 1 Is Complete")


@pytest.mark.usefixtures("setup_teardown")
def test2_change_password_title():
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Password").click()
    assert driver.title == "Change Password"
    print("Test 2 Is Complete")
