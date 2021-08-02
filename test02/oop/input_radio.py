from pip._internal.commands import index
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
driver.maximize_window()

elm_yes = driver.find_element(By.XPATH, "(//form[@id='contact_form']//input[@name='hosting'])[2]")
print(elm_yes.get_attribute('value'))


