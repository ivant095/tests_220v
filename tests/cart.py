from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value

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
time.sleep(1)

# Если количество элементов в корзине не равно 0, сделать очистку:
cart_items = driver.find_elements(By.CSS_SELECTOR, 'table-item.ecommerce-tracked-cart-item')

# Нажать все 'a.btn-del'
if len(cart_items) != 0:
    del_btns = driver.find_elements(By.CSS_SELECTOR, 'a.btn-del')
    for b in del_btns:
        b.click()
        time.sleep(2)

driver.get('https://www.220-volt.ru/catalog-501170/')
product_code = driver.find_element(By.CSS_SELECTOR, '.box-inline>#product-code')
product_code_first = product_code.text.replace(' ', '')
add_to_cart = driver.find_element(By.CSS_SELECTOR, '.mhbspace-40.phbspace-20>div:nth-child(3)>div>a')
add_to_cart.click()
time.sleep(2)
close_cart_notification = driver.find_element(By.CSS_SELECTOR,
                                              '.mhtspace-10>.box-inline.v-top.btn.btn-white.divider.pvspace-25.phspace-10.text-underline-none.radius-3.mvrspace-10')
close_cart_notification.click()
time.sleep(2)
cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
cart.click()
product_code_2 = driver.find_element(By.CSS_SELECTOR, 'div>.text-color-silver.text-size-small')
product_code_second = product_code_2.text.replace('Код товара ', '')
assert product_code_first == product_code_second
cart_items = driver.find_elements(By.CLASS_NAME, 'table-item.ecommerce-tracked-cart-item')
assert len(cart_items) == 1

cart_total_count = driver.find_element(By.CSS_SELECTOR, '.order-receipt-text>.order-packs').text
assert cart_total_count == '1'

driver.quit()
