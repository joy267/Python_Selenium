# 1. Verify the header section added to the website.
# 2. Verify header section is aligned.
# 3. Verify icons are aligned with the text if added to the header.
# 4. Verify icons added should be related to the link text.
# 5. Verify whether the link text should be readable or not.
# 6. Verify whether the logo of the website added on the header is aligned or not.
# 8. Verify the same header used on whole website pages.
# 9. Verify header is sticky on the whole page or fixed as per requirements and design.
# 10. Verify whether all links should be opening on the header or not.
# 11. Verify by clicking on the link on the header the correct page should be open.
# 12. Verify the home page should be open on clicking on the logo on all pages.
# 13. Verify on the mouse hover color change or not for the link added on the header menu.
# 14. Verify that selected header links should remain ACTIVE to inform the user about the clicked screen/page.
# 15. Verify whether the search bar is added to the header menu or not.
# 16. Verify header and body section don’t look the same. The header and body section must be distinguished.
# 17. Verify icon color should also change on mouse hover on the header if icons are added.
# 18. Verify dropdown options added on header shown on mouse hover or click.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = Service("C:\\Users\\Mrityunjoy Mandal\\OneDrive\\Desktop\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

