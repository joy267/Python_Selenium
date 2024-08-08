from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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


# Add Brand Account

add_button = driver.find_element(By.XPATH, "//tr[@class='model-brandaccounts']/td[1]").click()
time.sleep(1)

login_url = driver.find_element(By.NAME, "login_url").send_keys("https://www.google.com")
time.sleep(1)
user_name = driver.find_element(By.NAME, "username").send_keys("testuser@solivatech.com")
time.sleep(1)
account_type = driver.find_element(By.NAME, "account_type").click()
time.sleep(1)
select_account = driver.find_element(By.XPATH,"//option[@value='Single_brand']").click()
time.sleep(1)
is_active = driver.find_element(By.NAME,"isactive").send_keys("1")
time.sleep(1)
dynamic_var = driver.find_element(By.NAME,"dynamic_var").send_keys("test dynamic var")
time.sleep(1)
keeper_id = driver.find_element(By.NAME,"keeper_id").send_keys("234424")
time.sleep(1)
orgnanization = driver.find_element(By.NAME,"organization").click()
time.sleep(1)
select_org = driver.find_element(By.XPATH, "//option[@value='1']").click()
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save").click()
time.sleep(1)


try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


# Existing brand account

except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)
    click_brand_account = driver.find_element(By.XPATH, "//div[@class='breadcrumbs']/a[3]").click()
    time.sleep(1)
    search_brand_account = driver.find_element(By.ID, "searchbar").send_keys("testuser@solivatech.com")
    time.sleep(1)
    search_button = driver.find_element(By.XPATH, "//form[@id='changelist-search']//input[@value='Search']").click()
    time.sleep(1)
    brand_user = driver.find_element(By.XPATH, "//a[normalize-space()='testuser@solivatech.com']").click()
    time.sleep(1)
    edit_dynamic_var = driver.find_element(By.NAME, "dynamic_var")
    edit_dynamic_var.clear()
    edit_dynamic_var.send_keys("test dynamic var 1")
    time.sleep(1)
    save_button = driver.find_element(By.NAME, "_save").click()
    time.sleep(1)
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)




driver.quit()