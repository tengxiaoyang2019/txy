from selenium import webdriver
import time

def qqmail():

    driver=webdriver.Firefox()
    # driver.get('https://mail.qq.com/')

    driver.get('https://www.baidu.com')

    driver.find_element_by_css_selector('#kw').send_keys('QQ邮箱')
    # time.sleep(2)
    driver.find_element_by_css_selector('#su').click()
    driver.implicitly_wait(10)

    driver.find_element_by_link_text('QQ邮箱').click()
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[-1])

    driver.switch_to.frame('login_frame')
    driver.find_element_by_css_selector('#img_out_157536046').click()
    time.sleep(5)

    driver.switch_to.default_content()
    driver.find_element_by_link_text('写信').click()
    time.sleep(5)

    # driver.switch_to.frame("mainframe")
    driver.find_element_by_css_selector('body').send_keys('作业内容')

    # driver.switch_to.default_content()

    driver.switch_to.frame("mainFrame")

    driver.find_element_by_css_selector('#toAreaCtrl > div:nth-child(2) > input:nth-child(1)').send_keys('1136706340@qq.com')
    driver.find_element_by_id('subject').send_keys('作业邮件')

    driver.find_element_by_css_selector("a.btn_gray:nth-child(1)").click()

    driver.switch_to.default_content()

    time.sleep(5)

    # time.sleep(10)
    driver.quit()

qqmail()