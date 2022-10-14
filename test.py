import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.sfr.fr/")
time.sleep(2)


time.sleep(5)
#driver.quit()
