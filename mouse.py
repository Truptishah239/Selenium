from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest

class pythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("https://teams.microsoft.com/")
        driver.find_element_by_id('i0116').send_keys('r-------@m365x018015.onmicrosoft.com')
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("S-------------!")
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        driver.find_element_by_class_name("use-app-lnk").click()
        driver.maximize_window()
        driver.implicitly_wait(10)
        # assert "Microsoft Teams" in driver.title
        driver.find_element_by_xpath('//*[@id="toast-container"]/div/div/div[2]/div/button[2]/div').click()
        elem = driver.find_element_by_class_name("search-box")
        elem.click()
        elem2 = driver.find_element_by_xpath('//*[@id="discover-search-input"]')
        elem2.send_keys('test')
        elem2.send_keys(Keys.RETURN)
        time.sleep(15)
        #driver.find_element_by_class_name("error-button-text")
        driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div[2]/button/span').click()
        driver.find_element_by_xpath('//*[@id="WizardBtnfromExisting"]/div[2]/div[2]')
        #driver.find_element_by_css_selector('//*[@id="backButton"]').click()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))).click()
        driver.find_element_by_xpath('//*[@id="ngdialog3"]/div[2]/div/div/div/div/div/div/creation-options-wizard-step/div/div[1]/div[2]/button').click()
        time.sleep(30)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
