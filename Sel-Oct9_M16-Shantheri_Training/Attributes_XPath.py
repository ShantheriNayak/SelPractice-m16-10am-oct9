import time

'''
.text: it is the property of the webelement.
    * it will give the text of the element
    *SYNTAX  :   web_element.text


get_attribute: it is used to fetch or retrive the value of any attribute of a web-element
syntax:web_element.get_attribute('attribute_name')

'''

###########################################################################

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# men=driver.find_element('xpath','//a[@data-group="men"]')
# print(men.text) #MEN
#
# women=driver.find_element('xpath','//a[@data-group="women"]')
# print(women.text) #WOMEN

##############################################
#wap to fetch the value of the webelement/tagname

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# women=driver.find_element('xpath','(//a[text()="Women"])[1]')
# print(women.get_attribute('href')) #https://www.myntra.com/shop/women
# print(women.get_attribute('class')) #desktop-main
# print(women.get_attribute('style')) #border-bottom-color: rgb(251, 86, 193);
# print(women.get_attribute('data-index')) #1
#
# print(women.get_attribute('hreffffff'))# None
# ## becoz there value is not present in the html code, so returns null
#
# html_code=women.get_attribute('outerHTML')
# print(html_code) #gives the complete html code of women section
#
# html_code=women.get_attribute('innerHTML')
# print(html_code) #Women
# # gives data present between open and close tag

####################################################################
'''
get_dom_attribute: it retrievs the attribute full value exactly as it is visible in DOM
    syntax: web_element.get_dom_attribute("attr_name")

'''

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# women=driver.find_element('xpath','(//a[text()="Women"])[1]')
# print(women.get_attribute('href')) #https://www.myntra.com/shop/women
# print(women.get_dom_attribute('href')) #/shop/women

##########################################################

'''
is_enabled(): it is used to check whether a web-element is enabled or disabled on the webpage

if the element is enabled-->true
if the element is disabled-->false
syntax:web_element.is_enabled()# output will always be in boolean format
'''

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.instagram.com/accounts/emailsignup")
# time.sleep(2)
#
# ele=driver.find_element('xpath','button[text()="Sign up"]')
# print(ele.is_enabled()) #false
#
# ele1=driver.find_element('xpath','button[text()="Log in with Facebook"]')
# print(ele1.is_enabled()) #true


###########################################################################

'''
assert: it is a keyword in python. it is used to validate the expected output with actual output
assert will take a condition
syntax: assert condn
if true: the test case  passes and executeion will continue as expected
if false: the test case  fails and gives Assertion error

'''
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.instagram.com/accounts/emailsignup")
# time.sleep(2)
#
# ele1=driver.find_element('xpath','button[text()="Log in with Facebook"]')
# assert ele1.is_enabled() # true, will continue with execution
# print("login button is enabled")
#
# ele=driver.find_element('xpath','button[text()="Sign up"]')
# assert ele.is_enabled() #false gives assertion error

#############################################
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.myntra.com/")
# time.sleep(2)
#
# women=driver.find_element('xpath','(//a[text()="Women"])[1]')
# assert women.get_attribute('href')=='Shantheri', "the attribute value is not Shantheri"

#output:AssertionError: the attribute value is not Shantheri

#########################################################
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.zepto.com/")
# time.sleep(2)
#
# ele1=driver.find_element('xpath','//span[text()="login"]')
# ele1.click()
# assert ele1.is_enabled() # true, will continue with execution
# print("login button is enabled")
# time.sleep(2)
#
# ele2=driver.find_element('xpath','//div[text()="Continue"]')
# assert ele2.is_enabled() # true, will continue with execution
# print("Continue button is  not enabled")

#output:
#login button is enabled
#Continue button is  not enabled

#############################################################################

'''
tag_name    :   It is a property. It is used to get the tagname of a web_element.
                Eg  :   a, div, span, p, etc,...
                
aria-role   :   It is a property.
                This helps screen readers to understand what UI element it is.
                Eg  :   button, textbox, link etc,..

value of css property
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
print(women.tag_name)
print(women.aria_role)    ## link

ele = driver.find_element('xpath', '//h4[text()="LUXE GRAND REDUCTION DEALS"]')
print(ele.tag_name)
print(ele.aria_role)              ## heading

search_bar = driver.find_element('xpath', '//input[@class="desktop-searchBar"]')
print(search_bar.tag_name)
print(search_bar.aria_role)     ## textbox

# '''
# To Take the screenshot of a web-element, we have screenshot() attribute
#     #SYNTAX  :   web_element.screenshot("ss_name.png")
#                 By default the screenshot will be saved in the same location as our python file
#
# To store the screenshot in different location
#     #SYNTAX  :   web_element.screenshot("location\ss_name.png")
#
# '''

women.screenshot(r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files\women.png')
ele.screenshot(r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files\heading.png')
search_bar.screenshot(r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files\searchbar.png')

































































