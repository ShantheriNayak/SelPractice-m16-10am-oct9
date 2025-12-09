import time

'''
*The operations performed using mouse/keyboard , we call them as low-level operations.
*To perform low level operations in seleniums, we go for Actionchains

'''
'''
Mouse-Hovering operations:
WAP to perform the mouse hovering operation
'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# #opts.add_arugument(
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https:www.kushals.com')
# driver.maximize_window()
# time.sleep(4)
# #to perform mouse hover operation over earrings section
# accessories=driver.find_element('xpath','(//a[contains(text(),"Accessories")])[2]')
# ac_obj.move_to_element(accessories).perform()
# time.sleep(2)
#
# wedding_store=driver.find_element('xpath','(//a[contains(text(),"Wedding Store")])[2]')
# ac_obj.move_to_element(wedding_store).perform()


##################################################################


#WAP to perform hover over women ,home and genz element

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# #opts.add_arugument(
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(4)
#
# #hover over the women element
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# #hover over the home element
#
# Home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(Home).perform()
# time.sleep(2)
#
# #hover over the Genz element
#
# genz = driver.find_element('xpath', '(//a[text()="Genz"])[1]')
# ac_obj.move_to_element(genz).perform()
# time.sleep(2)



####################################################################################################
#wap to hover over the header elements

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# #opts.add_arugument(
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# time.sleep(4)
#solution1
# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
# for ele in navigation_elements[:-1]:
#     ac_obj.move_to_element(ele).perform()
#     time.sleep(2)

#solution2
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get('https://www.myntra.com/')
# driver.maximize_window()
#
# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
# for ele in range(0, len(navigation_elements)-1):
#     ac_obj.move_to_element(navigation_elements[ele]).perform()
#     time.sleep(2)
################################################################
'''     Double click mouse action'''

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# #opts.add_arugument(
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com')
# driver.maximize_window()
# time.sleep(4)
#
# copy_ele=driver.find_element('xpath','//button[text()="Copy Text"]')
# ac_obj.double_click(copy_ele).perform()


###################################################
'''             Right click mouse action'''


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com')
# driver.maximize_window()
# time.sleep(4)
#
# ele=driver.find_element('xpath','//h2[text()="Dynamic Button"]')

#to perform rightclick anywhere on the page


################################################################
'''Scroll down mouse action'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https:www.myntra.com/')
# driver.maximize_window()
# time.sleep(4)
#
# #scrolling down til a particular element:
# ref_ele=driver.find_element('xpath','//p[text()=" USEFUL LINKS "]')

# ac_obj.scroll_to_element(ref_ele).perform()
#
# #################################################################################
# Scrolling till end of the application using keyboard keys

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https:www.myntra.com/')
# driver.maximize_window()
# time.sleep(4)
# ######################################################################
# #send_keys is used to perform key action of the keys present on the keyboard
#
# ac_obj.send_keys(Keys.END).perform()
# #scroll to end of the page using keyboard key which are
# #predefined in Keys class
# time.sleep(2)
#
# '''driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#javaScript command to go to end of the page
# time.sleep(2)'''
#
#
# #to go back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()
# time.sleep(2)
#
# '''driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
# #Perform javaScript command to go to the home of the page
# time.sleep(2)'''
##########################################################################################

#to perform page up and page down
'''
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)

ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)

ac_obj.send_keys(Keys.PAGE_UP).perform()
time.sleep(2)
'''
###################################################################
'''scroll down by pixels'''
# driver.get('https:www.myntra.com/')
# driver.maximize_window()
# time.sleep(4)
# driver.execute("window.scrollby(0,500);")#will scroll down by 500 pixels
# time.sleep(3)
#
# driver.execute_script("window.scrollby(0,-500);") #will scroll up by 500 pixels


#############################################################
'''Drag and drop actions '''

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# ac_obj=ActionChains(driver)
#
# driver.get('https://testautomationpractice.blogspot.com')
# driver.maximize_window()
# time.sleep(4)
# #
# ele=driver.find_element('xpath','//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele=driver.find_element('xpath','//div[@id="draggable"]')
# droppable_ele=driver.find_element('xpath','//div[@id="droppable"]')
# ac_obj.drag_and_drop(draggable_ele,droppable_ele).perform()

##################################################

''' Slider'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
ac_obj=ActionChains(driver)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

slider = driver.find_element('xpath', '(//div[@id="slider-range"]/span)[1]')

## Move the slider RIGHT by 100 pixels
ac_obj.click_and_hold(slider).move_by_offset(100, 0).release().perform()
time.sleep(2)

## Move the slider LEFT by 100 pixels
ac_obj.click_and_hold(slider).move_by_offset(-100, 0).release().perform()



















































