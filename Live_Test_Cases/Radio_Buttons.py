
# Radio Buttons example can be used for practicing automated tests.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/radio-buttons")
driver.maximize_window()

driver.find_element(By.ID, "red").click()
driver.find_element(By.ID, "basketball").click()






driver.quit()