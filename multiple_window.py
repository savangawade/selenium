from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
var = driver.window_handles
element = driver.window_handles[-1]
