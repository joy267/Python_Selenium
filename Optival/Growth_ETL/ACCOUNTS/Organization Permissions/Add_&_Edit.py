import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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


# Add

add_button = driver.find_element(By.LINK_TEXT, "Add")
add_button.click()

time.sleep(1)

username_dropdown = driver.find_element(By.XPATH, "(//span[@role='combobox'])[1]")
time.sleep(1)
username_dropdown.click()
time.sleep(1)
username_search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
time.sleep(2)
username_search_box.send_keys("test@solivatech.com")
time.sleep(2)
username_search_box.send_keys(Keys.ENTER)
time.sleep(1)


organization = driver.find_element(By.XPATH, "(//span[@role='combobox'])[2]")
time.sleep(1)
organization.click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[normalize-space()='Datawave LTD']").click()
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save").click()


try:
    error_message = driver.find_element(By.XPATH, "//p[@class='errornote']").is_displayed()
    expected_error_message = "Organization permission with this User already exists."
    time.sleep(1)
    actual_error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist']").text
    time.sleep(1)
    print("Organization permission with this User already exists.")

except (TimeoutException, NoSuchElementException):
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


# Back to home page

driver.find_element(By.XPATH, "//a[normalize-space()='Home']").click()
time.sleep(1)


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








driver.quit()