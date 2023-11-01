# 1. Explicit Wait
from telnetlib import EC

#Adv --
       # a. More effectively works.

       #Dis --
       # a. Feel some difficulty to import this modules in multiple places.


from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,
    Exception])

driver.get("https://staging.etloptival.com/admin/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("mrityunjoy@solivatech.com")

driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("killerboyz567")
driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
attribute = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "vdss")))
attribute.click()

driver.find_element(By.CSS_SELECTOR, "button[title='Select Website']").click()
driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//input[@aria-label='Search']").send_keys("Punters")
driver.find_element(By.PARTIAL_LINK_TEXT, "punters - (SEO)").click()
driver.find_element(By.ID, "confirm-website-button").click()

driver.quit()


