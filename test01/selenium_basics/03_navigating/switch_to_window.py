from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.get("https://www.reddit.com")
driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.frame(driver.window_handles[1])
driver.get("https://www.youtube.com")
time.sleep(1)
driver.switch_to.frame(driver.window_handles[0])
driver.get("https://python.org")

driver.close()
driver.quit()
