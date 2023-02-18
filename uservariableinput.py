import time

from selenium import webdriver


# Store the website URLs in variables
url1 = 'https://www.google.com'
url2 = 'https://www.youtube.com'
url3 = 'https://github.com'
url4 = 'https://www.wikipedia.org'
url5 = 'https://www.linkedin.com'

# Open each URL in a new window and store the window handle in a dictionary
windows = {}
for url_name in ['url1', 'url2', 'url3', 'url4', 'url5']:
    driver = webdriver.Chrome()
    url = eval(url_name)
    driver.get(url)
    windows[url_name] = driver.window_handles[0]

# Prompt the user to enter the variable name of the window to switch to
url_name = input("Enter the variable name of the URL to switch to (url1, url2, url3, url4, url5): ")

# Switch to the window with the specified variable name
if url_name in windows:
    driver.switch_to.window(windows[url_name])
else:
    print("Invalid variable name")
time.sleep(2)
