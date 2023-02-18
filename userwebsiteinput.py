from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(3)
url = ["https://www.amazon.com/",
       "https://www.flipkart.com/",
       "https://www.facebook.com/",
       "https://www.instagram.com/",
       "https://www.timesofindia.com/"]
print("enter number from below list for particular website")
for i in range(len(url)):
    driver.get(url[i])
    print(f"{i} : {driver.current_url}")
    if i != len(url)-1:
        driver.execute_script("window.open('')")
        driver.switch_to.window(driver.window_handles[-1])
index = input("enter number of url :")
driver.switch_to.window(driver.window_handles[int(index)])
print(f"current url : {driver.current_url}")

