
# Example can be used for practicing upload files scenario in automated tests.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Documents\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)



driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()

driver.find_element(By.NAME, "file").send_keys("C:\\Users\\Mrityunjoy Mandal\\Downloads\\M90p3249_400x400.png")

driver.find_element(By.ID, "fileSubmit").click()

file = driver.find_element(By.ID, "uploaded-files").text

print("File Uploaded!:", file)


driver.quit()
