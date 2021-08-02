import unittest

from selenium import Basecase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.get("https://openweathermap.org")
        titleOfWebPage = driver.title
        # verify title is bing
        self.assertIn('Сurrent weather and forecast - OpenWeatherMap', titleOfWebPage)
        search = self.
        search.send_keys('Ha Noi')


if __name__ == "__main__":
    unittest.main()
