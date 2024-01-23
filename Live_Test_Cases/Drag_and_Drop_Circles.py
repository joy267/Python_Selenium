import time

# Example (Drag and Drop Circles) can be used for practicing Drag and Drop challenges in automated tests.

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/drag-and-drop-circles")
driver.maximize_window()

time.sleep(3)

red = driver.find_element(By.CLASS_NAME, "red")
green = driver.find_element(By.CLASS_NAME, "green")
blue = driver.find_element(By.CLASS_NAME, "blue")
target = driver.find_element(By.ID, "target")

action = ActionChains(driver)
action.drag_and_drop(red, target).perform()
action.drag_and_drop(green, target).perform()
action.drag_and_drop(blue, target).perform()


driver.quit()