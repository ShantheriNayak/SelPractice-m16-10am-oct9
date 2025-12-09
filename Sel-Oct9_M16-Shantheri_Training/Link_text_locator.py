#5.link text: it is used to find the locatiojn of an elemnent by usuing text
# *it will work only for anchor tag(<a) .(it will work for span tag as well but not all the time.)
#* the text value is case sensitive


#sample HTML code:
# <a href "https://www.amazon.in" > AMAZON </a>
#<span> ........</span>


################################

#sample program example:

import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

#driver.find_element('tag name','input').send_keys("password")
#elementNotInteractableException error
driver.find_element('link text','Wishlist').click()
time.sleep(3)
driver.find_element('link text','Contact us').click()
time.sleep(2)
















































