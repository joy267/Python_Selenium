# 1. time.sleep(time in seconds)
# Advantage -
           # a.simple to use.
# Disadvantage -
           # a. Performance of the script is very poor.
           # b. If the element is not available within the line mentioned, still there is a chance to getting error.


# 2. Implicit Wait

       #Adv --
       # a. single statement.
       # b. Performance will not be reduced.

       #Dis --
       # a. If the element is not available the time mentioned, still there is a chance of getting error.



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://staging.etloptival.com/admin/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME, "username").send_keys("mrityunjoy@solivatech.com")

driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("killerboyz567")
driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Websites Attribute").click()
driver.find_element(By.CSS_SELECTOR, "button[title='Select Website']").click()
driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//input[@aria-label='Search']").send_keys("Punters")
driver.find_element(By.PARTIAL_LINK_TEXT, "punters - (SEO)").click()
driver.find_element(By.ID, "confirm-website-button").click()

driver.quit()


