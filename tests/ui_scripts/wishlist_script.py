import time
from selenium.webdriver.common.by import By


def open_wishlist(driver):
    driver.find_element(By.CSS_SELECTOR, 'i.header-panel-fav-icon').click()
    time.sleep(3)


def get_wishlist_positions(driver):
    return driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')


def clear_wishlist(driver):
    if len(get_wishlist_positions(driver)) > 0:
        delete_btns = driver.find_elements(By.CSS_SELECTOR, 'td>.del-favorite')
        for b in delete_btns:
            b.click()
        time.sleep(2)



