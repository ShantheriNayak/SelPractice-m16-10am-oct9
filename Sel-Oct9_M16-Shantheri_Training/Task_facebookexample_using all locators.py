import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.facebook.com/")

driver.maximize_window()
time.sleep(2)

driver.find_element('link text','Create new account').click()
time.sleep(2)

driver.find_element('name','firstname').send_keys('Motu')
time.sleep(2)

driver.find_element('name','lastname').send_keys('patlu')
time.sleep(2)

driver.find_element('css selector',"input[value='2']").click()
time.sleep(2)

driver.find_element('name','reg_email__').send_keys('motupatlu@gmail.com')
time.sleep(2)

driver.find_element('id','password_step_input').send_keys('bne236rR')
time.sleep(2)

driver.find_element('link text','Sign Up').click()
time.sleep(2)

driver.close()