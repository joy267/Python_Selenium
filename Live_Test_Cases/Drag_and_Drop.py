import time

# Example (Drag and Drop) can be used for practicing Drag and Drop challenges in automated tests.

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/drag-and-drop")
driver.maximize_window()

time.sleep(3)

A = driver.find_element(By.ID, "column-a")
B = driver.find_element(By.ID, "column-b")

action = ActionChains(driver)
action.drag_and_drop(A, B).perform()


driver.quit()