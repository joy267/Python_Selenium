# Tase Case
# --------------------
# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on My Account Menu
# 4) Enter registered Email Address in Email-Address textbox@gmail.com
# 5) Enter your own password in password @#ejjijdhuh!kd
# 6) Click on Register button
# 7) User will be registered successfully and will be navigated to the Home page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practice.automationtesting.in/")
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
time.sleep(4)

driver.find_element(By.NAME, "email").send_keys("textbox@gmail.com")
driver.find_element(By.ID, "reg_password").send_keys("@#ejjijdhuh!kd")
driver.find_element(By.NAME, "register").click()