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


# Add Brand Parents

add_button = driver.find_element(By.XPATH, "//tr[@class='model-brandparent']/td[1]").click()
time.sleep(1)

company = driver.find_element(By.XPATH, "//span[@role='combobox']")
time.sleep(1)
company.click()
time.sleep(1)

search_company = driver.find_element(By.XPATH,"//input[@role='searchbox']")
time.sleep(1)
search_company.send_keys("BoyleSports Ltd")
time.sleep(1)
search_company.send_keys(Keys.ENTER)
time.sleep(1)

brand_parent_name = driver.find_element(By.NAME,"brand_parent_name")
time.sleep(1)
brand_parent_name.send_keys("brand_parent_1")
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

    company = driver.find_element(By.XPATH, "//span[@role='combobox']")
    time.sleep(1)
    company.click()
    time.sleep(1)

    search_company = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    time.sleep(1)
    search_company.send_keys("BoyleSports Ltd")
    time.sleep(1)
    search_company.send_keys(Keys.ENTER)
    time.sleep(1)

    brand_parent_name = driver.find_element(By.NAME, "brand_parent_name")
    time.sleep(1)
    brand_parent_name.clear()
    brand_parent_name.send_keys(f"brand_parent_{random.random}")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)



# Change website for brand display name

edit_brand_parent = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_brand_parent.click()
time.sleep(1)

company = driver.find_element(By.XPATH, "//span[@role='combobox']")
time.sleep(1)
company.click()
time.sleep(1)

search_company = driver.find_element(By.XPATH,"//input[@role='searchbox']")
time.sleep(1)
search_company.send_keys("Ocean Star Limited")
time.sleep(1)
search_company.send_keys(Keys.ENTER)
time.sleep(1)

brand_parent_name = driver.find_element(By.NAME,"brand_parent_name")
time.sleep(1)
brand_parent_name.clear()
time.sleep(1)
brand_parent_name.send_keys("brand_parent_2")
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

    company = driver.find_element(By.XPATH, "//span[@role='combobox']")
    time.sleep(1)
    company.click()
    time.sleep(1)

    search_company = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    time.sleep(1)
    search_company.send_keys("Entain Plc")
    time.sleep(1)
    search_company.send_keys(Keys.ENTER)
    time.sleep(1)

    brand_parent_name = driver.find_element(By.NAME, "brand_parent_name")
    time.sleep(1)
    brand_parent_name.clear()
    time.sleep(1)
    brand_parent_name.send_keys(f"brand_parent_{random.random}")
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