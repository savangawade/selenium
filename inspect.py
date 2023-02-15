from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://facebook.com")
driver.maximize_window()

print(f"current url: {driver.current_url}")
print(f"page title: {driver.title}")
emailElement = driver.find_element(By.ID, "email")
emailElement.send_keys("savan@gmail.com")
passElement = driver.find_element(By.ID, "pass")
passElement.send_keys("Pass@124")
driver.find_element(By.NAME, "login").click()
time.sleep(20)