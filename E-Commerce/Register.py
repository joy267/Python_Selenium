import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()
driver.implicitly_wait(10)


# Home_Page

home = driver.get("https://ecommerce.tealiumdemo.com/")
time.sleep(1)
title = driver.title
print("Website Name", title)
time.sleep(1)


# Navigate to Register Page

account = driver.find_element(By.XPATH, "//span[@class='label'][normalize-space()='Account']")
account.click()
time.sleep(1)

register = driver.find_element(By.PARTIAL_LINK_TEXT, "Register")
register.click()
time.sleep(1)


# Create account

first_name = driver.find_element(By.ID, "firstname")
first_name.send_keys("abc")
time.sleep(1)

last_name = driver.find_element(By.ID, "lastname")
last_name.send_keys("def")
time.sleep(1)

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("bcshbh3456@godsigma.com")
time.sleep(1)

scroll_down = driver.find_element(By.TAG_NAME, "body")
scroll_down.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

password = driver.find_element(By.NAME, "password")
password.send_keys("bcshbh3456@godsigma.com")
time.sleep(1)

confirm_password = driver.find_element(By.ID, "confirmation")
confirm_password.send_keys("bcshbh3456@godsigma.com")
time.sleep(1)

scroll_down = driver.find_element(By.TAG_NAME, "body")
scroll_down.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

remember_me = driver.find_element(By.XPATH, "//label[normalize-space()='Remember Me']")
remember_me.click()
time.sleep(1)

submit_button = driver.find_element(By.XPATH, "//button[@title='Register']")
submit_button.click()
time.sleep(1)


# Confirmation Message

accual_confirmation_text = driver.find_element(By.XPATH, "//span[normalize-space()='Thank you for registering with Tealium Ecommerce.']").text
expected_confirmation_text = 'Thank you for registering with Tealium Ecommerce.'

if expected_confirmation_text == accual_confirmation_text:
    print("User has successfully create the account")




driver.quit()