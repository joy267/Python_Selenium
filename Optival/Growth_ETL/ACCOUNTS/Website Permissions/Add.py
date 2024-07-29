import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
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


# Assign website to user

website_permission = driver.find_element(By.LINK_TEXT, "Website Permissions").click()
time.sleep(1)

add_website_permission = driver.find_element(By.XPATH, "//a[normalize-space()='Add website permission']").click()
time.sleep(1)

user_field = driver.find_element(By.XPATH, "//select[@name='user']")
time.sleep(1)

user_field.click()
time.sleep(1)

user_field.send_keys(Keys.DOWN)
time.sleep(1)

user_field.send_keys(Keys.DOWN,Keys.ENTER)
time.sleep(1)

website_field = driver.find_element(By.XPATH, "//select[@name='website_id']")
time.sleep(1)

website_field.click()

# Assign Website To User

assign_website = driver.find_element(By.XPATH, "//option[@value='15']")
time.sleep(1)
assign_website.click()
time.sleep(1)

save = driver.find_element(By.NAME, "_save")
save.click()
time.sleep(1)





try:
    already_assigned = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(already_assigned)
    driver.find_element(By.XPATH, "//div[@class='breadcrumbs']//a[normalize-space()='Website Permissions']").click()
    filter = driver.find_element(By.XPATH, "//div[@id='changelist-filter']").click()
    time.sleep(1)

    user_filter = driver.find_element(By.XPATH, "//a[@title='tester@etloptival.com']").click()
    time.sleep(1)

    user = driver.find_element(By.XPATH, "//th[@class='field-user nowrap']").text
    time.sleep(1)

    if user == "tester@etloptival.com":

        try:
            websites = driver.find_elements(By.XPATH, "//td[@class='field-website']")
            for element in websites:
                print(user, element.text)

        except (TimeoutException):
            print("Timeout Exception")

        except (NoSuchElementException):
            print("No Such Element Found")


except:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)





driver.quit()