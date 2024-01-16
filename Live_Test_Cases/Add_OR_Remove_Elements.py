
# Dynamically Adding and Removing Web Elements.



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://practice.expandtesting.com/add-remove-elements")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()

driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']").click()
driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']").click()
driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']").click()

driver.quit()



