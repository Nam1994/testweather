from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http:www.zing.vn')
driver.maximize_window()

elenmet_image = driver.find_element(By.XPATH, "(//p[@class='article-thumbnail']//img)[1]")
elenmet_image.click()

elenmet_logo = driver.find_element(By.XPATH, "//h1[@class='logo']")
elenmet_logo.click()

element_button = driver.find_element(By.XPATH, "//ul[@class='current-city']")
element_button.click()

element_angian = driver.find_element(By.XPATH, "//div[@class='city-list']//div[@class='others-city']//li[@city='angiang']")
element_angian.click()