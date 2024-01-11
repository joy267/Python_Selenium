from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Select a perticular checkbox

#driver.find_element(By.ID, "sunday").click()

# 2. Select all checkboxes

checkboxes=driver.find_element(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")


# Approach 1

#for i in range(len('checkbox')):
    #checkboxes[i].click()

# Approach 2

#for checkbox in checkboxes:
    #checkbox.click()

# 3. Select some checkboxes

for checkbox in checkboxes:
    weekname=checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday':
        checkbox.click()


