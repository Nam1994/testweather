from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
driver.maximize_window()

# 1. Single Select
"""elem_select = driver.find_elements_by_tag_name("option")
for i in elem_select[0:7]:
    print(i.click())
"""
# 2. Multiply:

options = Select(driver.find_element(By.XPATH, "//select[@name='States']")).options
first_button = driver.find_element(By.XPATH, "//button[@id='printMe']")
get_total_value = driver.find_element(By.XPATH, "//button[@id='printAll']")

for elem in options[0:3]:
    elem.click()
    print(elem.get_attribute("value"))
    first_button.click()
    get_total_value.click()



