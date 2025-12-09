'''
Test case scenario steps:
1. goto url https://testautomationpractice.blogspot.com/,
2. click on Udemy Courses
3. goto  Playwright with Python , click on view course-->clciking opens a new window tab
4. scroll down to end of page
5. clicck on udemy bussiness---> opens new window
6. Scroll again to end of this page
6. click on "IN" image
7. New window Linkedin window page opens
8. enter email id and password

'''
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_ = WebDriverWait(driver, 10)

driver.get('https://testautomationpractice.blogspot.com/')
driver.implicitly_wait(20)
time.sleep(2)
handles = driver.window_handles
print(handles)# prints address of the window

#2. click on Udemy Courses
driver.find_element('xpath','//a[contains(text(),"Udemy Courses")] ').click()

##3. goto  Playwright with Python , click on view course-->clciking opens a new window tab

driver.find_element('xpath','(//a[text()="View Course"])[2]').click()


handles2=driver.window_handles
print(handles2)
driver.switch_to.window(handles2[1])
time.sleep(1)

## 4.scrolls down to end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scrolls down to end of the page
time.sleep(2)

##5. clicck on udemy bussiness---> opens new window
driver.find_element('class name','link.white-link.ud-text-sm').click()

handles3=driver.window_handles
print(handles3)
driver.switch_to.window(handles3[2])  ## control comes to 3rd window opened

## 6. Scroll again to end of this pag