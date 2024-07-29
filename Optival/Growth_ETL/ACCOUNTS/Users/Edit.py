import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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


# Edit User

users = driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
time.sleep(1)
edit_user = driver.find_element(By.XPATH, "//a[normalize-space()='test@solivatech.com']").click()
time.sleep(1)

# If you edit any permission then give the locator of the changing element.

save_button = driver.find_element(By.NAME, "_save").click()
time.sleep(1)




# Error handling :

try:
    error_message = driver.find_element(By.XPATH, "//li[normalize-space()='User with this Email Address already exists.']").text
    print(error_message)

# Need to add more error handling for other fields

except (TimeoutException, NoSuchElementException):
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


driver.quit()
