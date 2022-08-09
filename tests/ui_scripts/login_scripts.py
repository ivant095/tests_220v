import time

from selenium.webdriver.common.by import By


def press_login_button(driver):
    login_button = driver.find_element(By.CSS_SELECTOR, 'a>.header-panel-icon>.header-panel-user-icon')
    login_button.click()
    time.sleep(3)


def fill_username_password(driver, username, password):
    email_input = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>div>#user_email')
    email_input.send_keys(username)
    password_input = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.mhbspace-10:nth-child(2)>input')
    password_input.send_keys(password)


def login(driver, username, password):
    driver.get('https://www.220-volt.ru/')
    press_login_button(driver)
    fill_username_password(driver, username, password)
    enter_button = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10:nth-child(3)>.box-inline.col-12.v-middle>button')
    enter_button.click()
    time.sleep(2)
