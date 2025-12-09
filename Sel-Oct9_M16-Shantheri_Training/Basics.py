import time
from selenium import webdriver
#initilizing Chrome browser
c_driver=webdriver.Chrome()
time.sleep(20)

#to prevent the browser from closing automatically

#from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
c_driver=webdriver.Chrome(opts)    #if we dont pass the object "opts" here, then the browser closes automatically

########################################
#initilizing Firefox browser
f_driver=webdriver.Firefox()
#since for firefox browser doesnt close automatically, we need not consider FirefoxOptions and add_experimental_option

####################################
#initilizing Edge browser

e_driver= webdriver.Edge()
time.sleep(10)

opts=webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)
e_driver=webdriver.Edge(opts)




















































































