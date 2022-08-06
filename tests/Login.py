from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.220-volt.ru/')
driver.implicitly_wait(5)
enter = driver.find_element(By.CSS_SELECTOR, 'a>.header-panel-icon>.header-panel-user-icon')
enter.click()
email = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>div>#user_email')
email.send_keys('ivant095@yandex.ru')
password = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.mhbspace-10:nth-child(2)>input')
password.send_keys('K2nS9Qwp7')
enter_btn = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10:nth-child(3)>.box-inline.col-12.v-middle>button')
enter_btn.click()
text_to_be_present_in_element_value('.header-panel-item.header-user-wrapper>a>.header-panel-text.text-center', 'Иван Антонов')
driver.quit()