import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)


s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)


driver.get("https://www.google.com/search?q=testing+tools")
driver.maximize_window()
driver.implicitly_wait(10)

# Selenium

driver.find_element(By.XPATH, "//div[@data-entityname='Selenium']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of Selenium']")
src = img.get_attribute('src')
print(src)
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
href = link.get_attribute('href')
print(href)

time.sleep(1)

# appium

driver.find_element(By.XPATH, "//div[@data-entityname='Appium']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "Appium").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of Appium']")
src = img.get_attribute('src')
print(src)
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
href = link.get_attribute('href')
print(href)
time.sleep(1)

# Katalon Studio

driver.find_element(By.XPATH, "//div[@data-entityname='Katalon Studio']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "Katalon Studio").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of Katalon Studio']")
src = img.get_attribute('src')
print(src)
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
href = link.get_attribute('href')
print(href)
time.sleep(1)


# Apache JMeter

driver.find_element(By.XPATH, "//div[@data-entityname='Apache JMeter']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "Apache JMeter").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of Apache JMeter']")
src = img.get_attribute('src')
print(src)
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
href = link.get_attribute('href')
print(href)
time.sleep(1)



# SoapUI

driver.find_element(By.XPATH, "//div[@data-entityname='SoapUI']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "SoapUI").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of SoapUI']")
src = img.get_attribute('src')
print(src)
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
href = link.get_attribute('href')
print(href)
time.sleep(1)



# Applitools

driver.find_element(By.XPATH, "//div[@data-entityname='BreadthFirstSRP']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "Applitools").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of Applitools']")
src = img.get_attribute('src')
print(src)
time.sleep(5)

# LambdaTest

driver.find_element(By.XPATH, "//div[@data-entityname='BreadthFirstSRP']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "LambdaTest").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of LambdaTest']")
src = img.get_attribute('src')
print(src)
time.sleep(5)

# TestComplete

driver.find_element(By.XPATH, "//div[@data-entityname='TestComplete']").click()
selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "TestComplete").text
print(selenium)
time.sleep(2)

img = driver.find_element(By.XPATH, "//img[@alt='image of TestComplete']")
src = img.get_attribute('src')
print(src)
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Wikipedia")
href = link.get_attribute('href')
print(href)
time.sleep(1)

# # BlazeMeter
#
# BlazeMeter = driver.find_element(By.PARTIAL_LINK_TEXT, "BlazeMeter")
# BlazeMeter.click()
# selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "BlazeMeter").text
# print(selenium)
# time.sleep(2)
#
# img = driver.find_element(By.XPATH, "//img[@alt='image of BlazeMeter']")
# src = img.get_attribute('src')
# print(src)
# time.sleep(3)



driver.quit()