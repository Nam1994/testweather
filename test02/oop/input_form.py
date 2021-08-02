from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
from oop.contact import Contact


class TestInput(unittest.TestCase):

    def input_search(self, driver, contact):
        driver.find_element(By.NAME, "first_name").send_keys(contact.first_name)
        driver.find_element(By.NAME, "last_name").send_keys(contact.last_name)
        driver.find_element(By.NAME, "email").send_keys(contact.email)
        driver.find_element(By.NAME, "phone").send_keys(contact.phone)
        driver.find_element(By.NAME, "address").send_keys(contact.address)
        driver.find_element(By.NAME, "city").send_keys(contact.city)
        driver.find_element(By.XPATH, "//select[@name='state']/option[text()='" + contact.state + "']").click()
        driver.find_element(By.NAME, "zip").send_keys(contact.zipcode)
        driver.find_element(By.NAME, 'website').send_keys(contact.website_domain)
        driver.find_element(By.XPATH, "(//form[@id='contact_form']//input[@name='hosting'])[" + contact.hosting + "]").click()
        driver.find_element(By.NAME, 'comment').send_keys(contact.description)
        send = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Send')]")
        send.click()

    def test_input(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
        driver.maximize_window()

        contact = Contact('nam', "nguyen", 'namb1209103@gmail.com', '0975-683-243', 'Lam Van Ben street, HCM city',
                          'Ho Chi Minh', 'Arkansas', '71601', 'google.com', '1', 'This is a introduce myself')
        self.input_search(driver, contact)

        """driver.find_element(By.NAME, "first_name").send_keys('nam')
        driver.find_element(By.NAME, "last_name").send_keys("nguyen")
        driver.find_element(By.NAME, "email").send_keys("namb1209103@gmail.com")
        driver.find_element(By.NAME, "phone").send_keys(" 0975-683-243")
        driver.find_element(By.NAME, "address").send_keys("Lam Van Ben street, HCM city")
        driver.find_element(By.NAME, "city").send_keys("Ho Chi Minh")
        driver.find_element(By.XPATH, "//select[@name='state']/option[text()='Arkansas']").click()
        driver.find_element(By.NAME, "zip").send_keys('71601')
        driver.find_element(By.NAME, 'website').send_keys('google.com')
        driver.find_element(By.XPATH, "//div[@class='radio'][1]").click()
        driver.find_element(By.XPATH, "//div[@class='radio'][2]")
        driver.find_element(By.NAME, 'comment').send_keys('This is a introduce myself')
        send = driver.find_element(By.CLASS_NAME, "col-md-4")
        send.submit()"""
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
