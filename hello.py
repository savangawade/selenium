from savan import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://facebook.com")
driver.maximize_window()

print(f"current url: {driver.current_url}")
print(f"page title: {driver.title}")
time.sleep(10.0)