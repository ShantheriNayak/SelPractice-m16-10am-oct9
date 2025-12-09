'''
dependent and independent xpath
* identify the dependent-independent elements
*write the xpath of independent element
* traverse back(/..) until  we get the common match for dependent-independent element

xpath of independent element, traverse to immediate parent(/..), then write the dependent element's xpath
//td[text()="Ruby"]/..//input[@name="download"]
'''
##########################################
#Eg1. wap to click on the checkbox of Ruby in demo.html

#file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'file:///C:/Users/Prashanth%20Nayak/Desktop/py%20progs/Python-Selenium%20daily%20notes/demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()

############################################################################

#sample program 2

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.tradingview.com/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath','//span[text()="Search"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','//input[@name="query"]').send_keys("HAL")
# time.sleep(2)
#
# driver.find_element('xpath','(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)

#

############################################
# Handling Dynamically elements or  changing values
# #example:

#wap to print the sellprice and buyprice of Gold in https://www.iforex.in/tools/live-rates

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.iforex.in/tools/live-rates")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element('xpath', '(//div[@id="ai-chat-bubble-close"])[2]').click()
# time.sleep(3)
#
# gold_sellPrice=driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# gold_buyPrice=driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[3]')
#
# #print(gold_sellPrice)# address of the web element
# #print(gold_buyPrice)
#
# print(f"the sell price of the gold is: {gold_sellPrice.text}")
# print(f"the buy price of gold is: {gold_buyPrice.text}")
#driver.quit()

####################################################################################
#Calender handling:
# WAP to select particular date in make my trip

# import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# time.sleep(2)
# #close the pop-up ,i donot want to enter the phone number
# driver.find_element('xpath','//span[@class="commonModal__close"]').click()
# time.sleep(2)
# #depature
#
# driver.find_element('xpath','//span[text()="Departure"]').click()
# time.sleep(2)
# def select_date(month,date):
#
#     while True:
#         try:
#             driver.find_element('xpath',f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#         except:
# #click on the forward arrow
#             driver.find_element('xpath','//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click()
#
# select_date('September 2026',18)
# select_date('August 2026',18)
'''
nov-dec-->except-->next month
dec-jan-->except-->next month
jan-feb--except-->next month
feb-mar--except-->next month
mar-apr--except-->next month
apr-may--except-->next month
may-jun--except-->next month
jun-jul--except-->next month
jul-aug--try-clicks on aug 15--> break

'''
##########################################################################
'''
Go to https://www.irctc.co.in/nget/train-search, select the travel date
Go to https://www.redbus.in/, select the date of journey
Go to https://www.booking.com/, select the check-in date
'''










































































































