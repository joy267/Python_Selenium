
# This is an example of using input fields such as numbers, text, passwords, or dates on a website.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)


driver.get("https://practice.expandtesting.com/inputs")
driver.maximize_window()

driver.find_element(By.ID, "input-number" ).send_keys("102")
driver.find_element(By.ID, "input-text").send_keys("admin")
driver.find_element(By.ID, "input-password").send_keys("1234")
driver.find_element(By.ID, "input-date").send_keys("26/07/1998")
driver.find_element(By.ID, "btn-display-inputs").click()

driver.quit()