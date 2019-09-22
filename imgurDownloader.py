#! python3
# imgurDownloader.py - This project takes an argument and searches imgur with the user input
#   and proceeds to download all image search results.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Get user input
print('Please enter a tag to  search & download from Imgur.')
tag = input()

# Assign Firefox as the browser of choice
browser = webdriver.Firefox()
browser.get('https://imgur.com')
print('Connecting to imgur...')

# Search imgur with user input 
print('Searching for the images...')
searchbar = browser.find_element_by_xpath('//input[@class="Searchbar-textInput"]')
searchbar.send_keys(tag)
searchbar.send_keys(Keys.ENTER)

# Loop through all images and download