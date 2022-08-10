import unittest

from selenium.webdriver.common.by import By
from tests.ui_scripts.common_scripts import create_driver
from tests.ui_scripts.login_scripts import login


class TestLogin(unittest.TestCase):

    username = 'ivant095@yandex.ru'
    password = 'K2nS9Qwp7'

    def test_login_successful(self):
        driver = create_driver()
        login(driver, self.username, self.password)
        username_text = driver.find_element(
            By.CSS_SELECTOR,
            '.header-panel-item.header-user-wrapper>a>.header-panel-text.text-center'
        ) \
            .text
        self.assertEqual('Иван Антонов', username_text)
        driver.quit()
