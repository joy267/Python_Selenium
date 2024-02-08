import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
mobile_emulation = {
   "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0, "mobile": True, "deviceScaleFactor": 50},
   "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",

}

options.add_argument("--window-size=414,900")
options.add_experimental_option("mobileEmulation", mobile_emulation)



s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=s)



driver.get(f"https://staging-ppcsport.kinsta.cloud/?keyword=seleniumtest{random.random()}")
driver.implicitly_wait(30)
time.sleep(3)


driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/p[1]/a[1]").click()
time.sleep(3)
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
time.sleep(2)


driver.find_element(By.ID,"popup_close").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME,"hamburger").click()
time.sleep(1)
driver.find_element(By.ID, "menu-item-5307").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME,"hamburger").click()
time.sleep(1)
driver.find_element(By.ID, "menu-item-814").click()
time.sleep(1)
driver.find_element(By.ID, "menu-item-816").click()
time.sleep(3)


# For switching new window or tab
driver.switch_to.new_window('tab')
time.sleep(2)
driver.get("https://pagespeed.web.dev/")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys(f"https://staging-ppcsport.kinsta.cloud/?keyword=seleniumtest{random.random()}")
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Analyze']").click()
time.sleep(50)

mobile_page_speed = driver.find_element(By.CLASS_NAME, "lh-exp-gauge__percentage").text
time.sleep(1)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
print("Mobile Page Speed:", mobile_page_speed)
time.sleep(1)


driver.quit()

