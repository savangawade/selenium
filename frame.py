from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()
driver.switch_to.frame("myFrame3")
element = driver.find_element(By.XPATH, '//*[@id="checkBox6"]')
element.click()
time.sleep(5)

