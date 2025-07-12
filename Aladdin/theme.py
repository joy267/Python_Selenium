from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://aladdin-ui-stage.etloptival.com/")
driver.maximize_window()
driver.implicitly_wait(10)


# Login

user_email = driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']")
password = driver.find_element(By.XPATH, "//input[@type='password']")
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='LOGIN NOW']")

user_email.send_keys("tester@etloptival.com")
password.send_keys("soliva@123")
login_button.click()


# Create a new theme

assets = driver.find_element(By.XPATH, "//div[@aria-label='Assets']")
design = driver.find_element(By.XPATH, "//span[normalize-space()='Design']")
theme = driver.find_element(By.XPATH, "//span[normalize-space()='Themes']")
select_site = driver.find_element(By.XPATH, "//input[@id=':rl:']")

assets.click()
design.click()
theme.click()
select_site.click()

