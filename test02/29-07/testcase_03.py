from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()

element_input = driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']")
element_input.send_keys('selenium')
element_input.submit()


elenment_check = driver.find_element(By.XPATH, "//div[@class='TbwUpd NJjxre']//*[text()='https://www.selenium.dev']")
elenment_check.click()

elenment_download = driver.find_element(By.XPATH, "(//div[@class='download-button-container'])[2]//a")
elenment_download.click()

elenment_linkdownload = driver.find_element(By.XPATH, "(//td/a)[1]")
elenment_linkdownload.click()