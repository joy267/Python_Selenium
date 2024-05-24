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
print(title)
time.sleep(1)


# Navigate to Login Page

account = driver.find_element(By.XPATH, "//span[@class='label'][normalize-space()='Account']")
account.click()
time.sleep(1)

login = driver.find_element(By.XPATH, "//a[normalize-space()='Log In']")
login.click()
time.sleep(1)


# Valid Credentials

username = driver.find_element(By.NAME, "login[username]")
username.send_keys("bawisit809@godsigma.com")
time.sleep(1)

password = driver.find_element(By.ID, "pass")
password.send_keys("bawisit809@godsigma.com")
time.sleep(1)

scroll_down = driver.find_element(By.TAG_NAME, "body")
scroll_down.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

submit = driver.find_element(By.XPATH, "//button[@title='Login']")
submit.click()
time.sleep(2)


# Confirmation Message

my_dashboard = driver.find_element(By.XPATH, "//div[@class='my-account']")
print("Login Successfully")







driver.quit()