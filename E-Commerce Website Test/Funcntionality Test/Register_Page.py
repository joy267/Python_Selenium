from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=s)


driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")


my_account = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
register = driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()

first_name = driver.find_element(By.ID, "input-firstname").send_keys("test first name")
last_name = driver.find_element(By.ID, "input-lastname").send_keys("test last name")
email = driver.find_element(By.ID, "input-email").send_keys("sfhfshfsg@gmail.com")
telephone = driver.find_element(By.ID, "input-telephone").send_keys("12345678")
password = driver.find_element(By.ID, "input-password").send_keys("1234")
confirm_password = driver.find_element(By.ID, "input-confirm").send_keys("1234")
privacy_policy = driver.find_element(By.NAME, "agree").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

expected_success_massage = "Your Account Has Been Created!"
actual_success_massage = driver.find_element(By.XPATH,"//div[@class='col-sm-9']/h1").text

if expected_success_massage == actual_success_massage:
    print("Your Account Has Been Created!")


driver.quit()


