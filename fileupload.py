import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

input = driver.find_element(By.XPATH, "//input[@id = 'file-upload']")
file = r"C:\Users\ADMIN\Desktop\Capture9.PNG"
input.send_keys(file)
driver.find_element(By.XPATH, "//input[@id = 'file-submit']").click()
driver.implicitly_wait(10)
uploaded_file_name = driver.find_element(By.XPATH, '//*[@id="uploaded-files"]').text
print(uploaded_file_name)
expected_file_name = os.path.basename(r"C:\Users\ADMIN\Desktop\Capture9.PNG")
print(expected_file_name)
if uploaded_file_name == expected_file_name:
    print(True)
else:
    print(False)
