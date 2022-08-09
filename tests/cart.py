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

# Открыть корзину
cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
cart.click()
time.sleep(2)

# Находим элементы в корзине
cart_items = driver.find_elements(By.CSS_SELECTOR, '.table-item.ecommerce-tracked-cart-item')

# Если количество элементов в корзине не равно 0, сделать очистку: Нажать все 'a.btn-del'
if len(cart_items) != 0:
    del_btns = driver.find_elements(By.CSS_SELECTOR, 'a.btn-del')
    for b in del_btns:
        b.click()
        time.sleep(7)

driver.get('https://www.220-volt.ru/catalog-501522/')
product_code = driver.find_element(By.CSS_SELECTOR, '.box-inline>#product-code')
product_code_first = product_code.text.replace(' ', '')
add_to_cart = driver.find_element(By.CSS_SELECTOR, '.mvspace-20.mhbspace-10>.ecommerce-tracked-product.in-cart.box-inline.mspace-0')
add_to_cart.click()
time.sleep(2)
close_cart_notification = driver.find_element(By.CSS_SELECTOR, '.form-group>div>.btn-light-yellow-flat')
close_cart_notification.click()
time.sleep(2)
cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
cart.click()
time.sleep(3)
product_code_2 = driver.find_element(By.CSS_SELECTOR, 'div>.text-color-silver.text-size-small')
product_code_second = product_code_2.text.replace('Код товара ', '')
assert product_code_first == product_code_second
cart_items = driver.find_elements(By.CSS_SELECTOR, '.table-item.ecommerce-tracked-cart-item')
assert len(cart_items) == 1

cart_total_count = driver.find_element(By.CSS_SELECTOR, '.order-receipt-text>.order-packs').text
assert cart_total_count == '1'

driver.quit()
