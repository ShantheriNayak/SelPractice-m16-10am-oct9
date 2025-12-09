import time
from selenium import webdriver
from DataDrivenTesting.Read_Excel import reading_testdata

path=r'C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining\DataDrivenTesting\TestData.xlsx'
data=reading_testdata(path,'reg')

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
time.sleep(1)

driver.find_element('xpath','//a[text()="Register"]').click()
time.sleep(1)
driver.find_element('id','gender-female').click()
driver.find_element('id','FirstName').send_keys(data['firstname'])
driver.find_element('id','LastName').send_keys(data['lastname'])
driver.find_element('id','Email').send_keys(data['email_id'])
driver.find_element('id','Password').send_keys(data['pwd'])
driver.find_element('id','ConfirmPassword').send_keys(data['confirm_pwd'])
time.sleep(1)




































































