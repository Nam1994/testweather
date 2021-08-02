import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def tearDown(self):
        self.driver.close()


    def test_Search_elenment(self):
        driver = self.driver
        driver.get("http://www.python.org")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        

        time.sleep(3)




if __name__ == "__main__":
    unittest.main()
