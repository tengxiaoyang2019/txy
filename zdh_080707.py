'''
功能：******
作者：滕晓阳
时间：2020-**-**
'''
from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)

new_window='window.open("https://www.sogou.com/")'

driver.execute_script(new_window)

handle1=driver.current_window_handle

handles=driver.window_handles

driver.switch_to.window(handles[1])
driver.implicitly_wait(10)

driver.find_element_by_id('query').send_keys('java')
time.sleep(5)

print('运行完成')

driver.quit()