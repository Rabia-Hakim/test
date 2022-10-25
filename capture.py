from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

googleChromeOptions = webdriver.chrome.options.Options()
googleChromeOptions.headless = True
googleChromeOptions.add_argument('--window-size=1280,720')
googleChrome = webdriver.Chrome(executable_path="/usr/bin/chromedriver",
options=googleChromeOptions)
pageUrl = "https://www.w3schools.com";
googleChrome.get(pageUrl)
googleChrome.save_screenshot('images/w3schools_google-chrome.png')
googleChrome.close()
