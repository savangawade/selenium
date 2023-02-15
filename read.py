import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()

element = driver.find_element(By.XPATH, '//*[@id="myTextInput2"]')

result = element.get_attribute('value')
print(f"Value : {result}")

print(f"Name : {element.get_attribute('name')}")
print(f"Type : {element.get_attribute('type')}")
print(f"ID : {element.get_attribute('id')}")

element.clear()


time.sleep(10)