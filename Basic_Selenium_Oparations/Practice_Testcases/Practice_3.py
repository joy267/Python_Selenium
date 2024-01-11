# Basic_Selenium_Oparations
# ---------------
# 1) Open the browser
# 2) Enter the URL “http://practice.automationtesting.in/”
# 3) Click on Shop Menu
# 4) Now click on Home menu button
# 5) Test whether the Home page has Three Arrivals only
# 6) The Home page must contains only three Arrivals
# 7) Now click the image in the Arrivals
# 8) Test whether it is navigating to next page where the user can add that book into his basket.
# 9) Image should be clickable and should navigate to next page where user can add that book to his basket

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
time.sleep(3)
print("Number of Arrivals :",len(arrivals))

driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.close()



