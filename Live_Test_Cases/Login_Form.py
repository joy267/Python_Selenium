
# This example is a login form, a common use case for website authentication.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://practice.expandtesting.com/login")
driver.maximize_window()
driver.implicitly_wait(3)


# valid credentials

driver.find_element(By.ID, "username").send_keys("practice")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

#  Login Message Text
message = driver.find_element(By.ID, "flash").text
print(message)



# Invalid credentials

driver.find_element(By.ID, "username").send_keys("abcd")
driver.find_element(By.ID, "password").send_keys("abcd")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Login Message Text
message = driver.find_element(By.ID, "flash").text
print(message)


driver.quit()