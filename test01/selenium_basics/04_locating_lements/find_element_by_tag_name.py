from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Admin\Desktop\Python Selenium\test01\Drivers\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

elements = driver.find_element_by_tag_name("input")
elements = driver.find_elements_by_tag_name("input")

driver.close()
driver.quit()
