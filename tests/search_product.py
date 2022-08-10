import unittest
import time
from selenium.webdriver.common.by import By

from tests.ui_scripts.common_scripts import create_driver


class TestSearchProduct(unittest.TestCase):

    def test_search_product(self):
        driver = create_driver()
        driver.get('https://www.220-volt.ru/')

        search = driver.find_element(By.CSS_SELECTOR, '.panel-search-input>input')
        search.send_keys('Дрель\n')
        time.sleep(5)

        items_names = driver.find_elements(By.CSS_SELECTOR, '.new-item-list-name>a')
        if self.assertGreaterEqual(len(items_names), 0):
            for name in items_names:
                self.assertIn(name.text.lower(), "дрель")

        driver.quit()
