# Conditional Commands
# --------------------------
# 1. is_displayed() - To indentify the web element has present or not in the webpage.
# 2. is_enabled() - To indentify the web element has enabled or not in the webpage.
# 3. is_selected() - To indentify the web element has selected or not in the webpage.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

# is_displayed() ----------
print("Search Box is diplayed :", search_box.is_displayed())

# is_enabled() ----------
print("Search Box is enabled :", search_box.is_enabled())

time.sleep(2)

# is_selected() ----------
register = driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()
male = driver.find_element(By.CSS_SELECTOR, "#gender-male")
female = driver.find_element(By.CSS_SELECTOR, "#gender-female")
female.click()

print("Male Button :", male.is_selected())
print("Female Button :", female.is_selected())


driver.quit()

