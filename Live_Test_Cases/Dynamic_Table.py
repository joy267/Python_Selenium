
# Generating dynamic table content on every page load can be used as a practice exercise to verify cell values in a dynamic table.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/dynamic-table")
driver.maximize_window()

driver.find_element()