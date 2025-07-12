import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

s = Service("C:\\Projects\\Selenium_Automation\\Chomedriver\\chromedriver-win64\\chromedriver.exe")
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
time.sleep(3)

# If you edit any permission then give the locator of the changing element.

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

save = driver.find_element(By.XPATH, "//input[@name='_save']").click()
time.sleep(1)


# Error handling :

success_message = driver.find_element(By.XPATH, "//li[@class='success']")

if success_message.is_displayed():
    print(success_message.text)

else:
    print("The user changes is fail")



driver.quit()



driver.quit()
