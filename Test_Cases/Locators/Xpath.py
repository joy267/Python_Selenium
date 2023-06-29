from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

# Absulte Xpath and  Relative Xpath

driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[3]/div/div/div[2]/form/input[4]"). send_keys("T-Shirt")

driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

# Or And

driver.find_element(By.XPATH, "//input[@id='search_query_top']" or "//input[@id='search_query']").send_keys("T-Shirt")

driver.find_element(By.XPATH, "//button[@name='submit_search']" and "//button[@class='btn btn-default button-search']").click()

# Contains And Starts-With

driver.find_element(By.XPATH, "//input[contains(@class,'ac_input')]").send_keys("T-Shirt")

driver.find_element(By.XPATH, "//button[starts-with(@name,'submit_')]").click()

#Text

driver.find_element(By.XPATH, "//a[text()='Blog']").click()

