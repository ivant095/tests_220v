import time
from selenium.webdriver.common.by import By


def open_cart(driver):
    cart = driver.find_element(By.CSS_SELECTOR, '.header-panel>div:nth-child(3)>a>span>i')
    cart.click()
    time.sleep(3)


def get_cart_positions(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.table-item.ecommerce-tracked-cart-item')


def clear_cart(driver):
    if len(get_cart_positions(driver)) != 0:
        del_btns = driver.find_elements(By.CSS_SELECTOR, 'a.btn-del')
        for b in del_btns:
            b.click()
            time.sleep(7)
