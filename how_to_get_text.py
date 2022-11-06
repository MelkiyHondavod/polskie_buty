from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome( ChromeDriverManager().install())

browser.get( "https://www.zalando.pl/katalog/?q=air+jordan+1+mid" )



item = browser.find_element( By.XPATH, "//a[@class='JT3_zV CKDt_l ONArL- _2dqvZS CKDt_l LyRfpJ']" )

print( item.tag_name )



item = browser.find_element( By.XPATH, "//h3[@class='_0Qm8W1 u-6V88 FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2']" )
print( item.get_attribute("href") )