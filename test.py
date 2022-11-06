#from distutils.command.config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

from custom_funcs import *

import time


#ep =  get_json( "config.json" )["common_data"]["folder_path"]
#browser = webdriver.Firefox( executable_path= f"{ ep }\\geckodriver.exe" )

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome( ChromeDriverManager().install())

#browser = webdriver.Chrome()

browser.get( 'https://www.zalando.pl/katalog/?q=air+jordan&p=18' )

# Find the search box
#elem = browser.find_element(By.NAME, 'p')
elem = browser.find_elements( By.XPATH, "//div[@class='DT5BTM w8MdNG cYylcv QylWsg _75qWlu iOzucJ JT3_zV DvypSJ']" )

print(elem)

time.sleep(10)
browser.close()