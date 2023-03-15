import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


@pytest.fixture
def test_browser(request):
    #request.cls.x = 2
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    #request.cls.driver = driver
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    return driver