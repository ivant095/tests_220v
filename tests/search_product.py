import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.220-volt.ru/')
driver.implicitly_wait(5)
time.sleep(2)
search = driver.find_element(By.CSS_SELECTOR, '.panel-search-input>input')
search.send_keys('Дрель\n')
time.sleep(5)
items_name = driver.find_elements(By.CSS_SELECTOR, '.new-item-list-name>a')

assert len(items_name) > 0

for d in items_name:
    a = d.text
    assert a.lower().__contains__("дрель")

driver.quit()
