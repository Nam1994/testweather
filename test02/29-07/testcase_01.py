from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('http://www.python.org')

#element_search = driver.find_element_by_id("id-search-field")
#element_search = driver.find_element_by_name('q')
#element_search = driver.find_element_by_class_name("search-field")
#element_search = driver.find_element_by_xpath('//*[@id="id-search-field"]')
#element_search = driver.find_element_by_css_selector('#id-search-field')
#element_search = driver.find_element(By.ID, "id-search-field")
#element_search = driver.find_element(By.NAME, 'q')
#element_search = driver.find_element(By.CLASS_NAME, "search-field")
#element_search = driver.find_element(By.CSS_SELECTOR, "#id-search-field")
element_search = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
#element_search = driver.find_element(By.XPATH, "//input[@type='search']")


element_search.send_keys("python")


#element_go = driver.find_element_by_id('submit')
#element_go = driver.find_element(By.XPATH, "//button[@name='submit']")
element_go = driver.find_element(By.XPATH, "//button[@class='search-button']")
element_go.click()
element_about = driver.find_element(By.XPATH, "(//*[text()='About'])[1]") #lay Index
element_about.click()
element_documentation = driver.find_element(By.XPATH, "(//*[text()='Documentation'])[2]")
element_documentation.click()

driver.close()
