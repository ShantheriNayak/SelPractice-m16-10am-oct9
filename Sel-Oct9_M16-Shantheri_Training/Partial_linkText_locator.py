#Partial link text locator:
# it is used to find the location of an element by passing some portion of a text value
# *it will work only for anchor tag(it will also work for <span> tag but not all the time)
# * in this also the text value is case sensitive

#note:
# * in  link text, you have to pass the text value completely but in partial link text you have to pass the
#text value some portion
# * both link text and partial text are case sensitive.
#########################################################

#Sample program example:


# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.selenium.dev/downloads/")
# driver.maximize_window()
# time.sleep(2)
#
# #driver.find_element("link text","Python 3.14.0").click() # NoSuchElementException
#
# # driver.find_element('partial link text','languages').click()
# # time.sleep(2)
# driver.find_element("partial link text","Python").click()
# time.sleep(2)

#################################################
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
time.sleep(2)
driver.find_element("partial link text","Data").click()
time.sleep(2)
driver.find_element("partial link text","Mathematics").click()
time.sleep(2)





























































