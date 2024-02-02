
# The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://practice.expandtesting.com/challenging-dom")
driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element(By.XPATH, "//a[@class='btn btn-primary mb-2']").click()


for element in driver.find_element(By.TAG_NAME, "canvas"):
    print(element.text)



driver.quit()



