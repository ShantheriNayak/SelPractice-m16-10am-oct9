# Tag Name Locator:
# Sample Html code <a href="https://www.google.com"> Google</a>
from tkinter.font import names
# <a -anchor tag --->is tag_name, Href is attribute

#A HTML code consists of 3 components:
    # 1.tag name
    #2. Attribute
    #3. Text

# html code has multiple matches to tag name, therefore it always selects the first

########################################
#program

import time
from selenium  import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(2)

driver.find_element("tag name","input").send_keys("Selenium")
# even though we want to enter the keys"selenium" in first name text field, the above line displays "selenium" in the search store
# on the top page because the tagname input is matching in the html code for search store. this a drawback.
time.sleep(2)






























