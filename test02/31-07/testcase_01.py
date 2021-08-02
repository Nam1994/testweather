from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.python.org")
driver.maximize_window()


wait = WebDriverWait(driver, 10)
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//a[text()='About1']")))

element = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.XPATH, "//a[text()='About']")))


element_about = driver.find_elements(By.XPATH, "//a[text()='About']")
element_1 = element_about[1]
print(element_1.text)

element_2 = driver.find_element(By.XPATH, "//*[@id='about']")
print(element_2.get_attribute('class'))
print(element_2.get_attribute('aria-haspopup'))





element_1.click()
print(len(element_about))

driver.close()
