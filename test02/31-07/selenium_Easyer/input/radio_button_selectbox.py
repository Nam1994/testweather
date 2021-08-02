from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
driver.maximize_window()
# get attribute button in table 1

"""male_1 = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").click()
button_choices = driver.find_element(By.XPATH, " //button[text()='Get Checked value']").click()
time.sleep(1)
female_1 = driver.find_element(By.XPATH, "(//input[@type='radio'])[2]").click()
button_choices = driver.find_element(By.XPATH, " //button[text()='Get Checked value']").click()
time.sleep(1)"""

# click to button in table 2

male_2 = driver.find_element(By.XPATH, "(//input[@value='Male'])[2]")

male_2.click()
# Male + Age(value) = get_total
age_0_5 = driver.find_element(By.XPATH, "//input[@value='0 - 5']")
age_0_5.click()
get_values = driver.find_element(By.XPATH, "//button[text()='Get values']")
get_values.click()
time.sleep(2)

text_value = driver.find_element(By.XPATH, "//p[@class='groupradiobutton']")
print(text_value.text)
assert 'Sex : Male' in text_value.text
assert 'Age group: 0 - 5' in text_value.text
# with 5-15
# with 15-50

"""female_2 = driver.find_element(By.XPATH, "(//input[@type='radio'])[4]")
female_2.click()
age_0_5_f = driver.find_element(By.XPATH, "(//input[@type='radio'])[5]")
age_0_5_f.click()
get_values_f = driver.find_element(By.XPATH, "//button[text()='Get values']")
get_values_f.click()
time.sleep(2)"""


driver.close()
