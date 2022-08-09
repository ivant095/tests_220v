from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.220-volt.ru/')
driver.implicitly_wait(5)
enter = driver.find_element(By.CSS_SELECTOR, 'a>.header-panel-icon>.header-panel-user-icon')
enter.click()
time.sleep(2)
reg = driver.find_element(By.ID, 'reg')
reg.click()
time.sleep(2)
email =driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>span>#user_email')
email.send_keys('hd22%^&*!u@mi.ru')
password = driver.find_element(By.CSS_SELECTOR,'.box-inline.col-8>#password1')
password.send_keys('111111')
password_2 = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.box-inline.col-8>#password2')
password_2.send_keys('111111')
user_name = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.box-inline.col-8>#user_fullname')
user_name.send_keys('Иванов Алексей Петрович')
user_phone = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>span>#user_phone')
user_phone.send_keys('89999999999')
time.sleep(2)
email_warning = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>#err_user_email')
email_warning_text = email_warning.text
assert email_warning_text == 'Неправильный email адрес'
time.sleep(2)
password_warning = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>#err_password1')
password_warning_text = password_warning.text
assert password_warning_text == 'Пароль должен содержать от 8 до 32 символов'
time.sleep(2)
password_warning_2= driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>#err_password2')
password_warning_2_text = password_warning_2.text
assert password_warning_text == 'Пароль должен содержать от 8 до 32 символов'
driver.quit()