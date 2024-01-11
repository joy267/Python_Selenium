# Application Commands
# --------------------------
# 1. get() - Opening the application URL.
# 2. title - To capture the title of the current webpage.
# 3. current_url - To capture the current URL of the webpage.
# 4. page_source - To Capture the source code of the webpage.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# get() ----
driver.get("https://demo.nopcommerce.com/")

# title ------
print(driver.title)

# current_url -------
print(driver.current_url)

# page_source -------
print(driver.page_source)

driver.quit()