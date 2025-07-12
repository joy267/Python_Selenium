import time

# This page presents examples of various JavaScript Dialogs which can pose challenges for automation efforts.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get("https://practice.expandtesting.com/js-dialogs")
time.sleep(2)

# Accept the JS alert.

button_1 = driver.find_element(By.ID, "js-alert").text
driver.find_element(By.ID, "js-alert").click()
time.sleep(1)

js_alert = driver.switch_to.alert
time.sleep(1)
print(button_1)
js_alert.accept()

Dialog_Response = driver.find_element(By.ID, "dialog-response").text
print ("Dialog Response :", Dialog_Response)

time.sleep(2)

# Dismiss the JS alert.

button_2 = driver.find_element(By.ID, "js-confirm").text
driver.find_element(By.ID, "js-confirm").click()
time.sleep(1)
print(button_2)

js_confirm = driver.switch_to.alert
js_confirm.dismiss()

Dialog_Response = driver.find_element(By.ID, "dialog-response").text
print ("Dialog Response :", Dialog_Response)

time.sleep(2)

# Send inputs into the JS prompt.

button_3 = driver.find_element(By.ID, "js-prompt").text
driver.find_element(By.ID, "js-prompt").click()
time.sleep(1)
print(button_3)

js_prompt = driver.switch_to.alert
js_prompt.send_keys("Joy Mandal")
js_prompt.accept()

Dialog_Response = driver.find_element(By.ID, "dialog-response").text
print ("Dialog Response :", Dialog_Response)


driver.quit()


