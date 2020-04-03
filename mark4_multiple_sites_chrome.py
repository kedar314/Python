import webbrowser
import os

url = 'https://www.appstraps.com'

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', "open")

webbrowser.get(chrome_path).open_new(url)
webbrowser.get(chrome_path).open('https://in.godaddy.com/')
webbrowser.get(chrome_path).open('https://www.indeed.co.in/')
webbrowser.get(chrome_path).open('https://www.naukri.com/')
webbrowser.get(chrome_path).open('https://www.monsterindia.com/')
webbrowser.get(chrome_path).open('https://www.w3schools.com/python/')
webbrowser.get(chrome_path).open('https://www.onlinegdb.com/')
webbrowser.get(chrome_path).open('https://www.google.com/')


