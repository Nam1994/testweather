from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
time.sleep(5)

element_a = driver.find_element_by_id("column-a")
element_b = driver.find_element_by_id("column-b")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element_a, element_b).perform()
time.sleep(5)
action_chains.drag_and_drop(element_b, element_a).perform()

driver.get("https://www.testandquiz.com/selenium/testing.html")
time.sleep(3)

sourceImage = driver.find_element_by_id("sourceImage")
targetDiv = driver.find_element_by_id("targetDiv")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(sourceImage, targetDiv).perform()
time.sleep(3)

driver.close()
