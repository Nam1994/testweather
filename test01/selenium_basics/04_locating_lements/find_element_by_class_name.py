from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()


driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)
elements = driver.find_element_by_class_name("example")


driver.close()
driver.quit()
