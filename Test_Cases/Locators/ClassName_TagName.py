from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# # By CLASS_NAME :
radio_buttons = driver.find_elements(By.CLASS_NAME, 'answer')
print(len(radio_buttons))

# By TAG_NAME :
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

