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

cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
cart.click()
time.sleep(3)

cart_items = driver.find_elements(By.CSS_SELECTOR, '.table-item.ecommerce-tracked-cart-item')

# Нажать все 'a.btn-del'
if len(cart_items) != 0:
    del_btns = driver.find_elements(By.CSS_SELECTOR, 'a.btn-del')
    for b in del_btns:
        b.click()
        time.sleep(7)

driver.get('https://www.220-volt.ru/catalog-501522/')
count_1_cart = driver.find_element(By.CSS_SELECTOR, '.mvspace-20.mhbspace-10>.ecommerce-tracked-product.in-cart.box-inline.mspace-0')
count_1_cart.click()
time.sleep(2)
close_1 = driver.find_element(By.CSS_SELECTOR, '.form-group>div>.btn-light-yellow-flat')
close_1.click()
time.sleep(2)
driver.get('https://www.220-volt.ru/catalog-524325/')
count_2_cart = driver.find_element(By.CSS_SELECTOR, '.mvspace-20.mhbspace-10>a>.text-in-cart-btn')
count_2_cart.click()
time.sleep(2)
close_2 = driver.find_element(By.CSS_SELECTOR, '.form-group>div>.btn-light-yellow-flat')
close_2.click()
time.sleep(2)
driver.get('https://www.220-volt.ru/catalog-378204/')
count_3_cart = driver.find_element(By.CSS_SELECTOR, '.mhbspace-40.phbspace-20>div:nth-child(3)>div>a')
count_3_cart.click()
time.sleep(2)
close_3 = driver.find_element(By.CSS_SELECTOR, '.form-group>div>.btn-light-yellow-flat')
close_3.click()
time.sleep(2)
cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
cart.click()
time.sleep(3)

items_product = driver.find_elements(By.CSS_SELECTOR, '.table-item.ecommerce-tracked-cart-item')
assert len(items_product) == 3
driver.quit()
