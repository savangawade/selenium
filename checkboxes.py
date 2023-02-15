from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
elements = driver.find_elements(By.XPATH, '//*[@type="checkbox"]')
print(elements)
for element in elements:
    print(element.is_selected())
time.sleep(5)