from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.220-volt.ru/')
driver.implicitly_wait(5)

enter = driver.find_element(By.CSS_SELECTOR, 'a>.header-panel-icon>.header-panel-user-icon')
enter.click()
time.sleep(1)
email = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>div>#user_email')
email.send_keys('ivant095@yandex.ru')
password = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10.box-relative>.mhbspace-10:nth-child(2)>input')
password.send_keys('K2nS9Qwp7')
enter_btn = driver.find_element(By.CSS_SELECTOR, '.mhbspace-10:nth-child(3)>.box-inline.col-12.v-middle>button')
enter_btn.click()
time.sleep(2)

wishlist_btn = driver.find_element(By.CSS_SELECTOR, 'i.header-panel-fav-icon')
wishlist_btn.click()
time.sleep(3)

wishlist = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')

# Нажать все 'a.btn-del'
if len(wishlist) != 0:
    del_btns = driver.find_elements(By.CSS_SELECTOR, 'td>.del-favorite')
    for b in del_btns:
        b.click()
        time.sleep(2)


driver.get('https://www.220-volt.ru/catalog-501522/')
count_1_list = driver.find_element(By.CSS_SELECTOR, '.box-inline.v-top.mvrspace-20>.favorite-trigger.text-underdot.text-underline-none.v-middle.text-small')
count_1_list.click()
time.sleep(2)
driver.get('https://www.220-volt.ru/catalog-524325/')
count_2_list = driver.find_element(By.CSS_SELECTOR, '.box-inline.v-top.mvrspace-20>.favorite-trigger.text-underdot.text-underline-none.v-middle.text-small')
count_2_list.click()
time.sleep(2)
driver.get('https://www.220-volt.ru/catalog-378204/')
count_3_list = driver.find_element(By.CSS_SELECTOR, '.box-inline.v-top.mvrspace-20>.favorite-trigger.text-underdot.text-underline-none.v-middle.text-small')
count_3_list.click()
time.sleep(2)
cart = driver.find_element(By.CSS_SELECTOR, '.header-panel-item:nth-child(2)>a>span>i')
cart.click()
time.sleep(2)
items_counts = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
assert len(items_counts) == 3
driver.quit()