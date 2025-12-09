import timefrom selenium import webdriver
opts=webdriver.ChromeOptions()# ID locator example

opts.add_experimental_option("detach", True)#lauching chrome browser and preventing from closing automatically

driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.find_element('id','name').send_keys('Mary')
time.sleep(2)
driver.find_element('id','email').send_keys('mary@gmail.com')
time.sleep(2)
driver.find_element('id','phone').send_keys('9087093412')
time.sleep(2)
driver.find_element('id','textarea').send_keys('Bengaluru')
time.sleep(2)
driver.find_element('id','female').click()
time.sleep(2)
driver.find_element('id','wednesday').click()
time.sleep(2)
driver.find_element('id','country').send_keys('India')
time.sleep(2)
driver.find_element('id','colors').send_keys('red')
time.sleep(2)
driver.find_element('id','animals').send_keys('cheetah')
time.sleep(2)
