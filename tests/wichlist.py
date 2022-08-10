from tests.ui_scripts.common_scripts import create_driver

from tests.ui_scripts.login_scripts import login

from tests.ui_scripts.wishlist_script import open_wishlist
from tests.ui_scripts.wishlist_script import clear_wishlist
from tests.ui_scripts.wishlist_script import get_wishlist_positions

from tests.ui_scripts.common_scripts import open_product

from tests.ui_scripts.product_scripts import press_add_to_wishlist


driver = create_driver()
login(driver, 'ivant095@yandex.ru', 'K2nS9Qwp7')
open_wishlist(driver)
clear_wishlist(driver)

open_product(driver, 'https://www.220-volt.ru/catalog-501522/')
press_add_to_wishlist(driver)

open_product(driver, 'https://www.220-volt.ru/catalog-524325/')
press_add_to_wishlist(driver)

open_product(driver, 'https://www.220-volt.ru/catalog-378204/')
press_add_to_wishlist(driver)

assert len(get_wishlist_positions(driver)) == 3
driver.quit()
