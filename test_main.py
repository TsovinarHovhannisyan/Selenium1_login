import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Constants
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "haykabelyan1@gmail.com"
PASSWORD = "hayk123!@#"
NEW_PASSWORD = "hayk123!@#"


@pytest.fixture(scope="module")
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--headless") # Запускает Chrome в безголовом режиме, то есть без отображения графического интерфейса.
    chrome_options.add_argument("--disable-gpu") # Отключает аппаратное ускорение графики (GPU).
    chrome_options.add_argument("--no-sandbox") # Используется в окружениях вроде Docker или CI/CD, где пользователь, запускающий Chrome,
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.regression
@allure.feature('Login')
@allure.story('Invalid Login Attempt')
@allure.severity(allure.severity_level.CRITICAL)

def test_invalid_login(driver):
 with allure.step('Navigate to login page'):
    driver.get(LOGIN_URL)

 with allure.step('Enter invalid email'):
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("invalidemail@gmail.com")

 with allure.step('Enter invalid password'):
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys("invalidpassword")

 with allure.step('Click login button'):
    login_button = driver.find_element(By.ID, "send2")
    login_button.click()

 with allure.step('Verify error message'):
    time.sleep(3)  # Wait for the page to load
    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
    assert "Please wait and try again later" in error_message.text


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Login')
@allure.story('Successful Login')
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver):

 with allure.step('Navigate to login page'):
    driver.get(LOGIN_URL)

 with allure.step('Enter email'):
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(EMAIL)

 with allure.step('Enter password'):
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(PASSWORD)

 with allure.step('Click login button'):
    login_button = driver.find_element(By.ID, "send2")
    login_button.click()

 with allure.step('Verify login by checking account page URL'):
    time.sleep(3)  # Wait for the page to load
    assert driver.current_url == ACCOUNT_URL


@pytest.mark.regression
@allure.feature('Change Password')
@allure.story('Incorrect Current Password')
@allure.severity(allure.severity_level.CRITICAL)

def test_change_password_incorrect_current(driver):
 with allure.step('Navigate to account page'):
    driver.get(ACCOUNT_URL)

 with allure.step('Navigate to change password page'):
    change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
    change_password_link.click()

 with allure.step('Enter incorrect current password'):
    current_password_input = driver.find_element(By.ID, "current-password")
    current_password_input.send_keys("incorrectpassword")

 with allure.step('Enter new password'):
    new_password_input = driver.find_element(By.ID, "password")
    new_password_input.send_keys(NEW_PASSWORD)

 with allure.step('Confirm new password'):
    confirm_password_input = driver.find_element(By.ID, "password-confirmation")
    confirm_password_input.send_keys(NEW_PASSWORD)

 with allure.step('Save new password'):
    save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
    save_button.click()

 with allure.step('Verify error message'):
    time.sleep(3)  # Wait for the page to load
    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
    assert "The password doesn't match this account." in error_message.text


@pytest.mark.regression
@allure.feature('Change Password')
@allure.story('Password Mismatch')
@allure.severity(allure.severity_level.CRITICAL)

def test_change_password_mismatch(driver):
 with allure.step('Navigate to account page'):
    driver.get(ACCOUNT_URL)

 with allure.step('Navigate to change password page'):
    change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
    change_password_link.click()

 with allure.step('Enter current password'):
    current_password_input = driver.find_element(By.ID, "current-password")
    current_password_input.send_keys(PASSWORD)

 with allure.step('Enter new password'):
    new_password_input = driver.find_element(By.ID, "password")
    new_password_input.send_keys(NEW_PASSWORD)

 with allure.step('Enter mismatched confirmation password'):
    confirm_password_input = driver.find_element(By.ID, "password-confirmation")
    confirm_password_input.send_keys("mismatchedpassword")

 with allure.step('Save new password'):
    save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
    save_button.click()

 with allure.step('Verify error message'):
    time.sleep(3)  # Wait for the page to load
    error_message = driver.find_element(By.ID, "password-confirmation-error")
    assert "Please enter the same value again." in error_message.text


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Change Password')
@allure.story('Successful Password Change')
@allure.severity(allure.severity_level.CRITICAL)

def test_change_password(driver):
 with allure.step('Navigate to account page'):
    driver.get(ACCOUNT_URL)

 with allure.step('Navigate to change password page'):
    change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
    change_password_link.click()

 with allure.step('Enter current password'):
    current_password_input = driver.find_element(By.ID, "current-password")
    current_password_input.send_keys(PASSWORD)

 with allure.step('Enter new password'):
    new_password_input = driver.find_element(By.ID, "password")
    new_password_input.send_keys(NEW_PASSWORD)

 with allure.step('Confirm new password'):
    confirm_password_input = driver.find_element(By.ID, "password-confirmation")
    confirm_password_input.send_keys(NEW_PASSWORD)

 with allure.step('Save new password'):
    save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
    save_button.click()

 with allure.step('Verify password change success message'):
    time.sleep(3)  # Wait for the page to load
    success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")
    assert "You saved the account information." in success_message.text