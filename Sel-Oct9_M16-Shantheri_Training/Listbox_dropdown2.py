##Wap to enter date, month, year on the facebook signup page

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox()
# ac_obj=ActionChains(driver)
#
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# day = driver.find_element('xpath', '//select[@id="day"]')
# select_obj=Select(day)
#
# select_obj.select_by_value('22')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the Month
# time.sleep(1)
# #
# month=driver.find_element('xpath', '//select[@id="month"]')
# select_obj=Select(month)
#
# select_obj.select_by_value('10')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.TAB).perform()   ## The control will shift to the year
#
# year= driver.find_element('xpath', '//select[@id="year"]')
# select_obj=Select(year)
#
# select_obj.select_by_value('1990')
# time.sleep(2)