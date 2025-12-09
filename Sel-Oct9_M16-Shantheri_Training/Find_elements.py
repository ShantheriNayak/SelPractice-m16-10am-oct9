import time

#Find_elements:

#Ex 1. wap to display all the footer elements

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(3)
#
# footer_elements=driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
# print(footer_elements)#prints only address of all 22 footer elements in list format
# #[wb1,wb2,wb3,wb4.......wb22]
# for ele in footer_elements:
#     print(ele.text)

############################################################
#ex2 wap to display all the elements in category section

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(3)
#
# Category_elements=driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
# print(Category_elements)#prints only address of all category section elements in list format
# #[wb1,wb2,wb3,wb4.......wb7]
# for ele in Category_elements:
#     print(ele.text)

###################################################################

#eg3:WAP to fetch all the popular searches in the footer of myntra

# from selenium import webdriver
# from selenium.webdriver import Keys
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(3)
#
# Popular_searches=driver.find_elements('xpath','//div[@class="desktop-pSearchlinks"]//a')
# #print(footer_elements)#prints only address of all category section elements in list format
# #[wb1,wb2,wb3,wb4.......wb47]
# for ele in Popular_searches:
#     print(ele.text)
'''
output:
[<selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.24")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.25")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.26")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.27")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.28")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.29")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.30")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.31")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.32")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.33")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.34")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.35")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.36")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.37")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.38")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.39")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.40")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.41")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.42")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.43")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.44")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.45")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.46")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.47")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.48")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.49")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.50")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.51")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.52")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.53")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.54")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.55")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.56")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.57")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.58")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.59")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.60")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.61")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.62")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.63")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.64")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.65")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.66")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.67")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.68")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.69")>, <selenium.webdriver.remote.webelement.WebElement (session="ca209a849b5569cffccf1243a5099b6b", element="f.5FBD8C71ADFAD055CF2F66FC83F0714E.d.9AC8D35F7D2A4938D02E8260D7738E5F.e.70")>]
Makeup
Dresses For Girls
T-Shirts
Sandals
Headphones
Babydolls
Blazers For Men
Handbags
Ladies Watches
Bags
Sport Shoes
Reebok Shoes
Puma Shoes
Boxers
Wallets
Tops
Earrings
Fastrack Watches
Kurtis
Nike
Smart Watches
Titan Watches
Designer Blouse
Gowns
Rings
Cricket Shoes
Forever 21
Eye Makeup
Photo Frames
Punjabi Suits
Bikini
Myntra Fashion Show
Lipstick
Saree
Watches
Dresses
Lehenga
Nike Shoes
Goggles
Bras
Suit
Chinos
Shoes
Adidas Shoes
Woodland Shoes
Jewellery
Designers Sarees
'''
#####################################################################################################
#eg 4:WAP to fetch all the adidas shoe results along with name and price

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(3)
#
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(3)
#
# driver.find_element('xpath','//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(3)
#
# adidas_shoes = driver.find_elements('xpath', '//h4[@class="product-product"]')      ## [wb1, wb2, wb3,..wb50]
# shoes_prices = driver.find_elements('xpath', '//div[@class="product-price"]')       ## [wb1, wb2, wb3,..wb50]
#
# for shoe, price in zip(adidas_shoes, shoes_prices):
#     print(shoe.text, "=", price.text)
'''
Zip concept in python
name1='ankesh'
name2='naveeeen'
for i, j in zip(name1, name2):
    print(i, j)
Output: a n
        n a
        k v
        e e
        s e
        h e
          e
          e
          n

'''
#####################################################################################
#assignment 4:WAP to fetch all colors by clicking on 18+more and print all the colors for adidas originals shoes

#//div[@class="vertical-filters-filters"][2]
#//div[@class="colour-more"].click

#Category_elements=driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
# print(Category_elements)#prints only address of all category section elements in list format
# #[wb1,wb2,wb3,wb4.......wb7]
# for ele in Category_elements:
#     print(ele.text)

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://www.myntra.com/")
# time.sleep(3)
#
# driver.find_element('xpath','//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(3)
#
# driver.find_element('xpath','//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(3)
#
# driver.find_element('xpath','//div[@class="vertical-filters-filters"][2]').click()
# time.sleep(3)
#
# Colour_ele=driver.find_element('xpath','//div[@class="colour-more"]').click()
# time.sleep(3)
#
# for ele in Colour_ele:
#     print(ele.text)

#output:
''' for ele in Colour_ele:
               ^^^^^^^^^^
TypeError: 'NoneType' object is not iterable'''


################################################################################################

#3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    #wap to print the name and price of each food item in available


from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)

driver.get("https://www.zomato.com/bangalore/restaurants")
time.sleep(3)

#search for pizza,
driver.find_element('xpath','//input[@class="sc-dBfaGr dyyfrm"]').send_keys('pizza')
time.sleep(3)

#select pizza-delivery,
# driver.find_element('xpath','//p[text()="Pizza - Delivery"][1]').click()
# time.sleep(3)
# not showing dropdown to select the pizza delivery



##############################################
#assignment 5: lauch bookmyshow from pycharm, 2.select location .print all the movie names available

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://in.bookmyshow.com/")
# time.sleep(2)
# driver.find_element('xpath','//p[text()="Bengaluru"]').click() #Select location="bengaluru"
# time.sleep(2)
#
# #click on movies
# driver.find_element('xpath','//a[text()="Movies"]').click()
# time.sleep(2)
#
# #print names of all the movies:
# movies=driver.find_elements('xpath','//div[@class="sc-7o7nez-0 elfplV"]')
# for ele in movies:
#     print(ele.text)
'''
output:
De De Pyaar De 2
Kaantha
Gatha Vaibhava
The Running Man
Now You See Me: Now You Don't
Love OTP
Jai
Udaala
Dawood
Premam Madhuram
Kaal Trighori
Hikora
Kite Brothers
Santhana Prapthirasthu
Jigris
Agra (2025)
'''


####################################################################################
'''
1.  wap to fetch all the popular searches from https://www.myntra.com/
2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''

########################################################################

#example7: enter texts in all the 9 textboxes in demo.html

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
# all_textboxes=driver.find_elements('xpath','//input[@name="fname"]')
# print(all_textboxes)    #list of all the webelements  [wb1,wb2,wb3......wb9]
#
# # for textbox in all_textboxes:
# #     textbox.send_keys('data') #prints only data in all the text boxes.
#
# data_list=['kantara','Narasimha','fighter','shershah','su from so','RCB','Brahmastra','2States','the family man']
# for textbox, data in zip(all_textboxes,data_list):
#     textbox.send_keys(data)

#############################################################
#WAP to fetch all the links present in Python.org

# from selenium import webdriver
#
# driver = webdriver.Firefox()
# time.sleep(2)
#
# driver.get('https://www.python.org/')
# all_links=driver.find_elements('tag name', 'a')# list of webelements[a1,a2.a3.....]
# for link in all_links:
#     print(link.get_attribute('href'))
# '''
# all links are mainly present in href under the  tagname <a>





































