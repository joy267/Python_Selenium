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


# Add Brand Deal Plans

add_button = driver.find_element(By.XPATH, "//tr[@class='model-branddealplan']/td[1]").click()
time.sleep(1)
brand = driver.find_element(By.NAME, "brand")
brand.click()
time.sleep(1)
select_brand = driver.find_element(By.XPATH, "//select[@name='brand']/option[@value='3']").click()
time.sleep(1)
plan_term = driver.find_element(By.NAME, "plan_term").send_keys("test plan term")
time.sleep(1)
plan_name = driver.find_element(By.NAME, "plan_name").send_keys("test plan name")
time.sleep(1)
cpa = driver.find_element(By.NAME, "cpa")
cpa.clear()
cpa.send_keys("123")
time.sleep(1)
rs_percent = driver.find_element(By.NAME, "rs_percent")
rs_percent.clear()
rs_percent.send_keys("456")
time.sleep(1)
currency = driver.find_element(By.NAME, "currency").click()
time.sleep(1)
select_currency = driver.find_element(By.XPATH, "//select[@name='currency']/option[normalize-space()='Dollar']").click()
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save").click()
time.sleep(1)



success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
print(success_message)
time.sleep(1)


# Existing Brand Deal Plans

brand_deal_plans = driver.find_element(By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]").click()
time.sleep(2)
edit_brand = driver.find_element(By.NAME, "brand").click()
time.sleep(1)
change_brand = driver.find_element(By.XPATH, "//select[@name='brand']/option[@value='4']").click()
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save").click()
time.sleep(1)

success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
print(success_message)

driver.quit()