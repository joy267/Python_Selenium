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


# Add Brand Products

add_button = driver.find_element(By.XPATH, "//tr[@class='model-brandproduct']/td[1]").click()
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
time.sleep(1)
organization.click()
time.sleep(1)

select_organization = driver.find_element(By.XPATH,"//select[@id='id_organization']")
time.sleep(1)
select_organization.send_keys(Keys.DOWN)
select_organization.send_keys(Keys.DOWN)
select_organization.send_keys(Keys.DOWN)
select_organization.send_keys(Keys.ENTER)
time.sleep(1)

product_name = driver.find_element(By.NAME,"product_name")
time.sleep(1)
add_product_name = product_name.send_keys(f"test_brand_product_{random.randint(0, 100000)}")
time.sleep(1)


save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)



try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(add_product_name, success_message)


except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(add_product_name, error_message)
    time.sleep(1)

    organization = driver.find_element(By.NAME, "organization")
    time.sleep(1)
    organization.click()
    time.sleep(1)

    select_organization = driver.find_element(By.XPATH, "//select[@id='id_organization']")
    time.sleep(1)
    select_organization.send_keys(Keys.DOWN)
    select_organization.send_keys(Keys.DOWN)
    select_organization.send_keys(Keys.ENTER)
    time.sleep(1)

    product_name = driver.find_element(By.NAME, "product_name")
    time.sleep(1)
    product_name.clear()
    time.sleep(1)
    product_name.send_keys(f"test_brand_product_{random.randint(0, 100000)}")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)


    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)



# Change Brand Product

edit_brand_product = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_brand_product.click()
time.sleep(1)

organization = driver.find_element(By.NAME, "organization")
time.sleep(1)
organization.click()
time.sleep(1)

select_organization = driver.find_element(By.XPATH, "//select[@id='id_organization']")
time.sleep(1)
select_organization.send_keys(Keys.DOWN)
select_organization.send_keys(Keys.DOWN)
select_organization.send_keys(Keys.ENTER)
time.sleep(1)

product_name = driver.find_element(By.NAME, "product_name")
time.sleep(1)
product_name.clear()
time.sleep(1)
edit_product_name = product_name.send_keys(f"test_brand_product_{random.randint(0, 100000)}")
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)


try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(edit_product_name, success_message)

except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(edit_product_name, error_message)
    time.sleep(1)

    organization = driver.find_element(By.NAME, "organization")
    time.sleep(1)
    organization.click()
    time.sleep(1)

    select_organization = driver.find_element(By.XPATH, "//select[@id='id_organization']")
    time.sleep(1)
    select_organization.send_keys(Keys.DOWN)
    select_organization.send_keys(Keys.DOWN)
    select_organization.send_keys(Keys.ENTER)
    time.sleep(1)

    product_name = driver.find_element(By.NAME, "product_name")
    time.sleep(1)
    product_name.clear()
    time.sleep(1)
    product_name.send_keys(f"test_brand_product_{random.randint(0, 10000)}")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)


    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


# except(NoSuchElementException):
#     print("The element is not present in the webpage")
#
# except (TimeoutException):
#     print("Timeout Error")


driver.quit()