# Navigational Commands
# --------------------------
# 1. back() - To get the previous web page.
# 2. forward() - To get the next web page.
# 3. refresh() - To refresh the web page.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://www.facebook.com/")
driver.get("https://www.youtube.com/")

driver.back()  # facebook

driver.forward()  # youtube

driver.refresh() # refresh page


