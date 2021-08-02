from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://the-internet.herokuapp.com/dropdown")

drop_down = Select(driver.find_element(By.ID, "dropdown"))
drop_down.select_by_index(1)
drop_down.select_by_index(2)
drop_down.select_by_value('1')
drop_down.select_by_value('2')
drop_down.select_by_visible_text('Option 1')
drop_down.select_by_visible_text('Option 2')

all_options = driver.find_elements_by_tag_name('option')
for element in all_options:
    print(element.get_attribute("value"))

driver.close()




