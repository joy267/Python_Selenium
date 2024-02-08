from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=s)

driver.maximize_window()
driver.get("https://pagespeed.web.dev/")
time.sleep(2)
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//button/span[text()='Ok, Got it.']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@class='VfPpkd-fmcmS-wGMbrd ']").send_keys("https://staging-ppcsport.kinsta.cloud/")
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='Analyze']").click()
time.sleep(20)
page_speed = driver.find_element(By.CLASS_NAME, "lh-exp-gauge__percentage").text
time.sleep(2)

print("Page Speed :",page_speed)
