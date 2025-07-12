
# Example can be used for practicing Broken Images challenges in automated test.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\\Selenium_Python\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("https://www.google.com/search?q=testing+tools")
driver.maximize_window()


image_list = driver.find_elements(By.ID, "dimg_Kk06ZrCGFKjCjuMP16-RkAs_45")
scr = image_list.__getattribute__()
print(scr)




driver.quit()