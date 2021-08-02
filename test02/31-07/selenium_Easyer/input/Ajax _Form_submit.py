from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.seleniumeasy.com/test/ajax-form-submit-demo.html")
driver.maximize_window()

name_title = driver.find_element(By.ID, 'title').send_keys('Hoai Nam')
comment_de = driver.find_element(By.ID, 'description').send_keys(' That is my name')
submit_button = driver.find_element(By.ID, 'btn-submit').click()
driver.close()