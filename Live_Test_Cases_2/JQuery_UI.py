# Examples based on JQuery UI can be used for practicing JQuery Widgets challenges in automated tests.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ChromeOptions = webdriver.ChromeOptions
ChromeOptions.add_experimental_option("prefs", {"download.default_directory" : "C:\\Users\Mrityunjoy Mandal\\PycharmProjects\\pythonProject\\Download"})


s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get("https://practice.expandtesting.com/jqueryui")
driver.implicitly_wait(10)

driver.find_element(By.PARTIAL_LINK_TEXT, "Menu").click()

jquary_manu = driver.find_element(By.ID, "ui-id-2")
actions = ActionChains(driver)
actions.move_to_element(jquary_manu).perform()
time.sleep(1)

jquary_manu = driver.find_element(By.ID, "ui-id-4")
actions = ActionChains(driver)
actions.move_to_element(jquary_manu).perform()
time.sleep(1)

driver.find_element(By.ID, "ui-id-6").click()
time.sleep(2)

jquary_manu = driver.find_element(By.ID, "ui-id-2")
actions = ActionChains(driver)
actions.move_to_element(jquary_manu).perform()
time.sleep(1)
driver.find_element(By.ID, "ui-id-5").click()
