

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com")
driver.maximize_window()
print(f"current url: {driver.current_url}")
print(f"page title: {driver.title}")

usernameElement = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usernameElement.send_keys("savan@gmail")
passElement = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
passElement.send_keys("Saw@1566")
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
login_button.click()
time.sleep(15)