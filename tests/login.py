from selenium.webdriver.common.by import By

from tests.ui_scripts.common_scripts import create_driver
from tests.ui_scripts.login_scripts import login

driver = create_driver()
login(driver, 'ivant095@yandex.ru', 'K2nS9Qwp7')

user_name = driver.find_element(By.CSS_SELECTOR, '.header-panel-item.header-user-wrapper>a>.header-panel-text.text-center')
user_name_text = user_name.text
assert user_name_text == 'Иван Антонов'
driver.quit()
