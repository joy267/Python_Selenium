import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\\Projects\\automation\\Webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.implicitly_wait(10)

# Get URL
driver.get("https://testautomationpractice.blogspot.com/")

# # Name
# name = driver.find_element(By.ID, "name")
# name.send_keys("Tony Stark")
# time.sleep(1)
#
# # Email
# email = driver.find_element(By.ID, "email")
# email.send_keys("tonystark@gmail.com")
# time.sleep(1)
#
# # Phone
# phone = driver.find_element(By.ID, "phone")
# phone.send_keys("123456789")
# time.sleep(1)
#
# # Address
# address = driver.find_element(By.ID, "textarea")
# address.send_keys("New York, NY, USA")
# time.sleep(1)
#
# # Gender
# male_button = driver.find_element(By.ID, "male")
# female_button = driver.find_element(By.ID, "female")
# male_button.click()
# # female_button.click()
# time.sleep(1)
#
# # Days
# Monday = driver.find_element(By.ID, "monday")
# Monday.click()
# Friday = driver.find_element(By.ID, "friday")
# Friday.click()
# Wednesday = driver.find_element(By.ID, "wednesday")
# Wednesday.click()
# time.sleep(1)
#
# # Country
# country = driver.find_element(By.ID, "country")
# country.click()
# India = driver.find_element(By.XPATH, "//option[@value='india']")
# India.click()
# time.sleep(1)
#
# # Colors
# colors = driver.find_element(By.ID, "colors")
# colors.click()
# White = driver.find_element(By.XPATH, "//option[@value='white']")
# White.click()
# time.sleep(1)
#
# # Sorted List
# sorted_list = driver.find_element(By.ID, "animals")
# sorted_list.click()
# Rabbit = driver.find_element(By.XPATH, "//option[@value='rabbit']")
# Rabbit.click()
# time.sleep(1)

# Date Picker 1
# date_picker = driver.find_element(By.ID, "datepicker")
# date_picker.click()
# prev_button = driver.find_element(By.XPATH, "//a[@title='Prev']")
# next_button = driver.find_element(By.XPATH, "//a[@title='Next']")
#
# date = driver.find_element(By.XPATH, "//a[normalize-space()='25']")

# # next_button.click()
# # time.sleep(2)
# select = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(date))
# select.click()

# # Close Browser
# time.sleep(2)
# driver.quit()

# Date Picker 2
date_picker = driver.find_element(By.ID, "datepicker")
date_picker.click()
prev_button = driver.find_element(By.XPATH, "//a[@title='Prev']")
next_button = driver.find_element(By.XPATH, "//a[@title='Next']")

date = driver.find_element(By.XPATH, "//a[normalize-space()='25']")

# next_button.click()
# time.sleep(2)
select = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(date))
select.click()

# # Close Browser
time.sleep(2)
driver.quit()
