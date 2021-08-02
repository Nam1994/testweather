from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.implicitly_wait(100)

driver.get("http://google.com")
driver.maximize_window()

print("Implicit Wait Example")
inputElement = driver.elem = driver.find_element_by_name("q")
inputElement.send_keys('Techbeamers')
inputElement.click()
time.sleep(5)   

driver.close()
