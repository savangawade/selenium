import time

from selenium import webdriver


# Store the website URLs in variables
url1 = 'https://www.google.com'
url2 = 'https://www.youtube.com'
url3 = 'https://github.com'
url4 = 'https://www.wikipedia.org'
url5 = 'https://www.linkedin.com'
driver = webdriver.Chrome()

driver.get(url1)
driver.switch_to.new_window('tab')
driver.get(url2)
driver.switch_to.new_window('tab')
driver.get(url3)
driver.switch_to.new_window('tab')
driver.get(url4)
driver.switch_to.new_window('tab')
driver.get(url5)
driver.switch_to.window(driver.window_handles[-1])
url_name = input("Enter the variable name of the URL to switch to (url1, url2, url3, url4, url5): ")

# Switch to the window with the specified variable name
for url in url_name:
    driver.switch_to.window(url)
else:
    print("Invalid variable name")
time.sleep(2)
print(f"current url : {driver.current_url}")

