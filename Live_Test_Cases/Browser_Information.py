
# This page, upon clicking the 'Browser Type' button, detects the name of your browser and displays it for you.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/my-browser")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id='browser-toggle']").click()

Codename = driver.find_element(By.ID, "browser-code-name").text
print("The Codename is",Codename)
Name = driver.find_element(By.ID, "browser-name").text
print("The Name is", Name)
Version = driver.find_element(By.ID, "browser-version").text
print("The version is", Version)
Platform = driver.find_element(By.ID, "browser-platform").text
print("The Platform is", Platform)


driver.quit()