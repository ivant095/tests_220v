from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.220-volt.ru/')
driver.implicitly_wait(10)
search = driver.find_element(By.CSS_SELECTOR, '.panel-search-input>input')
search.send_keys('Дрель')
search_btn = driver.find_element(By.CSS_SELECTOR, '.panel-search-input>i').click()
text_to_be_present_in_element_value('.column.column-page.right>.new-items-list.new-items-list-count-three.mhspace-10.new-items-list-box>#product-list', 'Дрель')
driver.quit()