from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
button = driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
button.click()
time.sleep(4)
driver.switch_to.alert.accept()
element = driver.find_element(By.XPATH, "//p[@id='result']")
if element.text == 'You clicked: Ok':
    print("test case is pass")
else:
    print("test case is fail")
time.sleep(4)

