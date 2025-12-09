import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
driver=webdriver.Chrome(opts)

driver.get("https://www.facebook.com/") #lauch the application
time.sleep(2)

driver.find_element('id','email').send_keys('hai Hello')
time.sleep(2)

driver.find_element('id','pass').send_keys('HELLOOOOO')
time.sleep(2)