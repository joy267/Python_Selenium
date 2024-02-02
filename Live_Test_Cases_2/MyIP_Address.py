
# The web page show you your public IP address.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/my-ip")
driver.maximize_window()


IPv4 = driver.find_element(By.ID, "ipv4").text
print(IPv4)

IPv6 = driver.find_element(By.ID, "ipv6").text
print(IPv6)

Country = driver.find_element(By.ID, "country").text
print(Country)

City = driver.find_element(By.ID, "city").text
print(City)

Timezone = driver.find_element(By.ID, "timezone").text
print(Timezone)


driver.quit()