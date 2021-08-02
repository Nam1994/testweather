from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')
driver.maximize_window()

"""dropdown = Select(driver.find_element(By.XPATH, "//select[@id='first']"))
dropdown.select_by_index(0)
dropdown.select_by_index(1)
dropdown.select_by_index(2)
dropdown.select_by_index(3)

dropdown.select_by_value('Microsoft')
dropdown.select_by_value('Google')
dropdown.select_by_value('Apple')
dropdown.select_by_value('Yahoo')

dropdown.select_by_visible_text('Bing')
dropdown.select_by_visible_text('Google')
dropdown.select_by_visible_text('Iphone')
dropdown.select_by_visible_text('Yahoo')

all_option = driver.find_elements(By.XPATH, "//select[@id='first']")
for i in all_option:
    print(i.text)"""

multi_product = Select(driver.find_element(By.XPATH, "//select[@id='second']"))
multi_product.select_by_index(0)
multi_product.select_by_index(1)
multi_product.select_by_index(2)
multi_product.select_by_index(3)

all_option = driver.find_elements(By.XPATH, "//select[@id='second']/option")
for i in all_option:
    i.click()


#multi_product.deselect_all()
#for i in range(4):
    #multi_product.select_by_index(i)



