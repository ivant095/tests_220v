from selenium.webdriver.common.by import By

from tests.ui_scripts.common_scripts import create_driver
from tests.ui_scripts.login_scripts import login

from tests.ui_scripts.cart_scripts import open_cart
from tests.ui_scripts.cart_scripts import clear_cart
from tests.ui_scripts.cart_scripts import get_cart_positions

from tests.ui_scripts.product_scripts import press_add_to_cart
from tests.ui_scripts.product_scripts import close_cart_alert


driver = create_driver()
login(driver, 'ivant095@yandex.ru', 'K2nS9Qwp7')
open_cart(driver)
clear_cart(driver)

driver.get('https://www.220-volt.ru/catalog-501522/')
product_code_in_catalog = driver.find_element(By.CSS_SELECTOR, '.box-inline>#product-code')\
    .text\
    .replace(' ', '')
press_add_to_cart(driver)
close_cart_alert(driver)

open_cart(driver)
product_code_in_cart = driver.find_element(By.CSS_SELECTOR, 'div>.text-color-silver.text-size-small') \
    .text \
    .replace('Код товара ', '')
assert product_code_in_catalog == product_code_in_cart

assert len(get_cart_positions(driver)) == 1

cart_products_total_count = driver.find_element(By.CSS_SELECTOR, '.order-receipt-text>.order-packs').text
assert cart_products_total_count == '1'

driver.quit()
