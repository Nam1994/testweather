from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()

click_button = driver.find_element(By.XPATH, "//div[@id='at-cv-lightbox-button-holder']/a[text()='No, thanks!']")
click_button.click()
# test simple input Field
input_elem = driver.find_element_by_class_name("form-control")
input_elem.send_keys('test input second time')
show_elem = driver.find_element(By.XPATH, "//button[text()='Show Message']")
show_elem.click()
time.sleep(2)

#two input field

enter_a = driver.find_element(By.ID, "sum1")
enter_b = driver.find_element(By.ID, "sum2")
get_total = driver.find_element(By.XPATH, "//button[text()='Get Total']")
enter_a.send_keys('2')
enter_b.send_keys('3')
get_total.click()
driver.find_element_by_tag_name('body').send_keys(Keys.END)


time.sleep(2)




driver.close()