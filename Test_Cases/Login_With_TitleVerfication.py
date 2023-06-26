# Test_Cases
# ---------------
# 1. Open Web Browser(Chrome/firefox/IE).
# 2. Open URL https://practicetestautomation.com/practice-test-login/
# 3. Provide Username (student).
# 4. Provide Password (Password123).
# 5. Click on Login.
# 6. Capture title of the dashboard page. (Actual title)
# 7. Verify title of the page: "Logged In Successfully | Practice Test Automation" (Expected)
# 8. Close Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")
driver.find_element(By.ID,"submit").click()

act_title = driver.title
exp_title = "Logged In Successfully | Practice Test Automation"

if act_title == exp_title:
    print("Logging Test Pass")
else:
    print("Logging Test Fail")

driver.close()