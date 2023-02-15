from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
driver.implicitly_wait(10)
element = driver.find_element(By.ID, 'checkBox1')
if element.is_selected():
    print("checkBox1 is selected : test case failed")
else:
    print("checkBox1 is not selected : test case is pass")
element = driver.find_element(By.ID, 'checkBox2')
if element.is_selected():
    print("checkBox2 is selected : test case failed")
else:
    print("checkBox2 is not selected : test case is pass")
element = driver.find_element(By.ID, 'checkBox3')
if element.is_selected():
    print("checkBox3 is selected : test case failed")
else:
    print("checkBox3 is not selected : test case is pass")
element = driver.find_element(By.ID, 'checkBox4')
if element.is_selected():
    print("checkBox4 is selected : test case failed")
else:
    print("checkBox4 is not selected : test case is pass")
element = driver.find_element(By.ID, 'checkBox5')
if element.is_selected():
    print("checkBox5 is selected : test case passed")
else:
    print("checkBox5 is not selected : test case is failed")

time.sleep(15)