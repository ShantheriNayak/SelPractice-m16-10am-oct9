# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/register")
# time.sleep(2)
#
# driver.find_element('id','gender-female').click()
# time.sleep(1)
# driver.find_element('id', 'FirstName').send_keys('Shantheri')
# time.sleep(1)
# driver.find_element('name','LastName').send_keys('Nayak')
# time.sleep(1)
#
# driver.find_element('name','Email').send_keys('name@gmail.com')
# time.sleep(2)
# driver.find_element('id','Password').send_keys('name@123')
# time.sleep(2)
# driver.find_element('name','ConfirmPassword').send_keys('name@123')
# time.sleep(2)
# driver.find_element('id','register-button').click()



#########################################################
#TagName locator:
# it is used to find the location of an element by using tagname.
#HTML code consists of 3 components:
#1.tag name
#2. attribute
#3.text

#<a href "www.amazon.in"
#a= tagname with find_elements is a preferred combination

####################
#sample program:\
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.amazon.in/")
time.sleep(2)

driver.find_element().send_keys('tag name','a').click()
time.sleep(1)
driver.find_element().send_keys('')
time.sleep(1)




































