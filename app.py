import time
import bs4
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import hidden as hd

kumoh = "http://elearning.kumoh.ac.kr/Main.do?cmd=viewHome&userDTO.localeKey=ko"

driver = webdriver.Chrome('E:\Webdriver\Chromedriver.exe')
driver.implicitly_wait(2)
driver.get(kumoh)

elem = driver.find_element_by_xpath('//*[@id="BeforeLoginForm"]/div[1]/div/input')
elem.send_keys(hd.id)
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="BeforeLoginForm"]/div[2]/div/input')
elem.send_keys(hd.pw)
time.sleep(1)
elem.send_keys(Keys.RETURN)
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a/span') #강의목록
elem.click()
elem = driver.find_element_by_xpath('//*[@id="bodyContent"]/form/div[2]/div[1]/ul[2]/li/a/span[1]')
elem.click()

html = bs4.BeautifulSoup(driver.page_source,"html.parser")
links = html.findAll('div',{'class':'cont'})

print(str(links)[23:52].lstrip().rstrip())

youtube = webdriver.Chrome('E:\Webdriver\Chromedriver.exe')
youtube.implicitly_wait(2)
youtube.get(str(links)[23:52].lstrip().rstrip())

