from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")
driver.get("https://teams.microsoft.com/_")


#driver.find_element_by_xpath('//*[@id="signup"]').click()
#driver.find_element_by_name('MemberName').send_keys('Gandhifamily@hotmail.com')
#driver.find_element_by_id('iSignupAction').click()
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
time.sleep(2)
'''
#elem = driver.find_element_by_class_id('//*[@id="searchInputField"]').click()
#elem.send_keys("Trupti")
'''

'''
ele = driver.find_element_by_name("Create account")
print(ele.is_displayed())
print(ele.is_enabled())
#driver.close()
#driver.back()
#driver.forward()
'''
#driver.quit()



