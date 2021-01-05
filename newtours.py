from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge(executable_path= r"C:\Users\v-trugan\Driver\edgedriver_win64_84\msedgedriver.exe")
driver.get("http://www.newtours.demoaut.com")
print(driver.title)
print(driver.current_url)


user_ele = driver.find_element_by_name("useName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

round_trip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(round_trip_radio.is_selected())

one_trip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("Status of one trip:", round_trip_radio.is_selected())
driver.close()