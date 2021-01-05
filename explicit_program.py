from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge(executable_path= r"C:\Users\v-trugan\Driver\edgedriver_win64_84\msedgedriver.exe")
driver.get("https://www.expedia.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)