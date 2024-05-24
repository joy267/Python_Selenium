
# Handling context menus and right-clicks on specific areas.



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get("https://practice.expandtesting.com/context-menu")
driver.implicitly_wait(10)


context_manu = driver.find_element(By.ID, "hot-spot")
actions = ActionChains(driver)
actions.context_click(context_manu).perform()


prompt_alert = driver.switch_to.alert
prompt_alert.accept()


driver.quit()


