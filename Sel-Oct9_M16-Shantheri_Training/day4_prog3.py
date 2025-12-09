#name locator

#Name Locator: it is used to find the location of a partoicular webelement by using name attribute

# import time
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
#
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# driver.find_element('name','firstname').send_keys('Shantheri')
# time.sleep(2)
# driver.find_element('name','lastname').send_keys('Nayak')
# time.sleep(2)
# driver.find_element('name','reg_email__').send_keys('shnterinyk@gmail.com')
# time.sleep(2)



##########################################################
import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element('name', 'q').send_keys('Iphone')





















