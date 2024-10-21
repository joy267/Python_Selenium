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


# Add Website

add_button = driver.find_element(By.XPATH, "//tr[@class='model-website']/td[1]")
add_button.click()
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
organization.click()
time.sleep(1)
organization.send_keys(Keys.DOWN)
organization.send_keys(Keys.ENTER)
time.sleep(1)

site_name = driver.find_element(By.NAME, "site_name")
site_name.send_keys(f"Test Website {random.randint(1,10000000)}")
time.sleep(1)

site_url = driver.find_element(By.NAME, "site_url")
site_url.send_keys(f"https://www.testwebsite{random.randint(0,10000000)}.com")
time.sleep(1)

site_type = driver.find_element(By.NAME, "site_type")
site_type.click()
time.sleep(1)
site_type.send_keys(Keys.DOWN)
site_type.send_keys(Keys.ENTER)
time.sleep(1)

industry = driver.find_element(By.NAME,"industry")
industry.click()
time.sleep(1)
industry.send_keys(Keys.DOWN)
industry.send_keys(Keys.ENTER)
time.sleep(1)

territory = driver.find_element(By.NAME,"territory")
territory.click()
time.sleep(1)
territory.send_keys(Keys.DOWN)
territory.send_keys(Keys.ENTER)
time.sleep(1)

website_username = driver.find_element(By.NAME, "website_username")
website_username.send_keys("Aladdin")
time.sleep(1)

application_password = driver.find_element(By.NAME, "application_password")
application_password.send_keys("wwee ssda adwd csea")
time.sleep(1)

finance_activity = driver.find_element(By.NAME, "finance_activity")
finance_activity.click()
finance_activity.send_keys(Keys.DOWN)
finance_activity.send_keys(Keys.ENTER)
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
    organization.click()
    time.sleep(1)
    organization.send_keys(Keys.DOWN)
    organization.send_keys(Keys.ENTER)
    time.sleep(1)

    site_name = driver.find_element(By.NAME, "site_name")
    site_name.clear()
    site_name.send_keys(f"Test Website {random.randint(1,10000000)}")
    time.sleep(1)

    site_url = driver.find_element(By.NAME, "site_url")
    site_url.clear()
    site_url.send_keys(f"https://www.testwebsite{random.randint(0, 10000000)}.com")
    time.sleep(1)

    site_type = driver.find_element(By.NAME, "site_type")
    site_type.click()
    time.sleep(1)
    site_type.send_keys(Keys.DOWN)
    site_type.send_keys(Keys.ENTER)
    time.sleep(1)

    industry = driver.find_element(By.NAME, "industry")
    industry.click()
    time.sleep(1)
    industry.send_keys(Keys.DOWN)
    industry.send_keys(Keys.ENTER)
    time.sleep(1)

    territory = driver.find_element(By.NAME, "territory")
    territory.click()
    time.sleep(1)
    territory.send_keys(Keys.DOWN)
    territory.send_keys(Keys.ENTER)
    time.sleep(1)

    website_username = driver.find_element(By.NAME, "website_username")
    website_username.send_keys("Aladdin")
    time.sleep(1)

    application_password = driver.find_element(By.NAME, "application_password")
    application_password.clear()
    application_password.send_keys("wwee ssda adwd csea")
    time.sleep(1)

    finance_activity = driver.find_element(By.NAME, "finance_activity")
    finance_activity.click()
    finance_activity.send_keys(Keys.DOWN)
    finance_activity.send_keys(Keys.ENTER)
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


# Change Website

edit_website = driver.find_element(By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_website.click()
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
organization.click()
time.sleep(1)
organization.send_keys(Keys.DOWN)
organization.send_keys(Keys.ENTER)
time.sleep(1)

site_name = driver.find_element(By.NAME, "site_name")
site_name.clear()
site_name.send_keys(f"Test Website {random.randint(1,10000000)}")
time.sleep(1)

site_url = driver.find_element(By.NAME, "site_url")
site_url.clear()
site_url.send_keys(f"https://www.testwebsite{random.randint(0, 10000000)}.com")
time.sleep(1)

site_type = driver.find_element(By.NAME, "site_type")
site_type.click()
time.sleep(1)
site_type.send_keys(Keys.DOWN)
site_type.send_keys(Keys.ENTER)
time.sleep(1)

industry = driver.find_element(By.NAME, "industry")
industry.click()
time.sleep(1)
industry.send_keys(Keys.DOWN)
industry.send_keys(Keys.ENTER)
time.sleep(1)

territory = driver.find_element(By.NAME, "territory")
territory.click()
time.sleep(1)
territory.send_keys(Keys.DOWN)
territory.send_keys(Keys.ENTER)
time.sleep(1)

website_username = driver.find_element(By.NAME, "website_username")
website_username.send_keys("Aladdin")
time.sleep(1)

application_password = driver.find_element(By.NAME, "application_password")
application_password.clear()
application_password.send_keys("wwee ssda adwd csea")
time.sleep(1)

finance_activity = driver.find_element(By.NAME, "finance_activity")
finance_activity.click()
finance_activity.send_keys(Keys.DOWN)
finance_activity.send_keys(Keys.ENTER)
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
    organization.click()
    time.sleep(1)
    organization.send_keys(Keys.DOWN)
    organization.send_keys(Keys.ENTER)
    time.sleep(1)

    site_name = driver.find_element(By.NAME, "site_name")
    site_url.clear()
    site_url.send_keys(f"https://www.testwebsite{random.randint(0, 10000000)}.com")
    time.sleep(1)

    site_type = driver.find_element(By.NAME, "site_type")
    site_url.clear()
    site_url.send_keys(f"https://www.testwebsite{random.randint(0, 10000000)}.com")
    time.sleep(1)

    site_type = driver.find_element(By.XPATH, "site_type")
    site_type.click()
    time.sleep(1)
    site_type.send_keys(Keys.DOWN)
    site_type.send_keys(Keys.ENTER)
    time.sleep(1)

    industry = driver.find_element(By.NAME, "industry")
    industry.click()
    time.sleep(1)
    industry.send_keys(Keys.DOWN)
    industry.send_keys(Keys.ENTER)
    time.sleep(1)

    territory = driver.find_element(By.NAME, "territory")
    territory.click()
    time.sleep(1)
    territory.send_keys(Keys.DOWN)
    territory.send_keys(Keys.ENTER)
    time.sleep(1)

    website_username = driver.find_element(By.NAME, "website_username")
    website_username.send_keys("Aladdin")
    time.sleep(1)

    application_password = driver.find_element(By.NAME, "application_password")
    application_password.clear()
    application_password.send_keys("wwee ssda adwd csea")
    time.sleep(1)

    finance_activity = driver.find_element(By.NAME, "finance_activity")
    finance_activity.click()
    finance_activity.send_keys(Keys.DOWN)
    finance_activity.send_keys(Keys.ENTER)
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
