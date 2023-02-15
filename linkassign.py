from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
link = driver.find_element(By.ID, 'myLink2')
print(link.text)
print(f"{link.get_attribute('innerHTML')} : {link.get_attribute('href')}")