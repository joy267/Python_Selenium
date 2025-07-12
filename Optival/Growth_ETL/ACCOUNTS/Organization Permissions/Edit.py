import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)


# Growth_ETL URL -

driver.maximize_window()
driver.get("https://staging.etloptival.com/admin/")


# Login Credencials

username = driver.find_element(By.NAME, "username")
username.send_keys("mrityunjoy@solivatech.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("killerboyz567")

login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
login_button.click()

time.sleep(2)


# Change/Edit

edit_button = driver.find_element(By.XPATH, "//a[normalize-space()='Organization permissions']").click()
time.sleep(1)

edit_user = driver.find_element(By.XPATH, "//th[@class='field-user nowrap']//a[contains(text(),'test@solivatech.com')]").click()
time.sleep(1)

change_organization = driver.find_element(By.XPATH, "//span[@id='select2-id_organization_id-container']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[normalize-space()='Optival LTD']").click()
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save").click()

warning_text = driver.switch_to.alert
warning_text.accept()
time.sleep(3)

success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
print(success_message)



driver.quit()