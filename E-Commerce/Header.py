import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)
driver.maximize_window()
driver.implicitly_wait(10)


# Home_Page

home = driver.get("https://ecommerce.tealiumdemo.com/")
time.sleep(1)
title = driver.title
print("Website Name :", title)
time.sleep(3)


# Header_Checklists

# 1. Verify the header section added on the website.

header = driver.find_element(By.XPATH, "//div[@class='page-header-container']")

try:
    assert header.is_displayed()

    print("Header is present in this page.")

except:

    print("Header is not present in this page.")



# 2. Verify icons aligned with the text.

# Open a new window

driver.execute_script("window.open();")

# Switch to new window

driver.switch_to.window(driver.window_handles[1])

home = driver.get("https://ecommerce.tealiumdemo.com/")
time.sleep(1)

wait = WebDriverWait(driver, 10)
header = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='page-header-container']")))


# Locate the elements (adjust the locators based on your HTML structure)

try:
    # Example: Verify an icon is aligned with a text in a navigation link

    icon = header.find_element(By.XPATH, "//div[@class='account-cart-wrapper']/a/span[1]")
    text = header.find_element(By.XPATH, "//span[@class='label'][normalize-space()='Account']")  # Adjust locator

    # Retrieve CSS properties
    icon_css = icon.value_of_css_property('vertical-align')
    text_css = text.value_of_css_property('vertical-align')

    # Check if the alignment CSS properties are as expected
    assert icon_css == 'middle', f"Icon vertical alignment is {icon_css}, expected 'middle'"
    assert text_css == 'middle', f"Text vertical alignment is {text_css}, expected 'middle'"

    print("Icons are aligned with the text correctly.")
except Exception as e:
    print(f"Alignment verification failed: {e}")



# Verify the logo of the website added on the header

img_logo = driver.find_element(By.XPATH, "//img[@class='large']")
img = img_logo.get_attribute('scr')

response = requests.get(img)

if response.status_code == 200:
    with open('img.png', 'wb') as file:  # Specify the file name and extension
        file.write(response.content)
else:
    print(f"Failed to retrieve the image. Status code: {response.status_code}")




driver.quit()