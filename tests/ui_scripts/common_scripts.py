import time

from selenium import webdriver


def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def open_product(driver, product_url):
    driver.get(product_url)
    time.sleep(2)
