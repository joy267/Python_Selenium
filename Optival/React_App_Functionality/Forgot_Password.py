import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Browser_Setup

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()


# Open_the_Product

aladdin_reset_password = driver.get("https://aladin-ui-stage.etloptival.com/reset-password")


# Forgot_Password

# forgot_password = driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()
# time.sleep(1)
# back_to_login = driver.find_element(By.XPATH, "//button[normalize-space()='Back to Login']").click()
# time.sleep(1)
# forgot_password_email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys("mrityunjoy@solivatech.com")
# time.sleep(1)
# reset_password = driver.find_element(By.XPATH, "//button[normalize-space()='Forgot Password']").click()
# time.sleep(2)


forgot_password = driver.find_element(By.XPATH, "//div[@class='LoginSection_additionalActions__Mk3CN']/a").click()
time.sleep(1)
back_to_login = driver.find_element(By.XPATH, "//button[normalize-space()='Back to Login']").click()
time.sleep(1)
forgot_password_email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys("mrityunjoy@solivatech.com")
time.sleep(1)
reset_password = driver.find_element(By.XPATH, "//button[normalize-space()='Forgot Password']").click()
time.sleep(2)



driver.quit()