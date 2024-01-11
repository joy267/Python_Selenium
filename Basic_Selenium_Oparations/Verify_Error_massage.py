# Basic_Selenium_Oparations
# ---------------
# 1. Open Web Browser(Chrome/firefox/IE).
# 2. Open URL https://practicetestautomation.com/practice-test-login/
# 3. Provide Username (incorrectUser).
# 4. Provide Password (Password123).
# 5. Click on Login.
# 6. Capture the error message. (Actual message)
# 7. Verify the error message : "Your username is invalid!" (Expected)
# 8. Close Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

driver.find_element(By.NAME, "username").send_keys("incorrectUser")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

act_error = driver.find_element(By.XPATH, "//div[@id='error']").text
exp_error = "Your username is invalid!"

if act_error == exp_error:
    print("Test Pass")
else:
    print("Test Fail")

driver.close()
