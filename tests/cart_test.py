import unittest

from selenium.webdriver.common.by import By

from tests.ui_scripts.common_scripts import create_driver
from tests.ui_scripts.login_scripts import login

from tests.ui_scripts.cart_scripts import open_cart
from tests.ui_scripts.cart_scripts import clear_cart
from tests.ui_scripts.cart_scripts import get_cart_positions

from tests.ui_scripts.product_scripts import press_add_to_cart
from tests.ui_scripts.product_scripts import close_cart_alert
from tests.ui_scripts.common_scripts import open_product


class TestCart(unittest.TestCase):

    username = 'ivant095@yandex.ru'
    password = 'K2nS9Qwp7'

    def test_add_item_to_cart(self):
        driver = create_driver()
        login(driver, self.username, self.password)
        open_cart(driver)
        clear_cart(driver)

        open_product(driver, "https://www.220-volt.ru/catalog-501522/")
        product_code_in_catalog = driver.find_element(By.CSS_SELECTOR, '.box-inline>#product-code')\
            .text\
            .replace(' ', '')
        press_add_to_cart(driver)
        close_cart_alert(driver)

        open_cart(driver)
        product_code_in_cart = driver.find_element(By.CSS_SELECTOR, 'div>.text-color-silver.text-size-small') \
            .text \
            .replace('Код товара ', '')

        self.assertEqual(product_code_in_cart, product_code_in_catalog)
        self.assertGreaterEqual(1, len(get_cart_positions(driver)))
        cart_products_total_count = driver.find_element(By.CSS_SELECTOR, '.order-receipt-text>.order-packs').text
        self.assertEqual('1', cart_products_total_count)

        driver.quit()

    def test_add_items_to_cart(self):
        driver = create_driver()
        login(driver, self.username, self.password)
        open_cart(driver)
        clear_cart(driver)

        driver.get('https://www.220-volt.ru/catalog-501522/')
        press_add_to_cart(driver)
        close_cart_alert(driver)

        driver.get('https://www.220-volt.ru/catalog-524325/')
        press_add_to_cart(driver)
        close_cart_alert(driver)

        driver.get('https://www.220-volt.ru/catalog-378204/')
        press_add_to_cart(driver)
        close_cart_alert(driver)
        open_cart(driver)

        self.assertGreaterEqual(3, len(get_cart_positions(driver)))
        driver.quit()

