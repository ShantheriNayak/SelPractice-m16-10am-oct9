#wap to launch the application, enter the username & password and to click on the login button
# 1.Id locator: it is used to find the location of a weblelement by using id
#ID attribute:
    #syntax: id="attribute value"
#types: 1.find_element(): it is used to identify the single element
   # 2. find_elements(): it is used to identify more than one web elements

#1.Find_element(): it is used to identify the single element. return type of this method is a webelement
#it will accept 2 arguements.
#Syntax: find_element("loactorname", "locator vale")
#possiblities: 1. it should have to match one element.
2.
#example

import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
driver=webdriver.Chrome(opts)

driver.get("https://www.saucedemo.com/") #lauch the application
time.sleep(2)
driver.find_element('id','user-name').send_keys('standard_user')
#entering the username
#id also happens to be the locator
time.sleep(2)

#entering the password
driver.find_element('id','password').send_keys('secret_sauce')
time.sleep(2)

#submit the button
driver.find_element('id','login-button').click()
time.sleep(3)

#to search the logout button and perform logout operation
driver.find_element('id','react-burger-menu-btn').click()
time.sleep(3)
driver.find_element('id','logout_sidebar_link').click()

############################



