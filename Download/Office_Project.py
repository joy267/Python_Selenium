import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=s)

driver.get("https://staging-ppcsport.kinsta.cloud/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

# about_us = driver.find_element(By.LINK_TEXT, "About Us")
# driver.execute_script("arguments[0].scrollIntoView()", about_us)



Advertiser_Disclosure = driver.find_element(By.XPATH, "//p/a[text()='Advertiser Disclosure']")
actions = ActionChains(driver)
actions.move_to_element(Advertiser_Disclosure).perform()
time.sleep(2)


driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)


driver.find_element(By.ID, "menu-item-5307").click()
time.sleep(3)

A_Z_Sports = driver.find_element(By.ID, "menu-item-814")
actions.move_to_element(A_Z_Sports).perform()
time.sleep(2)
Tennis = driver.find_element(By.XPATH, "//li/a[text()='Tennis']").click()
time.sleep(3)


# For switching new window or tab
driver.switch_to.new_window('tab')
time.sleep(2)
driver.get("https://pagespeed.web.dev/")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@class='VfPpkd-fmcmS-wGMbrd ']").send_keys("https://staging-ppcsport.kinsta.cloud/")
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Analyze']").click()

