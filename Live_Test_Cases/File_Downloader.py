import time

# Example can be used for practicing download files scenario in automated tests.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# For changing the download location of the file.

Chromeoption = webdriver.ChromeOptions()

Chromeoption.add_experimental_option("prefs", {"download.default_directory" : "C:\\Users\\Mrityunjoy Mandal\\PycharmProjects\\pythonProject\\Download"})



s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=Chromeoption)



driver.get("https://practice.expandtesting.com/download")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@data-testid='1705563334352_test.bin']").click()

time.sleep(3)


driver.quit()



