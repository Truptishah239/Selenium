# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object
driver = webdriver.Edge(executable_path=  r"C:\Users\v-trugan\Driver\edgedriver_win64_84\msedgedriver.exe")

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# create action chain object
action = ActionChains(driver)

# click the item
action.click(on_element=element)

# perform the operation
action.perform()