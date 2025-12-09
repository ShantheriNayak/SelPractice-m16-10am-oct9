#CSS  locator -Cascading style sheets:

#CSS is used to decorate a webpage like color, fonts, size , backround etc.

#CSS selector locator: It is used to find the location of an element by using css expression
# Syntax:
# tagname[attribute name='attribute value']
# any attribute including id,name,class, etc

# where we have to write Css expression
#Step 1: inspect the element
#step 2: Press ctrl+f in ur keyboard "find my string"
#Step 3: type the css expression

#Verify the css expn to check if the expn is valid or not:
# 1.Element should get highlighted
# 2.code should get highlighted in yellow colour
# 3.(1of 1 ) matching we have to get

#Drawbacks of CSS selector:
#1. we cant able to make 1of 1 matching.
#2. we cant use this for text value

# #########

#SAmple example program 1:

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("css selector","input[id='Email']").send_keys("patlu@gmail.com")
# time.sleep(2)

#################################################################
# Sample program 2:

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.myntra.com/")
driver.maximize_window()
time.sleep(2)

#driver.find_element("css selector","input[class=





























