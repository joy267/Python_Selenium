
# Example can be used for practicing the Forgot Password scenario in automated tests. An email will be sent to indicate password reset instructions.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://practice.expandtesting.com/forgot-password")
driver.maximize_window()
driver.implicitly_wait(3)


# Forgot Password with valid email address

# driver.find_element(By.ID, "email").send_keys("abcd@gmail.com")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#
# Confirmation_Message = driver.find_element(By.ID, "confirmation-alert").text
# print(Confirmation_Message)


# Forgot Password with invalid email address

driver.find_element(By.ID, "email").send_keys("abcd")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


Error_Message = driver.find_element(By.XPATH, "//div[@class='ms-1 invalid-feedback']").text
print(Error_Message)





driver.quit()



