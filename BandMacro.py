import time
import bs4
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import BandMacroHidden as bd

Band = "https://band.us/"
driver = webdriver.Chrome('E:\Webdriver\Chromedriver.exe')
driver.implicitly_wait(2)
driver.get(Band)
time.sleep(20)


elem = driver.find_element_by_xpath('//*[@id="gnbProfileMenuPopup"]/div/ul/li[2]/a') #내가쓴글
elem.click()
time.sleep(1)
