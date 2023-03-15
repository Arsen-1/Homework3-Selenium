from conftest import test_browser
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
def test_log_in(test_browser):
    wait = WebDriverWait(test_browser, 40)
    actions = ActionChains(test_browser)
    login = wait.until(condition.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    login.send_keys("Admin")
    password = test_browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password.send_keys("admin123")
    button = test_browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    my_info = wait.until(condition.visibility_of_element_located((By.XPATH, "//*[text()='My Info']")))
    assert not my_info.is_selected()
    my_info.click()
    wait.until(condition.visibility_of_element_located((By.XPATH, "//*[text()='License Expiry Date']")))
    first_name = wait.until(condition.visibility_of_element_located((By.CSS_SELECTOR, "[name='firstName']")))
    assert not first_name.is_selected()
    first_name.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    first_name.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    first_name.send_keys("aaaaaa")
    middle_name = wait.until(condition.visibility_of_element_located((By.CSS_SELECTOR, "[name='middleName']")))
    assert not middle_name.is_selected()
    middle_name.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    middle_name.send_keys("aaaaaa")
    last_name = wait.until(condition.visibility_of_element_located((By.CSS_SELECTOR, "[name='lastName']")))
    assert not last_name.is_selected()
    last_name.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    last_name.send_keys("aaaaaa")
    nick_name = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[1]
    assert not nick_name.is_selected()
    nick_name.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    nick_name.send_keys("nick_name")
    employee_id = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[1]
    assert not employee_id.is_selected()
    employee_id.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    employee_id.send_keys("empl_id")
    other_id = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[2]
    assert not other_id.is_selected()
    other_id.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    other_id.send_keys("other_id")
    license_number = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[2]
    assert not license_number.is_selected()
    license_number.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    license_number.send_keys("lic_num")
    licence_date = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[3]
    assert not licence_date.is_selected()
    licence_date.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    selected_date = "2001-06-28"
    licence_date.send_keys(selected_date)
    #licence_date.send_keys(Keys.RETURN)
    close_calendar = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "[class='orangehrm-horizontal-padding orangehrm-vertical-padding']")))
    assert not close_calendar.is_selected()
    close_calendar.click()
    ssn_number = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[5]
    assert not ssn_number.is_selected()
    ssn_number.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    ssn_number.send_keys("ssn_num")
    sin_number = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[6]
    assert not sin_number.is_selected()
    sin_number.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    sin_number.send_keys("sin_num")
    test_browser.execute_script('window.scrollBy(0, window.innerHeight * 0.5);')
    country = test_browser.find_elements(By.XPATH, "//*[@class='oxd-select-text-input']")[0]
    assert not country.is_selected()
    country.click()
    nationality = test_browser.find_elements(By.XPATH, "//*[@class='oxd-select-option']")[4]
    assert not nationality.is_selected()
    nationality.click()
    marital_status = test_browser.find_elements(By.XPATH, "//*[@class='oxd-select-text-input']")[1]
    assert not marital_status.is_selected()
    marital_status.click()
    marital_status_married = nationality = test_browser.find_elements(By.XPATH, "//*[@class='oxd-select-option']")[1]
    assert not marital_status_married.is_selected()
    marital_status_married.click()
    date_of_birth = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[8]
    assert not date_of_birth.is_selected()
    date_of_birth.click()
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    date_of_birth.send_keys("2000-10-22")
    gender = wait.until(condition.element_to_be_clickable((By.CSS_SELECTOR, "[class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input']")))
    assert not gender.is_selected()
    gender.click()
    military_service = test_browser.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")[9]
    assert not military_service.is_selected()
    military_service.click()
    military_service.send_keys("Yes")
    smoker = test_browser.find_element(By.CSS_SELECTOR, "[class='oxd-icon bi-check oxd-checkbox-input-icon']")
    assert not smoker.is_selected()
    smoker.click()
    save = test_browser.find_elements(By.CSS_SELECTOR, "[class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")[0]
    assert not save.is_selected()
    save.click()
    time.sleep(5)