from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.google.com/")
tab1 = driver.current_url
driver.switch_to.new_window()
driver.get("https://www.flipkart.com/")
tab2 = driver.current_url
driver.switch_to.new_window()
driver.get("https://www.facebook.com/")
tab3 = driver.current_url
driver.switch_to.new_window()
driver.get("https://www.instagram.com/")
tab4 = driver.current_url
driver.switch_to.new_window()
driver.get("https://www.timesofindia.com/")
tab5 = driver.current_url
website = {'google': tab1, 'flipkart': tab2, 'facebook': tab3, 'insta': tab4, 'toi': tab5}
print(f"choose one of the url:\n {website}")
user = input("enter (website[key]):")
result = (website[user])
driver.switch_to.new_window()
driver.get(result)
print(f"page title : {driver.current_url}")
