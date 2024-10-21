from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

s = Service("C:\\Projects\\Selenium_Automation\\Chomedriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
wait = WebDriverWait(driver,10)


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


# Add Brand Display Name

add_button = driver.find_element(By.XPATH, "//tr[@class='model-branddisplaynames']/td[1]").click()
time.sleep(1)

brand_parent = driver.find_element(By.XPATH, "(//span[@role='combobox'])[1]")
brand_parent.click()
time.sleep(1)
search_box = driver.find_element(By.XPATH,"//input[@role='searchbox']")
search_box.send_keys("Foxy")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(1)

territory = driver.find_element(By.XPATH, "(//span[@role='combobox'])[2]")
territory.click()
time.sleep(2)
search_box = driver.find_element(By.XPATH,"//input[@role='searchbox']")
search_box.send_keys("UK")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(1)

product_type = driver.find_element(By.XPATH, "(//span[@role='combobox'])[3]")
product_type.click()
time.sleep(2)
search_box = driver.find_element(By.XPATH,"//input[@role='searchbox']")
search_box.send_keys("Sport")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(1)

brand_policy_plan = driver.find_element(By.NAME, "brand_policy_plan")
brand_policy_plan.click()
select_brand_policy_plan = driver.find_element(By.XPATH,"//select[@name='brand_policy_plan']")
time.sleep(1)
select_brand_policy_plan.send_keys(Keys.DOWN)
select_brand_policy_plan.send_keys(Keys.DOWN)
select_brand_policy_plan.send_keys(Keys.ENTER)
time.sleep(1)

logo_small = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_logo_small']"))) # Needs to addthe double first bracket ((By.XPATH,"//input[@id='id_logo_small']"))
logo_small.send_keys("C:\\Projects\\Selenium_Automation\\Python_Selenium\\pic.png")
time.sleep(1)

transparent_logo_small = wait.until(EC.element_to_be_clickable((By.NAME,"transparent_logo_small"))) # Needs to addthe double first bracket ((By.XPATH,"//input[@id='id_logo_small']"))
transparent_logo_small.send_keys("C:\\Projects\\Selenium_Automation\\Python_Selenium\\pic.png")
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)



try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)


except:
    error_message = driver.find_element(By.XPATH, "//ul[@class='errorlist nonfield']").text
    print(error_message)
    time.sleep(1)

    brand_parent = driver.find_element(By.XPATH, "(//span[@role='combobox'])[1]")
    brand_parent.click()
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    search_box.send_keys("Costa")
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)

    territory = driver.find_element(By.XPATH, "(//span[@role='combobox'])[2]")
    territory.click()
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    search_box.send_keys("MX")
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)

    product_type = driver.find_element(By.XPATH, "(//span[@role='combobox'])[3]")
    product_type.click()
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
    search_box.send_keys("Bingo")
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)

    brand_policy_plan = driver.find_element(By.NAME, "brand_policy_plan")
    brand_policy_plan.click()
    time.sleep(1)
    select_brand_policy_plan = driver.find_element(By.XPATH,"//select[@name='brand_policy_plan']")
    time.sleep(1)
    select_brand_policy_plan.send_keys(Keys.DOWN)
    select_brand_policy_plan.send_keys(Keys.DOWN)
    select_brand_policy_plan.send_keys(Keys.ENTER)
    time.sleep(1)

    logo_small = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_logo_small']")))  # Needs to addthe double first bracket ((By.XPATH,"//input[@id='id_logo_small']"))
    logo_small.send_keys("C:\\Projects\\Selenium_Automation\\Python_Selenium\\pic.png")
    time.sleep(1)

    transparent_logo_small = wait.until(EC.element_to_be_clickable((By.NAME,"transparent_logo_small")))  # Needs to addthe double first bracket ((By.XPATH,"//input[@id='id_logo_small']"))
    transparent_logo_small.send_keys("C:\\Projects\\Selenium_Automation\\Python_Selenium\\pic.png")
    time.sleep(1)

    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(1)

    try:
        success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
        print(success_message)

    except:
        print("The brand display is already exist")



# Change website for brand display name

edit_brand_display_name = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_brand_display_name.click()
time.sleep(1)

brand_parent = driver.find_element(By.XPATH, "(//span[@role='combobox'])[1]")
brand_parent.click()
time.sleep(1)
search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
search_box.send_keys("888")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(1)

territory = driver.find_element(By.XPATH, "(//span[@role='combobox'])[2]")
territory.click()
time.sleep(1)
search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
search_box.send_keys("US")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(1)

product_type = driver.find_element(By.XPATH, "(//span[@role='combobox'])[3]")
product_type.click()
time.sleep(1)
search_box = driver.find_element(By.XPATH, "//input[@role='searchbox']")
search_box.send_keys("Casino")
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(1)

brand_policy_plan = driver.find_element(By.NAME, "brand_policy_plan")
brand_policy_plan.click()
time.sleep(1)
select_brand_policy_plan = driver.find_element(By.XPATH,"//select[@name='brand_policy_plan']")
time.sleep(1)
select_brand_policy_plan.send_keys(Keys.DOWN)
select_brand_policy_plan.send_keys(Keys.DOWN)
select_brand_policy_plan.send_keys(Keys.ENTER)
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)


try:
    success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
    print(success_message)

except ():
    print("There has some problem for edit brand display name")

except NoSuchElementException:
    print("The element is not present in the webpage")

except TimeoutException:
    print("Timeout Error")





driver.quit()