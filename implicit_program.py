from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge(executable_path= r"C:\Users\v-trugan\Driver\edgedriver_win64_84\msedgedriver.exe")
driver.get("http://www.newtours.demoaut.com")
print(driver.title)
print(driver.current_url)

driver.implicitly_wait()wait(10)
assert "welcome: Mercury Tours" in driver.title
driver.find_element_by_name("useName").send_keys("mercury")

driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()