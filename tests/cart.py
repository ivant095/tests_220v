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
email = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>div>#user_email')
email.send_keys('ivant095@yandex.ru')
password = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.mhbspace-10:nth-child(2)>input')
password.send_keys('K2nS9Qwp7')
enter_btn = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10:nth-child(3)>.box-inline.col-12.v-middle>button')
enter_btn.click()
time.sleep(2)
driver.get('https://www.220-volt.ru/catalog-501170/')
count_1_cart = driver.find_element(By.CSS_SELECTOR, '.mhbspace-40.phbspace-20>div:nth-child(3)>div>a')
count_1_cart.click()
time.sleep(2)
close_1 = driver.find_element(By.CSS_SELECTOR, '.mhtspace-10>.box-inline.v-top.btn.btn-white.divider.pvspace-25.phspace-10.text-underline-none.radius-3.mvrspace-10')
close_1.click()
time.sleep(2)
cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
cart.click()
items_product = driver.find_elements_by_class_name('table-item.ecommerce-tracked-cart-item')
assert len(items_product) == 1
driver.quit()
