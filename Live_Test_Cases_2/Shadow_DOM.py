# Shadow DOM is a web standard that allows developers to encapsulate HTML markup, CSS styles,
# and JavaScript code within a custom HTML element, known as a Shadow DOM element.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/shadowdom")
driver.maximize_window()


button_text_1 = driver.find_element(By.ID, "my-btn").text
print(button_text_1)


shadow = driver.find_element(By.CSS_SELECTOR, "#shadow-host").shadow_root
button_text_2 = shadow.find_element(By.CSS_SELECTOR, "#my-btn").text
print(button_text_2)


driver.quit()