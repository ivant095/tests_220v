import time
from selenium.webdriver.common.by import By


def close_cart_alert(driver):
    driver.find_element(By.CSS_SELECTOR, '.form-group>div>.btn-light-yellow-flat')\
        .click()
    time.sleep(2)


def press_add_to_cart(driver):
    driver.find_element(
        By.CSS_SELECTOR,
        '.mvspace-20.mhbspace-10>.ecommerce-tracked-product.in-cart.box-inline.mspace-0'
    )\
        .click()
    time.sleep(3)

def press_add_to_wishlist(driver):
    driver.find_element(
        By.CSS_SELECTOR,
        '.box-inline.v-top.mvrspace-20>.favorite-trigger.text-underdot.text-underline-none.v-middle.text-small'
    )\
        .click()
    time.sleep(2)

