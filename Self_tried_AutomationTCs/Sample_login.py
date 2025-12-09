'''
Test case 1: Positive LogIn test

    Open page
    Type username student into Username field
    Type password Password123 into Password field
    Push Submit button
    Verify new page URL contains practicetestautomation.com/logged-in-successfully/
    Verify new page contains expected text ('Congratulations' or 'successfully logged in')
    Verify button Log out is displayed on the new page '''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts=webdriver.ChromeOptions()
#
#
# opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
# driver=webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
#
# driver.get("https://practicetestautomation.com/practice-test-login/") #lauch the application
# time.sleep(2)
# driver.maximize_window()

# driver.find_element('id','username').send_keys('student')
# time.sleep(2)
# driver.find_element('id','password').send_keys('Password123')
# time.sleep(2)
#
# driver.find_element('id','submit').click()
# time.sleep(2)

#Syncronisation topic
# ## condition1. Took the url to check whether the login is successfull or not

# try:
#     wait_.until(expected_conditions.url_contains('logged-in-successfully'))
#     print("Succesfull login")
# except:
#     print("Unsuccesfull login")

# ## condition2. Took some element on the homepage and checking if that element is visible or not
# try:
#     wait_.until(expected_conditions.visibility_of_element_located(('xpath', '//a[text()="Log out"]')))
#     print("Log-out button is present")
# except:
#     print("Log-out button is not present")
#
# driver.find_element('xpath','//a[text()="Log out"]').click()
# time.sleep(2)

#driver.close()


#######################################################################################################
'''Test case 2: Negative username test

    Open page
    Type username incorrectUser into Username field
    Type password Password123 into Password field
    Push Submit button
    Verify error message is displayed
    Verify error message text is Your username is invalid!'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts=webdriver.ChromeOptions()
#
#
# opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
# driver=webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get("https://practicetestautomation.com/practice-test-login/") #lauch the application
# time.sleep(2)
# driver.maximize_window()
# driver.find_element('id','username').send_keys('Student1')
# time.sleep(2)
# driver.find_element('id','password').send_keys('Password123')
# time.sleep(2)
#
# driver.find_element('id','submit').click()
# time.sleep(2)
#
# ##condition2. Took some element on the homepage and checking if that element is visible or not
# try:
#     wait_.until(expected_conditions.visibility_of_element_located(('id', 'error')))
#     print("Your username is invalid!")
# except:
#     print(" no such messages displayed!")

###############################################################################################
''' Test case 3: Negative password test

    Open page
    Type username student into Username field
    Type password incorrectPassword into Password field
    Push Submit button
    Verify error message is displayed
    Verify error message text is Your password is invalid!'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts=webdriver.ChromeOptions()


opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
driver=webdriver.Chrome(opts)
wait_ = WebDriverWait(driver, 10)


driver.get("https://practicetestautomation.com/practice-test-login/") #lauch the application
time.sleep(2)
driver.maximize_window()

driver.find_element('id','username').send_keys('student')
time.sleep(2)
driver.find_element('id','password').send_keys('Password12345')
time.sleep(2)

driver.find_element('id','submit').click()
time.sleep(2)

##condition2. Took some element on the homepage and checking if that element is visible or not
try:
    wait_.until(expected_conditions.visibility_of_element_located(('id', 'error')))
    print("Your password is invalid!")
except:
    print(" no such messages displayed!")
