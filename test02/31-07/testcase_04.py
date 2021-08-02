from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://zing.vn")
driver.maximize_window()
#driver.find_element_by_tag_name('body').send_keys(Keys.END)
#driver.find_element_by_tag_name('body').send_keys(Keys.HOME)

elenment = driver.find_elements(By.CLASS_NAME, 'article-thumbnail')
elenment.execute_script("{}.scrollIntoView()".format(elenment))

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)



driver.close()