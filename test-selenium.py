from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException

# sets chrome as driver
driver = webdriver.Chrome()

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

eleShowMsgBtn = driver.find_element_by_css_selector('button.btn')

# wait
time.sleep(3)

# clicks 'Show Message' button
#ElementClickInterceptedException: 'at-cv-lightbox-inner'
try:
    eleShowMsgBtn.click()
except:
    'at-cv-lightbox-inner'

# find outputted message
eleYourMsg = driver.find_element_by_id('display')

# wait 3 seconds
time.sleep(3)

# close window
driver.close()
