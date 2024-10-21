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


# Login Credentials

username = driver.find_element(By.NAME, "username")
username.send_keys("mrityunjoy@solivatech.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("killerboyz567")

login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
login_button.click()

time.sleep(2)


# Add Business Competitor

add_button = driver.find_element(By.XPATH, "//tr[@class='model-businesscompetitor']/td[1]").click()
time.sleep(1)

site_name = driver.find_element(By.NAME, "site_name")
add_site_name = site_name.send_keys(f"test_website_{random.randint(0,1000000)}")
time.sleep(1)

site_url = driver.find_element(By.NAME,"site_url")
time.sleep(1)
site_url.click()
time.sleep(1)
add_site_url = site_url.send_keys(f"https://www.testwebsite{random.randint(0,1000000)}.com")
time.sleep(1)

organization = driver.find_element(By.NAME,"organization")
time.sleep(1)
organization.click()
time.sleep(1)
organization.send_keys(Keys.DOWN)
organization.send_keys(Keys.ENTER)
time.sleep(1)

territory = driver.find_element(By.NAME,"territory")
time.sleep(1)
territory.click()
time.sleep(1)
territory.send_keys(Keys.DOWN)
territory.send_keys(Keys.ENTER)
time.sleep(1)

industry = driver.find_element(By.NAME,"industry")
time.sleep(1)
industry.click()
time.sleep(1)
industry.send_keys(Keys.DOWN)
industry.send_keys(Keys.ENTER)
time.sleep(1)


save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)



try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(add_site_name and add_site_url, success_message)


except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(add_site_name and add_site_url, error_message)
    time.sleep(1)

    site_name = driver.find_element(By.NAME, "site_name")
    time.sleep(1)
    site_name.clear()
    time.sleep(1)
    add_site_name = site_name.send_keys(f"test_website_{random.randint(0, 1000000)}")
    time.sleep(1)

    site_url = driver.find_element(By.NAME, "site_url")
    time.sleep(1)
    site_url.clear()
    time.sleep(1)
    add_site_url = site_url.send_keys(f"https://www.testwebsite{random.randint(0, 1000000)}.com")
    time.sleep(1)

    organization = driver.find_element(By.NAME, "organization")
    time.sleep(1)
    organization.click()
    time.sleep(1)
    organization.send_keys(Keys.DOWN)
    organization.send_keys(Keys.ENTER)
    time.sleep(1)

    territory = driver.find_element(By.NAME, "territory")
    time.sleep(1)
    territory.click()
    time.sleep(1)
    territory.send_keys(Keys.DOWN)
    territory.send_keys(Keys.ENTER)
    time.sleep(1)

    industry = driver.find_element(By.NAME, "industry")
    time.sleep(1)
    industry.click()
    time.sleep(1)
    industry.send_keys(Keys.DOWN)
    industry.send_keys(Keys.ENTER)
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)


    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)



# Change Business Competitor

edit_business_competitor = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_business_competitor.click()
time.sleep(1)

site_name = driver.find_element(By.NAME, "site_name")
time.sleep(1)
site_name.clear()
time.sleep(1)
edit_site_name = site_name.send_keys(f"test_website_{random.randint(0, 1000000)}")
time.sleep(1)

site_url = driver.find_element(By.NAME, "site_url")
time.sleep(1)
site_url.clear()
time.sleep(1)
edit_site_url = site_url.send_keys(f"https://www.testwebsite{random.randint(0, 1000000)}.com")
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
time.sleep(1)
organization.click()
time.sleep(1)
organization.send_keys(Keys.DOWN)
organization.send_keys(Keys.ENTER)
time.sleep(1)

territory = driver.find_element(By.NAME, "territory")
time.sleep(1)
territory.click()
time.sleep(1)
territory.send_keys(Keys.DOWN)
territory.send_keys(Keys.ENTER)
time.sleep(1)

industry = driver.find_element(By.NAME, "industry")
time.sleep(1)
industry.click()
time.sleep(1)
industry.send_keys(Keys.DOWN)
industry.send_keys(Keys.ENTER)
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)


try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(edit_site_name and edit_site_url, success_message)

except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(edit_site_name and edit_site_url, error_message)
    time.sleep(1)

    site_name = driver.find_element(By.NAME, "site_name")
    time.sleep(1)
    site_name.clear()
    time.sleep(1)
    edit_site_name = site_name.send_keys(f"test_website_{random.randint(0, 1000000)}")
    time.sleep(1)

    site_url = driver.find_element(By.NAME, "site_url")
    time.sleep(1)
    site_url.clear()
    time.sleep(1)
    edit_site_url = site_url.send_keys(f"https://www.testwebsite{random.randint(0, 1000000)}.com")
    time.sleep(1)

    organization = driver.find_element(By.NAME, "organization")
    time.sleep(1)
    organization.click()
    time.sleep(1)
    organization.send_keys(Keys.DOWN)
    organization.send_keys(Keys.ENTER)
    time.sleep(1)

    territory = driver.find_element(By.NAME, "territory")
    time.sleep(1)
    territory.click()
    time.sleep(1)
    territory.send_keys(Keys.DOWN)
    territory.send_keys(Keys.ENTER)
    time.sleep(1)

    industry = driver.find_element(By.NAME, "industry")
    time.sleep(1)
    industry.click()
    time.sleep(1)
    industry.send_keys(Keys.DOWN)
    industry.send_keys(Keys.ENTER)
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(edit_site_name and edit_site_url, success_message)


# except(NoSuchElementException):
#     print("The element is not present in the webpage")
#
# except (TimeoutException):
#     print("Timeout Error")


driver.quit()