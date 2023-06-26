from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@id='submit']").click()