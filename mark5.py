from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint
browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
browser.get('https://www.myntra.com/')
assert "Online Shopping" in browser.title
search = browser.find_element_by_class_name("desktop-searchBar") # Find the search box by class
search.send_keys("watch") #send the value of search field
submit_button = browser.find_element_by_class_name("desktop-submit")
submit_button.click()
#Lets wait for lobby page to load
delay = 10 # seconds max wait
myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "horizontal-filters-title")))
browser.save_screenshot("loggedIn.png") ## This will be stored in the location/path mentioned or the current directory
browser.close() # close browser
