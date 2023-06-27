# Test_Cases
# ---------------
# 1. Open Web Browser(Chrome/firefox/IE).
# 2. Open URL https://practicetestautomation.com/practice-test-exceptions/
# 3. Open page.
# 4. Click Add button.
# 5. Verify Row 2 input field is displayed.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-exceptions/")
driver.maximize_window()

driver.find_element(By.ID, "add_btn").click()

act_out = driver.find_element(By.CLASS_NAME, "input-field")
exp_out = driver.find_element(By.CSS_SELECTOR, "input[type=text]")

if act_out == exp_out:
    print("Row 2 input field is displayed")
else:
    print("Row 2 input field is not displayed")

driver.close()