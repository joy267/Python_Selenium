import time

# Example can be used for practicing Infinite Scroll challenges in automated tests.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/infinite-scroll")
driver.maximize_window()

time.sleep(5)

while True:
           height = driver.execute_script("return document.body.scrollHeight")
           print(height)
           driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
           new_height = driver.execute_script("return document.body.scrollHeight")
           if height == new_height:
               break


driver.quit()

