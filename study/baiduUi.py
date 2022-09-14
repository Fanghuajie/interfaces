import time

from selenium import webdriver

driver = webdriver.chrome()

driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")

time.sleep(2)
SR = driver.find_element_by_id('kw')
SR.send_keys('百度文库')

tj = driver.find_element_by_id('su')
tj.click()
dj = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
dj.click()
time.sleep(1)
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
dj1 = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div[2]/div[5]/div[2]')
dj1.click()
time.sleep(5)
driver.close()

