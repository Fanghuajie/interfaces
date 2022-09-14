

import time
from selenium import webdriver
import datetime
# from requests_html import HTMLSession
driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://chongzhi.jd.com/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="kbCoagent"]/ul/li[1]/a/span').click()
time.sleep(2)
driver.switch_to.frame('ptlogin_iframe')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="qlogin_list"]/a').click()
# 这里没打开新窗口，不用切换
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]').click()
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="J_babelOptPage"]/div/div[9]/div/div').click()
handles = driver.window_handles
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
# driver.find_element_by_xpath('//*[@id="J_babelOptPage"]/div/div[9]/div/div').click()
time.sleep(2)
j = 1
while j > 0:
    if datetime.datetime.now().minute == 59 and datetime.datetime.now().second == 59:
        i = 1
        while i > 0:
            driver.find_element_by_xpath('//*[@id="J_babelOptPage"]/div/div[2]/div/div[1]/a[2]').click()
