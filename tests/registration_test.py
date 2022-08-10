import unittest
import time
from selenium.webdriver.common.by import By

from tests.ui_scripts.common_scripts import create_driver


class TestRegistration(unittest.TestCase):

    def test_registration_email_validation(self):
        driver = create_driver()
        driver.get('https://www.220-volt.ru/')
        self.open_registration_page(driver)

        email = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>span>#user_email')
        email.send_keys('hd22%^&*!u@mi.ru')
        password = driver.find_element(By.CSS_SELECTOR, '.box-inline.col-8>#password1')
        password.send_keys('913547dgsa')
        password_2 = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.box-inline.col-8>#password2')
        password_2.send_keys('913547dgsa')
        username = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.box-inline.col-8>#user_fullname')
        username.send_keys('Иванов Алексей Петрович')
        user_phone = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>span>#user_phone')
        user_phone.send_keys('89999999999')
        time.sleep(2)

        email_warning = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>#err_user_email')
        self.assertEqual('Неправильный email адрес', email_warning.text)

        driver.quit()

    def test_registration_easy_password_validation(self):
        driver = create_driver()
        driver.get('https://www.220-volt.ru/')
        self.open_registration_page(driver)

        email = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>span>#user_email')
        email.send_keys('ivant095@mail.ru')
        password = driver.find_element(By.CSS_SELECTOR, '.box-inline.col-8>#password1')
        password.send_keys('111111')
        password_2 = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.box-inline.col-8>#password2')
        password_2.send_keys('111111')
        username = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.box-inline.col-8>#user_fullname')
        username.send_keys('Иванов Алексей Петрович')
        user_phone = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>span>#user_phone')
        user_phone.send_keys('89999999999')
        time.sleep(2)

        password_warning = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>#err_password1')
        self.assertEqual('Пароль должен содержать от 8 до 32 символов', password_warning.text)

        password_warning_2 = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>#err_password2')
        self.assertEqual('Пароль должен содержать от 8 до 32 символов', password_warning_2.text)

        driver.quit()

    def open_registration_page(self, driver):
        enter = driver.find_element(By.CSS_SELECTOR, 'a>.header-panel-icon>.header-panel-user-icon')
        enter.click()
        time.sleep(2)
        reg = driver.find_element(By.ID, 'reg')
        reg.click()
        time.sleep(2)
