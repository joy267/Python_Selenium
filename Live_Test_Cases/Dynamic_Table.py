
# Generating dynamic table content on every page load can be used as a practice exercise to verify cell values in a dynamic table.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/dynamic-table")
driver.maximize_window()

Actual_CPU_Value = driver.find_element(By.XPATH, "//tr[contains(.,'Chrome')]//td[contains(.,'%')]").text
print("Chrome CPU:", Actual_CPU_Value)

Expected_CPU_Value = driver.find_element(By.XPATH, "//p[contains(.,'%')]").text
print(Expected_CPU_Value)



driver.quit()