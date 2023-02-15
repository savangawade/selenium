from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://mpsconline.gov.in/candidate/login")
driver.maximize_window()

print(f"current url: {driver.current_url}")
print(f"page title: {driver.title}")
emailElement = driver.find_element(By.ID, "userName")
emailElement.send_keys("savan@gmail.com")
passElement = driver.find_element(By.ID, "password")
passElement.send_keys("Sahgjjw@124")
captchaElement = driver.find_element(By.ID, "exampleFormControlInput2")
captchaElement.send_keys("198392")
login = driver.find_element(By.NAME, "login")
login.click()
time.sleep(30)