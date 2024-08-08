import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

s = Service("C:\\Projects\\Selenium_Automation\\Chomedriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)


# Growth_ETL URL -

driver.maximize_window()
driver.get("https://staging.etloptival.com/admin/")


# Login Credencials

username = driver.find_element(By.NAME, "username")
username.send_keys("mrityunjoy@solivatech.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("killerboyz567")

login_button = driver.find_element(By.XPATH, "//input[@value='Log in']")
login_button.click()

time.sleep(2)


# Edit Websites Attribute

website_attribute = driver.find_element(By.XPATH, "//a[normalize-space()='Websites Attribute']").click()
time.sleep(1)
select_website = driver.find_element(By.XPATH, "//div[contains(text(),'Select Website')]").click()
time.sleep(1)
search_website = driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//input[@type='search']")
time.sleep(1)
search_website.send_keys("top10casinositesuk",Keys.ENTER)
time.sleep(1)
confirm_button = driver.find_element(By.ID, "confirm-website-button").click()
time.sleep(1)

keyword_id = driver.find_element(By.ID, "keyword-details-id").send_keys("2")
time.sleep(1)
save = driver.find_element(By.ID, "wa-save-button").send_keys("2")
time.sleep(1)

try:
    print("Website module is working perfectly")

except(NoSuchElementException):
    print("Element is not present in the webpage")
except(TimeoutException):
    print("Timeout Error")


driver.quit()