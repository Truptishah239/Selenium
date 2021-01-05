from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")
driver.get("https://login.live.com/")
print(driver.title)
print(driver.current_url)

time.sleep(2)
driver.find_element_by_id("i0116").send_keys('v------@microsoft.com')

driver.find_element_by_id("idSIButton9").click()
time.sleep(2)

