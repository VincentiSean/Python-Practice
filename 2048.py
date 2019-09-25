#! python3
# 2048.py - This program is designed to play the 2048 game with a 
#       preset of up -> right -> down -> left -> repeat motions.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up browser and go to thee webpage containing 2048
browser = webdriver.Firefox()
browser.get('https://play2048.co')

# Just get into it, start hitting keys with Selenium
time.sleep(10)
gameElem = browser.find_element_by_tag_name('html')
for x in range(1000):
    gameElem.send_keys(Keys.UP)
    time.sleep(.15)
    gameElem.send_keys(Keys.RIGHT)
    time.sleep(.15)
    gameElem.send_keys(Keys.DOWN)
    time.sleep(.15)
    gameElem.send_keys(Keys.LEFT)
    time.sleep(.15)