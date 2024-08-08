from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time

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


# Add Brand Display Name To Websites

add_button = driver.find_element(By.XPATH, "//tr[@class='model-branddisplaynametowebsite']/td[1]").click()
time.sleep(1)

brand_display_name = "Foxy Bingo UK"

select_brand_display_name = driver.find_element(By.XPATH, "//span[@role='combobox']")
time.sleep(1)
select_brand_display_name.click()
time.sleep(1)
search_brand_display_name = driver.find_element(By.XPATH,"//input[@role='searchbox']")
time.sleep(1)
search_brand_display_name.send_keys(brand_display_name)
time.sleep(2)
search_brand_display_name.send_keys(Keys.ENTER)
time.sleep(1)

brand_name_for_display = driver.find_element(By.NAME, "brand_name_for_display")
brand_name_for_display.send_keys(brand_display_name)
time.sleep(1)

websites = driver.find_element(By.NAME, "website")
time.sleep(1)
websites.click()
time.sleep(1)

select_website = driver.find_element(By.XPATH,"//select[@name='website']")
select_website.send_keys(Keys.DOWN)
select_website.send_keys(Keys.DOWN)
select_website.send_keys(Keys.DOWN)
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

    brand_display_name_to_website = driver.find_element(By.XPATH,"//div[@class='breadcrumbs']/a[normalize-space()='Brand Display Name To Websites']")
    brand_display_name_to_website.click()
    time.sleep(1)

    find_brand_display_name = driver.find_element(By.XPATH,"//input[@id='searchbar']")
    time.sleep(1)

    find_brand_display_name.send_keys(brand_display_name)
    time.sleep(1)

    search_button = driver.find_element(By.XPATH,"//input[@value='Search']")
    search_button.click()
    time.sleep(1)

    existing_brand_display_name = driver.find_element(By.XPATH,"//th[@class='field-brand_display_name nowrap']").text
    time.sleep(1)

    try:
        existing_websites = driver.find_elements(By.XPATH, "//td[@class='field-website nowrap']")
        for element in existing_websites:
            print(existing_brand_display_name, element.text)


    except (NoSuchElementException):
        print("Can't find the brand display name to website")



# Change website for brand display name

edit_brand_display_name_to_website = driver.find_element(By.XPATH,"//table[@id='result_list']/tbody/tr[1]/th[1]/a")
edit_brand_display_name_to_website.click()
time.sleep(1)

edit_brand_for_display = "Foxy Bingo UK 1"
brand_name_for_display = driver.find_element(By.NAME, "brand_name_for_display")
time.sleep(1)
brand_name_for_display.clear()
time.sleep(1)
brand_name_for_display.send_keys(edit_brand_for_display)
time.sleep(1)

save_button = driver.find_element(By.NAME, "_save")
save_button.click()
time.sleep(1)

success_message = driver.find_element(By.XPATH, "//li[@class='success']").text
print(success_message)


try:
    print("Test Case is pass successfully")

except (NoSuchElementException):
    print("The element is not present in the webpage")

except (TimeoutException):
    print("Timeout Error")



driver.quit()