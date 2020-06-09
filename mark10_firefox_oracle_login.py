from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get("https://eiyi.login.ap1.oraclecloud.com/")

submit   = browser.find_element_by_id("ssoBtn")
submit.click()

username = browser.find_element_by_id("userNameInput")
password = browser.find_element_by_id("passwordInput")
submit   = browser.find_element_by_id("submitButton")
username.send_keys("ENTER USERNAME")
password.send_keys("ENTER PASSWORD")
submit.click()
