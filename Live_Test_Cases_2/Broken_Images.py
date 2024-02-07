
# Example can be used for practicing Broken Images challenges in automated test.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://practice.expandtesting.com/broken-images")
driver.maximize_window()


image_list = driver.find_elements(By.TAG_NAME, "img")




driver.quit()