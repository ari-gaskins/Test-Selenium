from selenium import webdriver
from dotenv import load_dotenv
from keyring import http

# sets chrome as driver
driver = webdriver.Chrome(load_dotenv.CHROMEDRIVER)

# sets url for test
url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

# opens window at max
driver.maximize_window()

# opens url 
driver.get(url)

# goes to message bar by element id
eleUserMessage = driver.find_element_by_id('user-message')

# makes sure it is clear
eleUserMessage.clear()

# sends message 'Test Python'
eleUserMessage.send_keys('Test Python')

# finds 'Show Message' button 
eleShowMsgBtn = driver.find_element_by_css_selector('#get-input > .btn')

# clicks 'Show Message' button
eleShowMsgBtn.click()

# find outputted message
eleYourMsg = driver.find_element_by_id('display')

# show message in .txt file
assert eleYourMsg in eleYourMsg.txt

# close window
driver.close()
