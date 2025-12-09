## file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html
import time

'''
If the tagname of the dropdown is "/select " is called standard listbox
dropdowns----> 1. single select, 
               2. multiselect dropdown
 
'''
## example 1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--disable-notifications')
#
# driver = webdriver.Chrome(opts)# Chrome browser
#
# ##driver=webdriver.Firefox() #firefox browser  ---dropdown closes for dob dropdown options for facebooksignup page
#
# driver.get('file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html')
# time.sleep(2)
#
# cars=driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj=Select(cars)

############################################################################
## select_by_index

## index number starts from 0

# select_obj.select_by_index(6)
# time.sleep(2)
# select_obj.select_by_index(2)
# time.sleep(2)
# #select_obj.select_by_index(0)
# time.sleep(2)
# select_obj.select_by_index(9)
# select_obj.select_by_index(50) ## if the index number is out of range,Could not locate element with index 50, it will give NosuchElementException
# time.sleep(2)
#
# select_obj.select_by_index() ## iF we dont give any index number, it will give Type Error
# time.sleep(2)
# ########################################################
# ## select by value
# select_obj.select_by_value('for')
# time.sleep(2)
# select_obj.select_by_value('hda')
# time.sleep(2)
# select_obj.select_by_value('toy')
# time.sleep(2)
#
# ## Select by Visible text
# select_obj.select_by_visible_text('Honda')
# time.sleep(2)
# select_obj.select_by_visible_text('Toyota')
# time.sleep(2)
# select_obj.select_by_visible_text('Audi')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')
# time.sleep(2)
#######################################################################
## multiselect dropdown

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html')
# time.sleep(2)
#
# mulitselect_listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj=Select(mulitselect_listbox)

## select by index
# select_obj.select_by_index(2)
# time.sleep(2)
# select_obj.select_by_index(4)
# time.sleep(2)
# select_obj.select_by_index(5)
# time.sleep(2)
# #
# ## deselect by Index
# select_obj.deselect_by_index(2)
# time.sleep(2)
# select_obj.deselect_by_index(4)
# time.sleep(2)
# select_obj.deselect_by_index(5)
# time.sleep(2)

# #select by value
# select_obj.select_by_value('aud')
# time.sleep(2)
# select_obj.select_by_value('bmw')
# time.sleep(2)
# select_obj.select_by_value('for')
# time.sleep(2)
#
# # deselct by value
# select_obj.deselect_by_value('for')
# time.sleep(2)
# select_obj.select_by_value('aud')
# time.sleep(2)

## Select by Visible text
# select_obj.select_by_visible_text('Honda')
# time.sleep(2)
# select_obj.select_by_visible_text('Toyota')
# time.sleep(2)
# select_obj.select_by_visible_text('Audi')
# time.sleep(2)
# select_obj.select_by_visible_text('Ford')
# time.sleep(2)

## Deselect the dropbox
# select_obj.deselect_by_visible_text('Audi')
# time.sleep(2)
# select_obj.deselect_by_visible_text('ford')
# time.sleep(2)
# select_obj.deselect_by_visible_text('Honda')
# time.sleep(2)

## to deselect all the selected values
# select_obj.select_by_visible_text('Toyota')
# time.sleep(2)
# select_obj.select_by_value('aud')
# time.sleep(2)
# select_obj.select_by_index(2)
# time.sleep(2)
# select_obj.deselect_all()
# time.sleep(2)

''' to get all selected items'''

# select_obj.select_by_visible_text('Toyota')
# time.sleep(2)
# select_obj.select_by_value('aud')
# time.sleep(2)
# select_obj.select_by_index(2)
# time.sleep(2)
# selected_items=select_obj.all_selected_options
#
# for item in selected_items:
#     print(item.text)
#
# '''Output:Audi
# BMW
# Toyota'''
# # ####################################
# #
# first_ele=select_obj.first_selected_option
# print(first_ele.text) ####Audi

###############################################################################

'''options  '''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--disable-notifications')
#
# driver = webdriver.Chrome(opts)# Chrome browser
#
# ##driver=webdriver.Firefox() #firefox browser  ---dropdown closes for dob dropdown options for facebooksignup page
#
# driver.get('file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html')
# time.sleep(2)
#
# cars=driver.find_element('xpath','//select[@id="standard_cars"]')
# select_obj=Select(cars)
#
# all_options=select_obj.options
# print(all_options)# address of all the elements
# for option in all_options:
#     print(option.text)# prints all the text present inside the listbox

'''Select car:
Audi
BMW
Ford
Honda
Jaguar
Land Rover
Mercedes
Mini
Nissan
Toyota
Volvo '''
#

#################################################################################

'''to select all the elements from dropdown'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument('--disable-notifications')

driver = webdriver.Chrome(opts)# Chrome browser

driver.get('file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html')
time.sleep(2)

cars=driver.find_element('xpath','//select[@id="standard_cars"]')
select_obj=Select(cars)

all_elements=select_obj.options  ## [wb1,wb2,wb3...]

##select_by_index
# for i in range(0,len(all_elements)):
#     select_obj.select_by_index(i)# '''each iteration one by one element is getting selected '''
#     print(all_elements[i].text)
#     time.sleep(2)
# select_obj.select_by_index(8)#   '''MINI is selected in the dropdown'''

## select by value
# for ele in all_elements:
#     val=ele.get_attribute('value')  ## gives value of  the value attribute
#     select_obj.select_by_value(val)
#     print(val)
#     time.sleep(2)
'''sel value given in html code
aud
bmw
for
hda
jgr
lr
merc
min
nin
toy
vol'''

##select by visible text
for ele in all_elements:
    text1=ele.text
    select_obj.select_by_visible_text(text1)
    time.sleep(2)









































































