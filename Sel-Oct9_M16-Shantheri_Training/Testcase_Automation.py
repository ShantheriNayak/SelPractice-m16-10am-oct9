
# Test Case 1: Register User
#
#     1. Launch browser
#     2. Navigate to url 'http://automationexercise.com'
#     3. Verify that home page is visible successfully
#     4. Click on 'Signup / Login' button
#     5. Verify 'New User Signup!' is visible
#     6. Enter name and email address
#     7. Click 'Signup' button
#     8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
#     9. Fill details: Title, Name, Email, Password, Date of birth
#     10. Select checkbox 'Sign up for our newsletter!'
#     11. Select checkbox 'Receive special offers from our partners!'
#     12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
#     13. Click 'Create Account button'
#     14. Verify that 'ACCOUNT CREATED!' is visible
#     15. Click 'Continue' button
#     16. Verify that 'Logged in as username' is visible
#     17. Click 'Delete Account' button
#     18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("http://automationexercise.com")
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath',' //a[contains(text(),"Signup / Login")]').click()
time.sleep(2)
driver.find_element('xpath','//input[@name="name"]').send_keys("Nicole")
time.sleep(2)
driver.find_element('xpath','//input[@name="email"]').send_keys("nicole@yahoo.com")
time.sleep(2)
driver.find_element('xpath',"//button[text()='Signup']").click()
time.sleep(2)