from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")
driver.get("https://teams.microsoft.com/_")
driver.find_element_by_id('i0116').send_keys('rg07-r1@m365x018015.onmicrosoft.com')
time.sleep(2)
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_id("i0118").send_keys("Summer@Winter2020!")
time.sleep(2)
driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
driver.find_element_by_id('idSIButton9').click()
driver.find_element_by_class_name("use-app-lnk").click()
driver.maximize_window()
driver.implicitly_wait(10)
assert "Microsoft Teams" in driver.title
driver.find_element_by_xpath('//*[@id="toast-container"]/div/div/div[2]/div/button[2]/div').click()
print(f"Title of the page: ", driver.title)
print(f"website of the page: ", driver.current_url)
#driver.find_element_by_class_name("app-left-wrapper pull-left")

#driver.find_element_by_xpath('//*[@id="teams-app-bar"]/ul/li[5]')
'''
driver.find_element_by_id("calling-open-dialpad-btn").click()
driver.find_element_by_class_name("element-text").click()
driver.find_element_by_xpath('//*[@id="middle-call-list-stripe"]/div[2]/div/exchange-contacts/div/div/div/button').click()
driver.find_element_by_class_name("ts-search-input ng-valid ng-touched ng-dirty ng-valid-parse ng-empty").click()
'''

#driver.switch_to.alert.dismiss()
