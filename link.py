from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME, 'a')
print("Number of links present:", len(links))
for link in links:
    print(len(links))
    print(f"{link.get_attribute('innerHTML')} : {link.get_attribute('href')}")
time.sleep(5)