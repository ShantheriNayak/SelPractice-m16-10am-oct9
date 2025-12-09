#wap on udemy page, click on signup, enter usn, pwd and click on continue.
# use all the locators used till now for the program


import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.udemy.com/")#launch the application
time.sleep(2)

driver.find_element('link text','Sign up').click() # link text locator: span tag
time.sleep(2)

driver.find_element('id','form-group--1').send_keys('MotuPatlu')#id locator, entering username
time.sleep(2)

driver.find_element('id','form-group--3').send_keys('MotuPatlu@yahoomail.com')#entering emailid
time.sleep(2)

driver.find_element('class name','ud-btn.ud-btn-large.ud-btn-brand.ud-btn-text-md.passwordless-auth-mx-code-generation-form--submit-button--2vOvZ').click()
time.sleep(2)