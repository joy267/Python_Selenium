# At times it can take a while for third-party site resources to load (e.g., tracking code javascript,
# social networking widgets, etc.).
# This example has a rogue GET request that takes 10 seconds to complete.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/slow")
driver.maximize_window()
driver.implicitly_wait(10)

# time.sleep(10)


text = driver.find_element(By.XPATH, "//p[@class='alert alert-info']").text
print(text)



driver.quit()