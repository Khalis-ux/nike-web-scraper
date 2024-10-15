import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.nike.com/it/launch?s=upcoming")
        self.assertIn("Prodotti in arrivo. Nike SNKRS IT", driver.title)
        time.sleep(2)

        try:
            reject_button = driver.find_element(By.XPATH, "//button[@aria-label='Rifiuta tutti']")
            reject_button.click()
            time.sleep(2)
        except StaleElementReferenceException:
            # Rilocalizza l'elemento dopo l'aggiornamento della pagina
            reject_button = driver.find_element(By.XPATH, "//button[@aria-label='Rifiuta tutti']")
            reject_button.click()

        elem_1 = driver.find_elements(By.CSS_SELECTOR, "h2.headline-5")
        elem_2 = driver.find_elements(By.CSS_SELECTOR, "h3.headline-3")
        for elem1, elem2 in zip(elem_1, elem_2):
            print(elem1.text + '\n', elem2.text + '\n')

        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
