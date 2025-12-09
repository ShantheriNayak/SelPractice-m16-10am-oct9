#class name locator: it is used to find or inspect the element in a webpage by using the attribute
#called class

# InvalidSelectorException or #NoSuchElementException:: if any space is present in the value name,
# this kind exception is thrown.
# to avoid this we use dot "text-box.single-line"


# import time
# #from time import sleep
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
# driver=webdriver.Chrome(opts)
# driver.get("")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("class name","c1").send_keys("Mark")


####################################################
import time
from time import sleep
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
driver=webdriver.Chrome(opts)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(2)
driver.find_element("class name","text-box single-line").send_keys("Amitabh bachan")
time.sleep(2)
#NoSuchElementException
# With replacing the space with dot:
driver.find_element("class name","text-box.single-line").send_keys("Selenium")
time.sleep(2)

























