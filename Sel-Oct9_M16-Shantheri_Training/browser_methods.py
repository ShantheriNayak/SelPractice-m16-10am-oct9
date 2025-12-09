import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Edge(opts)

##launch the application
driver.get('https://www.myntra.com/')
time.sleep(2)

##maximizing browser
driver.maximize_window()
time.sleep(2)

##minimizing browser
#driver.minimize_window()
#time.sleep(2)

##to go back page
driver.back()
time.sleep(2)

##to go forward page
driver.forward()
time.sleep(2)

##to refresh the page
driver.refresh()
time.sleep(2)

#properties
print(driver.current_url)     ###https://www.myntra.com/
print(driver.title)    ###Online Shopping for Women, Men, Kids Fashion & Lifestyle - Myntra
print(driver.name)    ###chrome
print(driver.page_source) #HTML code of the page is shown as output:-->>>> <html lang="en"><head><title>Online Shopping for Women,

##to save the screenshot of the page
#driver.save_screenshot('Myntra_homepage.png')
driver.save_screenshot(r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files\myntra.png')  #this output is saved in files directory

#to close the browser
driver.close()