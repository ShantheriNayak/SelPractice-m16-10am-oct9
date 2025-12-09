#XPath Locator:
#Xpath is used to find the location of a web element in HTML tree structure or in DOM(Document object Model)

#Xpath classified into 2 types:
# 1.Absolute Xpath
# 2.Relative Xpath

# 1.Absolute Xpath:
#* it will traverse from parent to its own child.
#* it is denoted as (/)

#Drawbacks of Absolute Xpath:
#1.Absolute Xpath is very lengthy compared to relative xpath
#2. always it will traverse from parent to its own child

#2. Relative Xpath:
# *it will traverse from parent to any of the child
#* it is denoted as (//)

#####################################################################
# 1.Absolute Xpath:

#Sample Program 1 example for Absolute Xpath:

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/XpathExample.html")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div[2]/input[2]').send_keys('Virat')
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div[1]/input[2]').send_keys('Anushka')
# time.sleep(2)

########################################################################
#SAmple example program 2:

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
# time.sleep(2)

###############################################################
#SAmple example program 3:

'''import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath","html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("mark@gmail.com")
time.sleep(2)'''
# driver.find_element("xpath","html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input").send_keys("mark@123")
# time.sleep(2)

###############################################################
# Sample example 4 program for amazon search button

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(2)
# # driver.find_element("id","twotabsearchtextbox").send_keys("oneplus nord")
# # time.sleep(2)
# driver.find_element("xpath","html/body/div/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("oneplus nord mobile cover")
# time.sleep(2)
#################################################################################################

#2 Relative Xpath:

#Sample example 1 program :
import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/XpathExample.html")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath','//div[1]/input[1]').send_keys('Virat')
time.sleep(2)
driver.find_element('xpath','//div[2]/input[2]').send_keys('Kohli')
time.sleep(2)

###################################################






























