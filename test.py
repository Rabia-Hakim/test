import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'),
                          options=chrome_options)
def clich(chemin):
    
    try:
    
        driver.find_element(By.XPATH,chemin).click()
    except:
        
        driver.save_screenshot("/home/ec2-user/captures/error.png")
        
        
driver.get('https://www.sfr.fr/')
time.sleep(8)
#clich("//div[@id='CkC']/div/a[2]")
#element=driver.find_element(By.LINK_TEXT,"Forfaits et Téléphones")
driver.save_screenshot("/home/ec2-user/test/test/pantt.png")

driver.quit()
