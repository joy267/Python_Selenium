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
wait = WebDriverWait(driver, 10)
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]


# Growth_ETL URL -

driver.maximize_window()
driver.get("https://staging.etloptival.com/admin/")


# Login Credentials

username = driver.find_element(By.NAME, "username")
username.send_keys("mrityunjoy@solivatech.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("killerboyz567")

login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
login_button.click()

time.sleep(2)


# Add Territories

add_button = driver.find_element(By.XPATH, "//tr[@class='model-territories']/td[1]")
add_button.click()
time.sleep(1)

territory_name = driver.find_element(By.NAME, "territory_name")
territory_name.send_keys(f"test territory {random.randint(0,10000000000)}")
time.sleep(1)

language = driver.find_element(By.NAME, "language")
language.send_keys("Eng")
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

    territory_name = driver.find_element(By.NAME, "territory_name")
    territory_name.clear()
    territory_name.send_keys(f"test territory {random.randint(0, 10000000000)}")
    time.sleep(1)

    language = driver.find_element(By.NAME, "language")
    language.clear()
    language.send_keys("Hin")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


# Change Territories

edit_companies = driver.find_element(By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_companies.click()
time.sleep(1)

territory_name = driver.find_element(By.NAME, "territory_name")
territory_name.clear()
territory_name.send_keys(f"test territory {random.randint(0, 10000000000)}")
time.sleep(1)

language = driver.find_element(By.NAME, "language")
language.clear()
language.send_keys("Ben")
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)

try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)

except():
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)

    territory_name = driver.find_element(By.NAME, "territory_name")
    territory_name.clear()
    territory_name.send_keys(f"test territory {random.randint(0, 10000000000)}")
    time.sleep(1)

    language = driver.find_element(By.NAME, "language")
    language.clear()
    language.send_keys("tam")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)

except NoSuchElementException:
    print("The element is not present in the webpage")

except TimeoutException:
    print("Timeout Error")

driver.quit()
