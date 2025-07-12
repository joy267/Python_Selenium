from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service




options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)

driver.get("https://practice.expandtesting.com/login")

driver.find_element(By.ID, "username").send_keys("practice")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(By.PARTIAL_LINK_TEXT, "Login").click()
