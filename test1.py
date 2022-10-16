 from selenium.webdriver.chrome.options import Options  

 chrome_options = Options()  
 chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.sfr.fr/")
time.sleep(2)


time.sleep(5)
#driver.quit()
