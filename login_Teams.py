from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class pythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("https://teams.microsoft.com/")
        driver.find_element_by_id('i0116').send_keys('r------@m365x018015.onmicrosoft.com')
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("S------------")
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        time.sleep(2)
        driver.find_element_by_id('idSIButton9').click()
        driver.find_element_by_class_name("use-app-lnk").click()
        driver.maximize_window()
        driver.implicitly_wait(10)
        # assert "Microsoft Teams" in driver.title
        driver.find_element_by_xpath('//*[@id="toast-container"]/div/div/div[2]/div/button[2]/div').click()
        print(f"Title of the page: ", driver.title)
        print(f"website of the page: ", driver.current_url)
        #time.sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
