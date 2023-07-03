# Test_Cases
# ---------------
# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on Shop Menu
# 4) Now click on Home menu button
# 5) Test whether the Home page has Three Arrivals only
# 6) The Home page must contains only three Arrivals

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Shop").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT,"Home").click()

arrivals = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
print(len(arrivals))

driver.close()