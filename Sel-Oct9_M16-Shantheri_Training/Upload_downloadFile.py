import time

# wap to upload a  single file

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(3)
#
# file1=(r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Sel-Oct9_M16-Shantheri_Training\files\heading.png')
# driver.find_element('xpath','//input[@id="singleFileInput"]').send_keys(file1)
#
# time.sleep(3)
# driver.close()

###############################################################################

# wap to upload multiple; files

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(3)
#
# file1=r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Sel-Oct9_M16-Shantheri_Training\files\heading.png'
# file2=r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Sel-Oct9_M16-Shantheri_Training\files\myntra.png'
# file3=r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Sel-Oct9_M16-Shantheri_Training\files\searchbar.png'
# file4=r'C:\Users\Prashanth Nayak\Desktop\py progs\Python-Selenium daily notes\XpathExample.html'
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}\n{file4}')
#
#
# time.sleep(3)
# driver.close()

##################################################################
'''          upload-dowload files       '''
'''
download.default_directory--->>sets the folder where the downloaded files will be saved/stored
download.prompt_for_download--->>
safebrowsing.enabled--->>Enables Chromes's safe browsing so it doesnt block the download
plugins.always_open_pdf_externally--->>

'''


'''Chrome browser'''
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# prefs={
#     "download.default_directory":r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Sel-Oct9_M16-Shantheri_Training\files',
#     "download.prompt_for_download":False,
#     "safebrowsing.enabled":True,
#     "plugins.always_open_pdf_externally":True
# }
# opts.add_experimental_option("prefs", prefs)
#
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demoqa.com/upload-download")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('xpath','//a[text()="Download"]').click()
# time.sleep(3)
# driver.close()

#######################################################

'''Firefox browser'''
from selenium import webdriver
opts=webdriver.FirefoxOptions()
opts.set_preference("browser.download.folderList",2)
opts.set_preference("browser.download.dir",r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\Shantheri_Training\files')
opts.set_preference("pdfjs.disabled",True)

driver=webdriver.Firefox(opts)
driver.get("https://demoqa.com/upload-download")
driver.maximize_window()
time.sleep(3)
driver.find_element('xpath','//a[text()="Download"]').click()
time.sleep(3)
driver.close()











