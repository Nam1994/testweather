from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest


class Datepicker(unittest.TestCase):

    def testInput(self):
        driver = webdriver.Chrome()
        driver.get('https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html')
        driver.maximize_window()
        time.sleep(3)
        # select 'today'
        elem_click = driver.find_element(By.XPATH, "//span[@class='input-group-addon'][1]")
        elem_click.click()
        time.sleep(2)
        el2 = driver.find_element(By.XPATH, "(//table[1]/tfoot/tr/th[@class='today'])[1]")
        el2.click()
        time.sleep(2)
        elem_click = driver.find_element(By.XPATH, "//span[@class='input-group-addon'][1]")
        elem_click.click()
        el3 = driver.find_element(By.XPATH, "(//table[1]/tfoot/tr/th[@class='clear'])[1]")
        el3.click()
        # input Range Date picker
        start_state = driver.find_element(By.XPATH, "(//div[@id='datepicker']/input)[1]")
        start_state.send_keys('10/11/2020')
        time.sleep(4)

        end_state = driver.find_element(By.XPATH, "//div[@id='datepicker']/input[@type ='text' and @placeholder='End date']")
        end_state.click()

        time.sleep(5)




if __name__ == "__main__":
    unittest.main()
