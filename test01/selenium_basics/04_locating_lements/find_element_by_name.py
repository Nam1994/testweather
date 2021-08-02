from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.get("http://google.com")
driver.maximize_window()
time.sleep(3)
inputElement = driver.find_element_by_name("q")
inputElement = driver.find_elements_by_name("q")

driver.close()

