from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Link_Text :
driver.find_element(By.LINK_TEXT, "Register").click()

#Partial_Text :
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()