import time
import bs4
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import hidden as hd

Ads = "https://ads.google.com/"
KeyPlanner = "https://ads.google.com/aw/keywordplanner/home"
driver = webdriver.Chrome('E:\Webdriver\Chromedriver.exe')
driver.implicitly_wait(2)
driver.get(Ads)
time.sleep(1)

def login():
    elem = driver.find_element_by_xpath('/html/body/div/div[1]/div[4]/ul/li[2]/a/span')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="identifierId"]')
    elem.send_keys(hd.Gid)
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    elem.send_keys(hd.Gpw)
    elem = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
    elem.click()

def keywordinput():
    driver.get(KeyPlanner)

    time.sleep(2)
    elem = driver.find_elements_by_xpath('//*[@id="E36558FE-B2D9-406E-B255-816FCC7E8F35--0"]')
    elem.click()


login()
time.sleep(5)
keywordinput()
