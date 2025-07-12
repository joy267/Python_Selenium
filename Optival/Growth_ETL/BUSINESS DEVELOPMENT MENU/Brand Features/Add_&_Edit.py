from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import time

s = Service("C:\\Projects\\Selenium_Automation\\Chomedriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)


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


# Add Brand Display Name

add_button = driver.find_element(By.XPATH, "//tr[@class='model-brandfeature']/td[1]").click()
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
time.sleep(1)
organization.send_keys(Keys.ENTER)
time.sleep(1)

select_organization = driver.find_element(By.XPATH, "//select[@name='organization']/option[normalize-space()='Optival LTD']")
time.sleep(1)
select_organization.click()
time.sleep(1)

feature_name = driver.find_element(By.NAME,"feature_name")
time.sleep(1)
feature_name.send_keys("test feature 1")
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

    organization = driver.find_element(By.NAME, "organization")
    time.sleep(1)
    organization.click()
    time.sleep(1)

    select_organization = driver.find_element(By.XPATH,"//select[@name='organization']/option[normalize-space()='Optival LTD']")
    time.sleep(1)
    select_organization.click()
    time.sleep(1)

    feature_name = driver.find_element(By.NAME, "feature_name")
    time.sleep(1)
    feature_name.clear()
    feature_name.send_keys(f"test feature {random.random()}")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)



# Change website for brand display name

edit_brand_feature = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_brand_feature.click()
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
time.sleep(1)
organization.click()
time.sleep(1)

select_organization = driver.find_element(By.XPATH,"//select[@name='organization']/option[normalize-space()='Optival LTD']")
time.sleep(1)
select_organization.click()
time.sleep(1)

feature_name = driver.find_element(By.NAME, "feature_name")
time.sleep(1)
feature_name.clear()
feature_name.send_keys("test feature 2")
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)


try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)

except():
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist']").text
    print(error_message)
    time.sleep(1)

    organization = driver.find_element(By.NAME, "organization")
    time.sleep(1)
    organization.click()
    time.sleep(1)

    select_organization = driver.find_element(By.XPATH,"//select[@name='organization']/option[normalize-space()='Optival LTD']")
    time.sleep(1)
    select_organization.click()
    time.sleep(1)

    feature_name = driver.find_element(By.NAME, "feature_name")
    time.sleep(1)
    feature_name.clear()
    feature_name.send_keys(f"test feature {random.random()}")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

except(NoSuchElementException):
    print("The element is not present in the webpage")

except (TimeoutException):
    print("Timeout Error")


driver.quit()