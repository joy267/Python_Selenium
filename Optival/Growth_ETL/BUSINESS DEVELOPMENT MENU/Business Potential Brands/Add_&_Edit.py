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


# Add Business Potential Brands

add_button = driver.find_element(By.XPATH, "//tr[@class='model-businesspotentialbrand']/td[1]").click()
time.sleep(1)

brand_name = driver.find_element(By.NAME, "brand_name")
add_brand_name = brand_name.send_keys(f"test_brand_{random.randint(0, 1000000)}")
time.sleep(1)

brand_display_name = driver.find_element(By.XPATH, "//span[@role='combobox']")
time.sleep(1)
brand_display_name.click()
time.sleep(1)

search_brand_display_name = driver.find_element(By.XPATH, "//input[@role='searchbox']")
search_brand_display_name.send_keys("777 Casino UK")
time.sleep(1)
search_brand_display_name.send_keys(Keys.ENTER)
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)

try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)

except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)

    brand_name = driver.find_element(By.NAME, "brand_name")
    time.sleep(1)
    brand_name.clear()
    time.sleep(1)
    add_brand_name = brand_name.send_keys(f"test_brand_{random.randint(0, 1000000)}")
    time.sleep(1)

    brand_display_name = driver.find_element(By.XPATH, "//span[@role='combobox']")
    time.sleep(1)
    brand_display_name.click()
    time.sleep(1)

    search_brand_display_name = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    search_brand_display_name.send_keys("BoyleSports Sport UK")
    time.sleep(1)
    search_brand_display_name.send_keys(Keys.ENTER)
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


# Change Business Potential Brands

edit_business_potential_brands = driver.find_element(By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_business_potential_brands.click()
time.sleep(1)

brand_display_name = driver.find_element(By.XPATH, "//span[@role='textbox']")
time.sleep(1)
brand_display_name.click()
time.sleep(1)

search_brand_display_name = driver.find_element(By.XPATH, "//input[@role='searchbox']")
search_brand_display_name.send_keys("Foxy Bingo UK")
time.sleep(1)
search_brand_display_name.send_keys(Keys.ENTER)
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)

success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
print(success_message)

try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)

except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)

    brand_display_name = driver.find_element(By.XPATH, "//span[@role='combobox']")
    time.sleep(1)
    brand_display_name.click()
    time.sleep(1)

    search_brand_display_name = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    search_brand_display_name.send_keys("888 Casino UK")
    time.sleep(1)
    search_brand_display_name.send_keys(Keys.ENTER)
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
