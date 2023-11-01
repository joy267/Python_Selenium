# Difference  Between Find Element and Find Elements.
#-----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://demo.nopcommerce.com/")

############    find_element() - Returns single webelement.

# 1. Locator matching with single webelement.
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

# 2. Locator matching with multiple webelement.
# elements = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(elements.text)  # Print first link from footer "Sitemap"

# 3. If the element not availabel in webpage. (NoSuchElementException)
elements = driver.find_element(By.LINK_TEXT, "Log")
elements.click()