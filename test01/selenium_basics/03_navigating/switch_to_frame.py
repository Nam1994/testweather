from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(3)

driver.switch_to_frame("mce_0_ifr")
driver.switch_to_default_content()

driver.close()
