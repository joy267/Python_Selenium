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
print("Website Name :", title)
time.sleep(3)


# Header_Checklists

# 1. Verify the header section added on the website.

header = driver.find_element(By.ID, "header")

if header == True:

    print("Header is available on the web page.")

else:

    print("Header is not available on the web page.")



driver.quit()