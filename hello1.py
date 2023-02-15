

from savan import webdriver


driver = webdriver.Chrome()
driver.get("https://facebook.com")
driver.maximise_window()

print(f"current url: {driver.current_url}")
print(f"page title: {driver.title}")