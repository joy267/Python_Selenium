# Basic_Selenium_Oparations
# ---------------
# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on Shop Menu
# 4) Now click on Home menu button
# 5) Test whether the Home page has Three Sliders only
# 6) The Home page must contains only three sliders


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
sliders = driver.find_elements(By.CLASS_NAME, "n2-ss-slide")
print("Number of sliders :",len(sliders))

driver.close()
