
 # This example shows a dynamic notification message that can be used for practicing automated testing.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://practice.expandtesting.com/notification-message-rendered")
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT, "Click here").click()

notification = driver.find_element(By.ID,"flash-message")
print(notification.text)

driver.quit()