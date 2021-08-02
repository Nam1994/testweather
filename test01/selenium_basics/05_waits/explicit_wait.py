from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#driver = webdriver.Firefox()
driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.get("http://www.python.org")
time.sleep(2)
try:
    element = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    element.click()
    time.sleep(5)
finally:
    driver.quit()
