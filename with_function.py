from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class pythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\v-trugan\Driver\chromedriver_win32 (1)\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python",driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        time.sleep(20)
        assert "No Result Found" not in driver.page_source

    def tearDown(self):
        self.driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

