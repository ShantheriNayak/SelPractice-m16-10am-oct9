#Xpath by Attribute:
# Finding the location of the web element by usinmg the attributes.
# including ID,Name,Class etc. you can use as a attributes in xpath by attribute

#sample html code:
# <a href="https://www.amazon.in/" id="a1",name="n1",class="c1">Amazon </a>

#Syntax: //tagname[@attribute_name='attribute_value']
#// represents any child
# @- represents data is the attribute present as a child
#//a[@id="a1"]
#//a[@href='https://www.amazon.in/']

###############################################################
#Sample example 1.


#Sample example 1 program for amazon search button

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("oneplus nord mobile cover")
# time.sleep(2)
#
# driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
# time.sleep(2)
#
# driver.find_element("xpath","//button[@name='submit.addToCart']").click()
# time.sleep(2)

# driver.find_element('xpath','''//a[text()="Today's Deals"]''').click()
# time.sleep(2)
# driver.find_element('xpath','//button[text()="Coupons"]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Appliances"]').click()
# time.sleep(2)

#########################################################################
#Sample example 2 program for demo webworkshop

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath","//input[@id='gender-male']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='FirstName']").send_keys("Marvel")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='LastName']").send_keys("John Twain")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Email']").send_keys("ironman1@yahoo.com")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Password']").send_keys("mark@123")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='ConfirmPassword']").send_keys("mark@123")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='register-button']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@value='Continue']").click()
# time.sleep(2)
# driver.find_element("xpath","//a[@class='ico-logout']").click()
# time.sleep(2)
# driver.find_element("xpath","//a[@class='ico-login']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Email']").send_keys("ironman1@yahoo.com")
# time.sleep(2)
# driver.find_element("xpath","//input[@id='Password']").send_keys("mark@123")
# time.sleep(2)
# driver.find_element("xpath","//input[@value='Log in']").click()
# time.sleep(2)

###################################################################################################################
#sample program3:

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.saucedemo.com/") #lauch the application
# time.sleep(2)
# driver.find_element('xpath',"//input[@id='user-name']").send_keys('standard_user')
# #entering the username
# #id also happens to be the locator
# time.sleep(2)
#
# #entering the password
# driver.find_element('xpath',"//input[@id='password']").send_keys('secret_sauce')
# time.sleep(2)
#
# #submit the button
# driver.find_element('xpath',"//input[@id='login-button']").click()
# time.sleep(2)
# driver.find_element('xpath',"//input[@id='add-to-cart-sauce-labs-backpack']").click()
# time.sleep(2)
# driver.find_element('xpath',"//input[@id='add-to-cart-sauce-labs-bike-light']").click()
# time.sleep(2)
# driver.find_element("xpath","//a[@data-test='shopping-cart-link']").click()
# time.sleep(2)
# driver.find_element("xpath","//button[@id='remove-sauce-labs-backpack']").click()
# time.sleep(2)
# driver.find_element("xpath","//button[@id='remove-sauce-labs-bike-light']").click()
# time.sleep(2)
# driver.find_element("xpath","//button[@id='continue-shopping']").click()
# time.sleep(2)
#
# driver.find_element('xpath',"//button[@id='react-burger-menu-btn']").click()
# time.sleep(3)
# driver.find_element('xpath',"//a[@id='logout_sidebar_link']").click()


#################################################
#xpath with text(): it is used to identify an element with help of visible text on the page.
#below is the syntax:
#syntax://tagname[text()="text"]

#sample program
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath","//span[text()='TVs & Appliances']").click()
# time.sleep(2)
# driver.find_element("xpath","//span[text()='Become a Seller']").click()
# time.sleep(2)
# driver.find_element("xpath","//button[text()='Start Selling']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@name='mobileNumber']").send_keys("9045020789")
# time.sleep(2)
# driver.find_element("xpath","//input[@name='email']").send_keys("xyz@gmail.com")
# time.sleep(2)
# driver.find_element("xpath","//input[@name='gst']").send_keys("64ryejdfbkewd")
# time.sleep(2)
# driver.find_element("xpath","//span[text()='Register & Continue']").click()
# time.sleep(2)

####################################################################
#sample program amazon

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath","//a[text()='Bestsellers']").click()
# time.sleep(2)
# driver.find_element("xpath","//a[text()='Amazon Launchpad']").click()
# time.sleep(2)

##############################################################################
#Indexing with Xpath:

#group indexing--> (write the xpath)[index num 1,2,3...n]
#//input[@type="text"]---> matches 6 occurances(1 of 6) to match first occurance, we do group indexing
#ex 1.   (//input[@type="text"])[1]----> matches first Occurance
#ex 2.   (//input[@type="text"])[2]----> matches second occurance

# #Sample program 1
# #
# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','(//input[@type="text"])[1]').send_keys('maya')
# time.sleep(2)
# driver.find_element('xpath','(//input[@type="text"])[2]').send_keys('mahal')
# time.sleep(2)
# driver.find_element('xpath','(//input[@type="text"])[5]').send_keys('9075468291')
# time.sleep(2)

#########################################################################
#Sample program 2

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element('xpath','(//a[@class="desktop-main"])[1]').click()#men section gets clicked
time.sleep(2)
driver.find_element('xpath','(//a[@class="desktop-main"])[2]').click()#women section gets clicked
time.sleep(2)
driver.find_element('xpath','(//a[@class="desktop-main"])[3]').click()#kids section gets clicked
time.sleep(2)
driver.find_element('xpath','(//a[@class="desktop-main"])[4]').click()#men section gets clicked
time.sleep(2)
driver.find_element('xpath','(//a[@class="desktop-main"])[5]').click()#men section gets clicked
time.sleep(2)
driver.find_element('xpath','(//a[@class="desktop-main"])[6]').click()#men section gets clicked
time.sleep(2)

###########################################
#contains(): it helps to identify an element whose attribute value contains a sub texts or partial text.
#this function is normally used for attributes whose value changes on each page load.

#xpath using 'contains': to locate partial text of any tagname, we using xpath using contains
#Syntax://tagname[contains(text()," partialtext")]
#EXAMPLE: //span[contains(text(),"Gold with Lab Diamonds")]

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.giva.co/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element('xpath','//span[contains(text(),"Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath','//span[contains(text(),"GIVA Gift Card")]').click()
# time.sleep(2)
###############################################################################################################



























