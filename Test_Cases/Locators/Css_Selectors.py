from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

# Tag & Id :
driver.find_element(By.CSS_SELECTOR, "input#username"). send_keys('joy')
driver.find_element(By.CSS_SELECTOR, "#username"). send_keys('joy')

# Tag & Class :
driver.find_element(By.CSS_SELECTOR, "button.btn"). click()
driver.find_element(By.CSS_SELECTOR, ".btn"). click()

# Tag & Attribute :
driver.find_element(By.CSS_SELECTOR, "input[type=text]"). send_keys('joy')
driver.find_element(By.CSS_SELECTOR, "[type=text]"). send_keys('joy')

# Tag, Class & Attribute :
driver.find_element(By.CSS_SELECTOR, "tag_name.value_of_class[attribute=value]"). send_keys('joy')
