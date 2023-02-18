from selenium import webdriver

# List of URLs to open
urls = ['https://www.google.com', 'https://www.github.com', 'https://www.youtube.com', 'https://www.reddit.com', 'https://www.linkedin.com']

# Create a list to store the browser window handles
window_handles = []

# Open each URL in a new browser window and add its window handle to the list
for url in urls:
    driver = webdriver.Chrome()  # Use your preferred browser driver here
    driver.get(url)
    window_handles.append(driver.window_handles[0])

# Ask the user which window to switch to
print('Enter a window title or URL to switch to:')
user_input = input()

# Find the window handle for the matching window and switch to it
for handle in window_handles:
    driver.switch_to.window(handle)
    if user_input in driver.title or user_input in driver.current_url:
        print(f'Switched to window with title: "{driver.title}" and URL: {driver.current_url}')
        break
else:
    print(f'Could not find a window with title or URL containing "{user_input}"')








from selenium import webdriver

# Store the website URLs in a list
urls = ['https://www.google.com', 'https://www.youtube.com', 'https://github.com', 'https://www.wikipedia.org', 'https://www.linkedin.com']

# Open each URL in a new window and store the window handle and title in a list of dictionaries
windows = []
for url in urls:
    driver = webdriver.Chrome()
    driver.get(url)
    windows.append({'handle': driver.current_window_handle, 'title': driver.title})

# Prompt the user to enter a keyword in the window title to switch to
keyword = input("Enter a keyword in the title of the window to switch to: ")

# Switch to the window with the specified keyword in the title
for window in windows:
    if keyword in window['title']:
        driver.switch_to.window(window['handle'])
        break
else:
    print("Window not found")
