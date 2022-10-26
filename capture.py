import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

googleChromeOptions = Options()
googleChromeOptions.add_argument("--headless")
googleChromeOptions.add_argument('--ignore-certificate-errors')
googleChromeOptions.headless = True
googleChromeOptions.add_argument('--window-size=1280,720')
googleChrome = webdriver.Chrome(service=Service('/usr/bin/chromedriver'),
                          options=googleChromeOptions)

pageUrl = "https://www.sfr.fr";
googleChrome.get(pageUrl)
#element=googleChrome.find_element(By.LINK_TEXT,"Forfaits et Téléphones")
#element.click()
#time.sleep(30)
googleChrome.save_screenshot("/home/ec2-user/test/test/capture.png")
googleChrome.close()
