import time

# This example utilizes Basic Auth, which can be used for practicing automated testing.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

time.sleep(2)

driver.get( "https://admin:admin@practice.expandtesting.com/basic-auth")
driver.maximize_window()


login_message = driver.find_element(By.XPATH, "//p[@class='alert alert-success']").text

print(login_message)


driver.quit()