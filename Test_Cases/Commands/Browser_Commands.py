# Browser Commands
# --------------------------
# 1. close() - Close single browser window. (Where driver focused)
# 2. quit() - Close multiple browser windows. (This will kill the process)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(4)

driver.find_element(By.PARTIAL_LINK_TEXT, "nopCommerce").click()


# close() ---------
driver.close()

# quit() ---------
driver.close()