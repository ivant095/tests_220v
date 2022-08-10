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
press_add_to_cart(driver)
close_cart_alert(driver)

driver.get('https://www.220-volt.ru/catalog-524325/')
press_add_to_cart(driver)
close_cart_alert(driver)

driver.get('https://www.220-volt.ru/catalog-378204/')
press_add_to_cart(driver)
close_cart_alert(driver)
open_cart(driver)

assert len(get_cart_positions(driver)) == 3
driver.quit()
