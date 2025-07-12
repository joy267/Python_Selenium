from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Projects\\automation\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.implicitly_wait(10)

# Get URL
driver.get("https://testautomationpractice.blogspot.com/")

#

# Close Browser
driver.quit()
