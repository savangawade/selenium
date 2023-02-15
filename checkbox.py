from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
elements = driver.find_elements(By.CLASS_NAME, 'checkBoxClassB')
print(elements)
for element in elements:
    print(element.is_selected())
if elements.__init_subclass__():
    print("checkbox is selected : test case failed")
else:
    print("checkbox not selected : Test case is pass")
time.sleep(5)
