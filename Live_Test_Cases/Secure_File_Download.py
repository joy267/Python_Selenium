import time

# This example shows a secure download page that can only be accessed with authentication and can be used for practicing automated tests


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Chromeoption = webdriver.ChromeOptions()

Chromeoption.add_experimental_option("prefs", {"download.default_directory" : "C:\\Users\\Mrityunjoy Mandal\\PycharmProjects\\pythonProject\\Download"})

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=Chromeoption)


driver.get("https://admin:admin@practice.expandtesting.com/download-secure")
driver.maximize_window()


driver.find_element(By.XPATH, "//a[@data-testid='1705587701977_dates.png']").click()

time.sleep(3)


driver.quit()

