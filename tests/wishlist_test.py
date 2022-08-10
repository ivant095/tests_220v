import unittest
from tests.ui_scripts.common_scripts import create_driver

from tests.ui_scripts.login_scripts import login

from tests.ui_scripts.wishlist_script import open_wishlist
from tests.ui_scripts.wishlist_script import clear_wishlist
from tests.ui_scripts.wishlist_script import get_wishlist_positions

from tests.ui_scripts.common_scripts import open_product

from tests.ui_scripts.product_scripts import press_add_to_wishlist


class TestWishlist(unittest.TestCase):

    username = 'ivant095@yandex.ru'
    password = 'K2nS9Qwp7'

    def test_wishlist(self):
        driver = create_driver()
        login(driver, self.username, self.password)
        open_wishlist(driver)
        clear_wishlist(driver)

        open_product(driver, 'https://www.220-volt.ru/catalog-501522/')
        press_add_to_wishlist(driver)

        open_product(driver, 'https://www.220-volt.ru/catalog-524325/')
        press_add_to_wishlist(driver)

        open_product(driver, 'https://www.220-volt.ru/catalog-378204/')
        press_add_to_wishlist(driver)

        self.assertEqual(3, len(get_wishlist_positions(driver)))
        driver.quit()
