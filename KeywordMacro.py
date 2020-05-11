import bs4
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

GoogleAds = "https://ads.google.com/"

#driver = webdriver.Chrome('E:\Webdriver\Chromedriver.exe')
driver = webdriver.Chrome('D:\Webdriver\Chromedriver.exe')
driver.implicitly_wait(2)
driver.get(GoogleAds)

elem = driver.find_elements_by_xpath('//*[@id="h-js-header__drawer"]/div[2]/ul/li[1]/a/span')
