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


# Add User

add_user = driver.find_element(By.XPATH, "//tr[@class='model-user']//td[1]").click()
time.sleep(1)
email = driver.find_element(By.NAME, "email").send_keys("test@solivatech.com")
time.sleep(1)
first_name = driver.find_element(By.NAME, "first_name").send_keys("Test")
time.sleep(1)
last_name = driver.find_element(By.NAME, "last_name").send_keys("User")
time.sleep(1)
password = driver.find_element(By.NAME, "password1").send_keys("123456789")
time.sleep(1)
confirm_password = driver.find_element(By.NAME, "password2").send_keys("123456789")
time.sleep(1)


# Is Active Button
is_active_button = driver.find_element(By.NAME, "is_active").click()
time.sleep(1)

# Is Staff
is_staff = driver.find_element(By.NAME, "is_staff").click()
time.sleep(1)

# Superuser Button
superuser_button = driver.find_element(By.NAME, "is_superuser").click()
time.sleep(1)


# Group Selection
group_1 = driver.find_element(By.XPATH, "//option[@title='Biz Dev member']").click()
time.sleep(1)
group_2 = driver.find_element(By.XPATH, "//option[@title='Business Manager']").click()
time.sleep(1)
actions = ActionChains(driver)
actions.double_click(group_1).perform()
actions.double_click(group_2).perform()
time.sleep(1)
choose_button = driver.find_element(By.XPATH, "//a[@id='id_groups_add_link']").click()
time.sleep(1)

# Save
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
