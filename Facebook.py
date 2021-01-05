from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

#user_name = input("Enter username: ")
#pass_word = getpass("Password Please: ")

driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)

username = driver.find_element_by_name("email")
print(username.is_displayed())
print(username.is_enabled())
username.send_keys("Truptishah239@yahoo.com")
driver.find_element_by_id("pass").send_keys("-------")
driver.find_element_by_id("u_0_b").submit()

