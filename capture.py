from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

googleChromeOptions = Options()
googleChromeOptions.add_argument("--headless")
googleChromeOptions.headless = True
googleChromeOptions.add_argument('--window-size=1280,720')
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'),
                          options=chrome_options)

pageUrl = "https://www.w3schools.com";
googleChrome.get(pageUrl)
googleChrome.save_screenshot('images/w3schools_google-chrome.png')
googleChrome.close()
