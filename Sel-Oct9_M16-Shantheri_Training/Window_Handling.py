import time
#
'''
a new pop-up window or tab can open upon clicking a link or a button.
the webdriver by default has control over the main page, in order to 
acess the elements on the new window, the webdriver control has to be 
swtiched from main page to the new pop-up window or tab.

1.driver.window_handles or driver.current_window_handles: to obtain the handle id of current or parent window

2.driver.switch_to.window(<window handle id> handles2[0]): to switch the webdriver
control to opened window whose handle id is passed as a parameter to the method


'''

# #wap to check
#
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# handles = driver.window_handles
# print(handles)# prints address of the window ['B697D38491B94A83FB9EC1BC7F61E942']
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scrolls down to end of the page
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(2)
#
# handles2=driver.window_handles
# print(handles2)   #[parent_handle address,child_handle address]
#                 ## handles2[0]=parent_handle address
#                 ## handle2[1]=child_handle address
#      ##  '''#[parent_handle address,child_handle address]
#     ## ['B697D38491B94A83FB9EC1BC7F61E942', 'A7D95A5ADC672DE184D6A1C9C262A00D']'''
# driver.switch_to.window(handles2[1])
# time.sleep(2)
#
# driver.find_element('xpath','//input[@class="header__search"]').send_keys('Google Pixel 9')
# time.sleep(2)
#
# driver.switch_to.window(handles2[0]) ##switch back to parent window
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Twitter"]').click()
# time.sleep(2)
#
# handles3=driver.window_handles
# print(handles3)
# Output: memoryaddress of parent window, google+ CW1,twitter window-CW2
#['B697D38491B94A83FB9EC1BC7F61E942', 'A7D95A5ADC672DE184D6A1C9C262A00D', '2F1ABE776B3587FB950F4605A1E379FB']


#[parent_handle address,child_handle1 address,child_handle2 address]
                ## handles3[0]=parent_handle address
                ## handle3[1]=child_handle1 address
               ## handles3[2]=child_handle2 address

#  ###########################################################################
# #optimizing the above code

# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.implicitly_wait(20)
# time.sleep(2)
# handles = driver.window_handles
# print(handles)# prints address of the window   ['594908C3D463C0AE05CD0257E4296893']
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scrolls down to end of the page
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Google+"]').click()
# time.sleep(2)

# # driver.window_handles=[parent, child]
# # checks googleblog in parent window-false as its not present, comes out of if condn, goes into for loop, now the controls
# #goes to child window, checks 'googleblog' in child window. true as it is present, checks and performs.

# def handling_windows():
#     return driver.window_handles
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'googleblog'in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys('Google Pixel 9')
#         time.sleep(2)
#         driver.switch_to.window(handling_windows()[0]) # coming back to parent window
#         time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Twitter"]').click()
# time.sleep(2)
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'nopCommerce'in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()
#         time.sleep(2)
################################################################################################################
#Flipkart example:


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_ = WebDriverWait(driver, 10)

driver.get('https://www.flipkart.com/')
driver.implicitly_wait(20)
time.sleep(2)

driver.find_element('xpath','//input[@title="Search For Products, Brands and More"]').send_keys("phones under 30000")
time.sleep(2)

driver.find_element('xpath','//button[@type="submit"]').click()
time.sleep(2)

driver.find_element('xpath','//div[@class="KzDlHZ"]').click()
time.sleep(2)

def handle_windows():
    return driver.window_handles

#handle_windows() reurns a list [parent, child1, child2....]

for handle in handle_windows():
    driver.switch_to.window(handle)
    if "samsung-galaxy-f36-5g-red-128-gb" in driver.current_url:
        driver.find_element('xpath','//button[text()="Add to cart"]').click()
        time.sleep(2)

driver.find_element('xpath','//a[text()="Help Center"]').click()
time.sleep(2)

for handle in handle_windows():
    driver.switch_to.window(handle)
    if 'helpcentre' in driver.current_url:
        driver.find_element('xpath','//a[text()="Know more"]').click()
        time.sleep(2)

































































