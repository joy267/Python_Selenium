from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time

s = Service("C:\\Projects\\Selenium_Automation\\Chomedriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)


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


# Add Brand Details

add_button = driver.find_element(By.XPATH, "//tr[@class='model-branddetails']/td[1]").click()
time.sleep(1)

brand_id = "1960"

add_brand_id = driver.find_element(By.NAME, "brand_id")
add_brand_id.send_keys(brand_id)
time.sleep(1)

passwd_valid = driver.find_element(By.NAME, "passwd_valid")
passwd_valid.clear()
passwd_valid.send_keys("1")
time.sleep(1)

select_brand_group_details = driver.find_element(By.NAME, "brand_group_details").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[normalize-space()='10bet']").click()
time.sleep(1)

run_from_date = driver.find_element(By.XPATH,"//span[@class='datetimeshortcuts']/a[normalize-space()='Today']")
run_from_date.click()
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)



try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist']").text
    print(error_message)
    time.sleep(1)
    brand_details_list = driver.find_element(By.XPATH, "//div[@class='breadcrumbs']/a[normalize-space()='Brand Details']")
    brand_details_list.click()
    time.sleep(1)
    edit_existing_brand_details = driver.find_element(By.XPATH,"//td[normalize-space()='1960']/preceding-sibling::th")
    time.sleep(2)
    edit_existing_brand_details.click()
    time.sleep(1)

    passwd_valid = driver.find_element(By.NAME, "passwd_valid")
    passwd_valid.clear()
    time.sleep(1)
    passwd_valid.send_keys("2")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


try:
    print("Test Case is pass successfully")

except (NoSuchElementException):
    print("The element is not present in the webpage")
except (TimeoutException):
    print("Timeout Error")



driver.quit()