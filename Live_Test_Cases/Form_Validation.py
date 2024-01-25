
# Example of Form Validation Using Bootstrap and JavaScript Technologies.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://practice.expandtesting.com/form-validation")
driver.maximize_window()


driver.find_element(By.ID, "validationCustom01").clear()
driver.find_element(By.ID, "validationCustom01").send_keys("admin")

driver.find_element(By.ID, "validationCustom05").send_keys("012-3456789")

driver.find_element(By.XPATH, "//input[@name='pickupdate']").send_keys("28-01-2024")

driver.find_element(By.ID, "validationCustom04").click()

driver.find_element(By.XPATH, "//option[@value='card']").click()

driver.find_element(By.XPATH, "//button[@type='submit']").click()

confirmation_text = driver.find_element(By.XPATH, "//div[@role='alert']").text
print(confirmation_text)

driver.quit()