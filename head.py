from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'),
                          options=chrome_options)
driver.get('https://www.google.com/')
get_title = driver.title
print(get_title)
driver.quit()
