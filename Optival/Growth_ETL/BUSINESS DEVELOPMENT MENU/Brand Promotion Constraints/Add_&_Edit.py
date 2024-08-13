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


# Add Brand Promotion Constraints

add_button = driver.find_element(By.XPATH, "//tr[@class='model-brandpromotionconstraints']/td[1]").click()
time.sleep(1)

brand = driver.find_element(By.XPATH, "//span[@role='combobox']")
time.sleep(1)
brand.click()
time.sleep(1)

search_brands = driver.find_element(By.XPATH,"//input[@role='searchbox']")
time.sleep(1)
search_brands.send_keys("888 Mobile")
time.sleep(1)
search_brands.send_keys(Keys.ENTER)
time.sleep(1)

select_month = driver.find_element(By.XPATH,"//select[@class='django-yearmonth-widget-year-selector']")
time.sleep(1)
select_month.click()
time.sleep(1)
select_month.send_keys(Keys.DOWN)
select_month.send_keys(Keys.ENTER)
time.sleep(1)

select_date = driver.find_element(By.XPATH,"//select[@class='django-yearmonth-widget-month-selector']")
time.sleep(1)
select_date.click()
time.sleep(1)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.ENTER)
time.sleep(1)

cpa_income = driver.find_element(By.NAME, "cpa_income")
time.sleep(1)
cpa_income.send_keys("100")
time.sleep(1)

total_income = driver.find_element(By.NAME, "totalincome")
time.sleep(1)
total_income.send_keys("1000")
time.sleep(1)

max_position = driver.find_element(By.NAME,"max_position")
time.sleep(1)
max_position.send_keys("1")

min_position = driver.find_element(By.NAME,"min_position")
time.sleep(1)
min_position.send_keys("5")


save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)



try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print("888 Mobile:", success_message)


except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)

    select_month = driver.find_element(By.XPATH, "//select[@class='django-yearmonth-widget-year-selector']")
    time.sleep(1)
    select_month.click()
    time.sleep(1)
    select_month.send_keys(Keys.DOWN)
    select_month.send_keys(Keys.DOWN)
    select_month.send_keys(Keys.ENTER)
    time.sleep(1)

    select_date = driver.find_element(By.XPATH, "//select[@class='django-yearmonth-widget-month-selector']")
    time.sleep(1)
    select_date.click()
    time.sleep(1)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.ENTER)
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)


    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)



# Change Brand Promotion Constraints

edit_brand_product = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_brand_product.click()
time.sleep(1)

brand = driver.find_element(By.XPATH, "//span[@role='combobox']")
time.sleep(1)
brand.click()
time.sleep(1)

search_brands = driver.find_element(By.XPATH,"//input[@role='searchbox']")
time.sleep(1)
search_brands.send_keys("Bet365 bingo")
time.sleep(1)
search_brands.send_keys(Keys.ENTER)
time.sleep(1)

select_month = driver.find_element(By.XPATH,"//select[@class='django-yearmonth-widget-year-selector']")
time.sleep(1)
select_month.click()
time.sleep(1)
select_month.send_keys(Keys.DOWN)
select_month.send_keys(Keys.ENTER)
time.sleep(1)

select_date = driver.find_element(By.XPATH,"//select[@class='django-yearmonth-widget-month-selector']")
time.sleep(1)
select_date.click()
time.sleep(1)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.DOWN)
select_date.send_keys(Keys.ENTER)
time.sleep(1)

cpa_income = driver.find_element(By.NAME, "cpa_income")
time.sleep(1)
cpa_income.clear()
time.sleep(1)
cpa_income.send_keys("10")
time.sleep(1)

total_income = driver.find_element(By.NAME, "totalincome")
time.sleep(1)
total_income.clear()
time.sleep(1)
total_income.send_keys("1000")
time.sleep(1)

max_position = driver.find_element(By.NAME,"max_position")
time.sleep(1)
max_position.clear()
time.sleep(1)
max_position.send_keys("1")

min_position = driver.find_element(By.NAME,"min_position")
time.sleep(1)
min_position.clear()
time.sleep(1)
min_position.send_keys("5")


save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)


try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print("Bet365 bingo:", success_message)

except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)

    select_month = driver.find_element(By.XPATH, "//select[@class='django-yearmonth-widget-year-selector']")
    time.sleep(1)
    select_month.click()
    time.sleep(1)
    select_month.send_keys(Keys.DOWN)
    select_month.send_keys(Keys.DOWN)
    select_month.send_keys(Keys.ENTER)
    time.sleep(1)

    select_date = driver.find_element(By.XPATH, "//select[@class='django-yearmonth-widget-month-selector']")
    time.sleep(1)
    select_date.click()
    time.sleep(1)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.DOWN)
    select_date.send_keys(Keys.ENTER)
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)


# except(NoSuchElementException):
#     print("The element is not present in the webpage")
#
# except (TimeoutException):
#     print("Timeout Error")


driver.quit()