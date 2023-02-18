from selenium import webdriver
driver = webdriver.Chrome()
url = ["https://www.amazon.com/",
       "https://www.flipkart.com/",
       "https://www.facebook.com/",
       "https://www.instagram.com/",
       "https://www.timesofindia.com/"]
for i in range(5):
    driver.execute_script("window.open('{}','window{}')".format(url[i], i+1))
window_title = {driver.title: handle for handle in driver.window_handles}
print(window_title)
window_handles = {handle: title for title, handle in window_title.items()}
print(window_handles)
chosen_title = input('enter the title:')
chosen_handle = window_title[chosen_title]
driver.switch_to.new_window(chosen_handle)
chosen_url = driver.current_url
for handle in window_handles:
    if handle != chosen_handle:
        driver.switch_to.window(handle)
        print((handle, driver.title))
        if driver.current_url == chosen_url:
            break
driver.switch_to.window(chosen_handle)
print(f"current url : {driver.current_url}")