from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html")
driver.maximize_window()

"""el_title = driver.find_element(By.XPATH, "//h2[text()='Single Select - Search and Select country']")
assert 'Single Select - Search and Select country' in el_title.text

# Drop Down with Search box
country = Select(driver.find_element(By.ID, 'country'))
country.select_by_index(2)

 #Multi select
list_atr = Select(driver.find_element(By.XPATH, "(//div[@class='panel panel-primary']//select)[2]")).options
for i in list_atr[5:12]:
    i.click()"""

# disiable

element_disable = Select(driver.find_element(By.XPATH, "//select[@class='js-example-disabled-results select2-hidden-accessible']"))
element_disable.select_by_visible_text('Northern Mariana Islands')


select_file = Select(driver.find_element(By.XPATH, "//select[@id='files']"))
select_file.select_by_visible_text('PHP')
select_file.select_by_visible_text('Java')

scrp_lg = driver.find_elements(By.XPATH, "//select[@id='files']/optgroup[@label='Scripting languages']/option")
for elem in scrp_lg:
    print(elem.text)
    if elem.text == 'Python':
        elem.click()



