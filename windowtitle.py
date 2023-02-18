from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
window_title = driver.title
print(window_title)