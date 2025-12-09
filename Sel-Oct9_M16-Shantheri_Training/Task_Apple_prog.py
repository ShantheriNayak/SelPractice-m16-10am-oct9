#WAP to open the apple india website and click on MAC, iPad and search button

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.apple.com/in/")#launch the application
time.sleep(3)

driver.find_element('link text','Mac').click()
time.sleep(2)

driver.find_element('link text','iPad').click()
time.sleep(2)

driver.find_element('id','globalnav-menubutton-link-search').click()
time.sleep(2)