from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
import time


class test(unittest.TestCase):

    def testSearch(self):
        driver = webdriver.Chrome()
        driver.get("https://openweathermap.org/")
        driver.maximize_window()

        assert 'Сurrent weather and forecast - OpenWeatherMap' in driver.title

        search_elem = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        search_elem.send_keys('Ha Noi')

        # --> Tim form --> Submit
        elm_form = driver.find_element(By.XPATH, "(//form[@role='search'])[1]")
        elm_form.submit()
        # --> verify temperature
        print('----------------------------------')
        temperature_elem = driver.find_element(By.XPATH, "//span[@class='badge badge-info']")
        print('temperature in source is: ', temperature_elem.text)
        try:
            self.assertEqual('28°С', temperature_elem.text.strip())
        except AssertionError:
            print("exp temperature not match in page source")

        # --> verify Text Ha Noi, Vn
        print('--------------------------------------')
        text_hanoi = driver.find_element(By.XPATH, "//a[@href='/city/1581130']")
        try:
            print('Exp text matched')
            self.assertEqual('Ha Noi, VN', text_hanoi.text)

        except AssertionError:
            print("Exp text not match in page source")

        # --> Verify weather logo

        logo_weather = driver.find_element(By.XPATH, '(//td/img)[1]')
        logo_weather.get_attribute('height')
        self.assertEqual('50', logo_weather.get_attribute('height'))
        self.assertEqual('50', logo_weather.get_attribute('width'))

        # --> click in Ha Noi, Vn link
        get_url = driver.find_element(By.XPATH, "//a[@href='/city/1581130']")
        self.assertIn('/city/1581130', get_url.get_attribute('href'))
        temp_1 = driver.find_element(By.XPATH, "//span[@class='badge badge-info']")
        get_url.click()
        time.sleep(10)

        # --> verify temperature
        temp_2 = driver.find_element(By.XPATH, "//div[@class='current-temp']/span")

        try:
            self.assertEqual(temp_1, temp_2)
            print("temp_1 match temp_2")
        except AssertionError:
            print("not match temp")
        # --> verify text 'Ha Noi, VN'

        text_HN = driver.find_element(By.XPATH, "//h2[@style='margin-top: 0px;']")
        try:
            self.assertEqual('Ha Noi, VnN', text_HN.text)
        except AssertionError:
            print('Ha Noi, VN not match page source')



if __name__ == "__main__":
    unittest.main()
