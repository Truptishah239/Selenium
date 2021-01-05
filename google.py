from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver= webdriver.Edge(executable_path=  r"C:\Users\v-trugan\Driver\edgedriver_win64_84\msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com/")

print(driver.title)

search = driver.find_element_by_name('q')
search.click()
search.send_keys("Selenium webdriver interview questions")
search.submit()

lists = driver.find_elements_by_class_name("r")

print("Found " + str(len(lists)) + " searches")

i = 0
for item in lists:
    print(item.get_attribute("innerHTML"))
    i = i+1
    if(i>10):
        break

time.sleep(10)
driver.quit()



