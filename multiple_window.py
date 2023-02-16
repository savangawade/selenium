from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
print(f"Current Window Handle before click : {driver.current_window_handle}")     ## will give us where driver is looking for elements
print(f"Window Handles before click : {driver.window_handles}")

driver.find_element(By.XPATH, "//a[text()='Click Here']").click()   ## after click new tab will open
print(f"Current Window Handle after click : {driver.current_window_handle}")     ## will give us where driver is looking for elements
print(f"Window Handles after click : {driver.window_handles}")
print(f"Current URL before switch: {driver.current_url}")   #Current URL before switch: https://the-internet.herokuapp.com/windows

time.sleep(3)       # pause a script for 3 sec. block execution

## driver.window_handles[-1]   # lastly open window
driver.switch_to.window(driver.window_handles[-1])           #window() - Switches focus to the specified window
print(f"Current Window Handle after switch : {driver.current_window_handle}")     ## will give us where driver is looking for elements
print(f"Window Handles after switch : {driver.window_handles}")
print(f"Current URL after switch: {driver.current_url}")       #Current URL after switch: https://the-internet.herokuapp.com/windows/new

element = driver.find_element(By.XPATH, '/html/body/div/h3')
print(element.text)
#print(element.get_attribute('innerHTML'))

if element.text == 'New Window':
    print("Test case passed")
else:
    print("Test case failed")
###------------------------------------------------------------------------

## Open new blank window or tab and switch driver to it

# open new tab/window and switch to it
driver.switch_to.new_window()  ##default value :'tab'     ## new empty tab will be opened and driver focus will change to it
##print(driver.current_window_handle)
driver.get("https://www.amazon.com/")

driver.switch_to.new_window('tab')  # open new tab and switch to it
driver.get("https://www.flipkart.com/")

driver.switch_to.new_window('window')  # open new window and switch to it

driver.get("https://www.facebook.com/")
print(driver.current_window_handle)
print(driver.window_handles)
print(f"Current URL after switch: {driver.current_url}")