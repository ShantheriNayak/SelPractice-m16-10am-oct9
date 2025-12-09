'''SYNCHRONIZATION :   Matching the speed of the webdriver to the speed of the web-application

There are 2 types
*   unconditional synchronization   :   No conditions are passed
            We achieve unconditional synchronization by passing time.sleep()
            Unnecessary wait is too much in unconditional synchronization.

*   conditional synchronization     :   Conditions are passed
        There are 2 types
        *   implicit_wait   :   Here the conditions are internally given.
                                SYNTAX  :   driver.implicitly_wait(n_seconds)
                                Whenever there is a delay, implicit_wait will automatically make the driver wait for n seconds.
                                It will wait until the element is available,
                                As soon as the element is available, it will start performing the operations right away.
                                There is no unnecessary wait.
                                One implicit_wait is sufficient for the whole program
                                It will be applied globally.

        *   explicit_wait   :   Here the conditions are passed externally
                                Here the wait happens  based on a condition

                                We should import WebDriverWait and expected_conditions

                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions
                                    WebDriverWait       --> class
                                    expected_conditions --> module

                                wait_obj = WebDriverWait(driver, timeouttime)

        WebDriverWait   :   It allows the driver to wait for a certain condition to check before we continue the operation.
                            Instead of waiting for a fixed amount of time, it waits until a condition is True or maximum time is reached.

        expected_conditions :   The conditions to be applied on the web-elements are already pre-defined and they are defined in expected_conditions.py
                            To make use of the pre-defined conditions we import expected_conditions

        until()         :   It is a method of WebDriverWait
                            It checks whether the given condition is satisfied or not
                            If the condition is True, it will continue the operations.
                            If the condition is False, it will always gives TimeOutException

'''

# import time
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\loading.html')
# driver.maximize_window()
# time.sleep(20)
#
# driver.find_element('xpath',"//input[@name='fname']").send_keys('harry')
# time.sleep(2)
# driver.find_element('xpath',"//input[@name='lname']").send_keys('potter')
# time.sleep(2)

# gives error as the page is loaded completely to perform the fname and lname operations
#to overcome this problem, we use implicitly wait time

#############################################################
'''implicit wait concept '''

# import time
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\loading.html')
# driver.maximize_window()
# driver.implicitly_wait(30)
#
# driver.find_element('xpath',"//input[@name='fname']").send_keys('harry')
#
# driver.find_element('xpath',"//input[@name='lname']").send_keys('potter')
# ######################################################################

'''explicit wait concept'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# wait_= WebDriverWait(driver, 30) # to make the website wait explicitly
#
# driver.get(r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\loading.html')
#
# wait_.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
# #to wait till the "FirstName" is visible for the program to run as expected
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Harry')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Potter')

##########################################################################
'''understanding the explicit wait with real time example'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# wait_= WebDriverWait(driver, 10) # to make the website wait explicitly
#
# driver.get('https://www.saucedemo.com/')
# # wait_.until(expected_conditions.visibility_of_element_located(('xpath','//div[contains(text()."FirstName")]')))
#
# driver.find_element('id','user-name').send_keys('standard_user')
# time.sleep(1)
# # driver.find_element('id','password').send_keys('secret_sauce') #pwd is correct
# # time.sleep(1)
#
# driver.find_element('id','password').send_keys('Secret_Sauce') #wrong pwd given
# time.sleep(1)
#
# driver.find_element('id','login-button').click() # Sucess login as usn and pwd is correct
#______________________________________________________________________________________________
'''#condition1:  took the url to check whether the login is sucess or not'''

# try:
#     wait_.until(expected_conditions.url_contains('inventory'))
#     print('successfull login')
# except:
#     print('unsuccessful login')
#____________________________________________________________________________________________
'''condition2: took some element on the home page and checking if the element is visible or not '''

# try:
#     wait_.until(expected_conditions.visibility_of_element_located(('xpath', '(//button[text()="Add to cart"])[1]')))
#     print('successfull login')
# except:
#     print('unsuccessful login')


##########################################_________________________________________
'''real time example for implicit wait concept'''

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.get(r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\progressbar.html')
#
# driver.find_element('xpath','//button[text()="Click Me"]').click()
# time.sleep(45)
# driver.find_element('xpath','//button[text()="Click Me"]').click()
#
# # the progress bar might not take 45 sec to make it 100%, but since we have given time.sleep(45), it will simply wait for
# #100% and the click again on "click me" .
# therefore its silly to wait irrespective when there is 1000 of lines of code
#__________________________________________________________________________________________________________
# '''implicit wait concept'''
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(50)
#
# driver.get(r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# driver.find_element('xpath', '//div[text()="100%"]')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

# ####################################

# '''explicit wait concept'''

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 50)
#
# driver.get(r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# wait_.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

#####################################################################################################
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# assert wait_.until(expected_conditions.alert_is_present())
# alert_obj = driver.switch_to.alert
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

#####################################################################################################
#
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_ = WebDriverWait(driver, 10)

driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
time.sleep(2)

wait_.until(EC.element_to_be_clickable(('xpath', '//button[text()="Start"]'))).click()

start = time.time()
wait_.until(EC.invisibility_of_element(('xpath', '//div[text()="Loading... "]')))
end = time.time()
print(end-start)

# # output:5.183934211730957






































































