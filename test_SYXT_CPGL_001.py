'''
Created on 2020-08-26
@author: txy
Project:unittest框架编写测试用例
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
testdata=('#cppic','#cppic2','#cppic3','#cppic4')
class Test(unittest.TestCase):
    def setUp(self):

        # profile = webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Local\Mozilla\Firefox\Profiles\p0muipl7.default-release')
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http:/123.57.140.190/manage/')
        self.driver.find_element_by_css_selector('input.form-control:nth-child(1)').send_keys('admin')
        self.driver.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys('admin999')
        self.driver.find_element_by_css_selector('.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
    def test_case1(self):
    #正常输入，新增产品
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410l')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410ltxm')
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        self.driver.find_element_by_class_name('ke-edit-iframe').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
    def test_case2(self):

        # 必输项未输入，新增产品
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        # 1.没有输入产品名称
        # self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410l')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410ltxm')
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        self.driver.find_element_by_class_name('ke-edit-iframe').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)

        # 2.没有输入产品编号
        self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        # self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410l')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410ltxm')
        for i in testdata:
            self.driver.find_element_by_css_selector(i).clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        # self.driver.execute_script(js)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector('html').clear()
        self.driver.find_element_by_css_selector('html').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)

        # 3.没有输入产品条形码
        self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410l')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        # self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410ltxm')

        for i in testdata:
            self.driver.find_element_by_css_selector(i).clear()
        time.sleep(1)

        # self.driver.find_element_by_css_selector('#cppic').clear()
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        # self.driver.find_element_by_css_selector('#cppic2').clear()
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        # self.driver.find_element_by_css_selector('#cppic3').clear()
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        # self.driver.find_element_by_css_selector('#cppic4').clear()
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector('html').clear()
        self.driver.find_element_by_css_selector('html').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)

        # 4.没有输入产品详细描述
        # self.driver.find_element_by_css_selector('li.active > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        for i in testdata:
            self.driver.find_element_by_css_selector(i).clear()
        time.sleep(1)

        # self.driver.find_element_by_css_selector('#cppic').clear()
        # self.driver.find_element_by_css_selector('#cppic2').clear()
        # self.driver.find_element_by_css_selector('#cppic3').clear()
        # self.driver.find_element_by_css_selector('#cppic4').clear()
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector('body').clear()
        self.driver.switch_to.default_content()
        # self.driver.find_element_by_class_name('ke-edit-iframe').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2014款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410l')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410ltxm')
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
    def test_case3(self):
        # 输入重复信息，新增产品
        # 编号重复
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2013款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410l')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201310ltxm')
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        self.driver.find_element_by_class_name('ke-edit-iframe').send_keys('铃木奥拓2013款1.0L 手动豪华炫动版')
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
        # 条形码重复
        self.driver.find_element_by_css_selector('div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        for i in testdata:
            self.driver.find_element_by_css_selector(i).clear()
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector('body').clear()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('铃木奥拓2013款1.0L 手动豪华炫动版')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201310l')
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('lmat201410ltxm')
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200826/20200826153717_51948.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200826/20200826154336_56794.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200826/20200826154450_18725.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200826/20200826154548_22700.jpg')
        self.driver.find_element_by_class_name('ke-edit-iframe').send_keys('铃木奥拓2013款1.0L 手动豪华炫动版')
        time.sleep(1)
        self.driver.find_element_by_css_selector('button.btn').click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
    def test_case4(self):
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#uppic').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('span.ke-button-common:nth-child(2) > input:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#uppic').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('li.ke-tabs-li:nth-child(1)').click()
        self.driver.find_element_by_css_selector('span.ke-button-common:nth-child(3) > input:nth-child(1)').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('span.ke-dialog-no:nth-child(1) > input:nth-child(1)').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('span.ke-button-common:nth-child(3) > input:nth-child(1)').click()
        self.driver.implicitly_wait(500)

        Select(self.driver.find_element_by_css_selector('select.ke-inline-block:nth-child(1)')).select_by_index(1)
        Select(self.driver.find_element_by_css_selector('select.ke-inline-block:nth-child(2)')).select_by_index(1)
        self.driver.find_element_by_css_selector('.ke-table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1)').click()
        self.driver.find_element_by_css_selector('a.ke-inline-block').click()
        self.driver.find_element_by_css_selector('.ke-table > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(1)').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('#remoteWidth').send_keys('123')
        self.driver.find_element_by_css_selector('input.ke-input-text:nth-child(3)').send_keys('123')
        self.driver.find_element_by_css_selector('.ke-refresh-btn').click()
        self.driver.find_element_by_css_selector('input.ke-inline-block:nth-child(4)').click()
        self.driver.find_element_by_css_selector('#remoteTitle').send_keys('一张图片')
        self.driver.find_element_by_css_selector('span.ke-button-outer:nth-child(1) > input:nth-child(1)').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('#uppic').click()

        self.driver.find_element_by_css_selector('form.ke-upload-area > div:nth-child(1) > input:nth-child(2)').send_keys('C:\fakepath\lmatlft06.jpg')
        # C:\fakepath\lmatlft06.jpg
        self.driver.find_element_by_css_selector('span.ke-button-outer:nth-child(1) > input:nth-child(1)').click()
    def test_case5(self):
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#uppic').click()
        self.driver.find_element_by_css_selector('li.ke-tabs-li:nth-child(1)').click()
        self.driver.find_element_by_css_selector('span.ke-button-outer:nth-child(1) > input:nth-child(1)').click()
    def test_case6(self):
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector('#uppic').click()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_css_selector('span.ke-button-outer:nth-child(1) > input:nth-child(1)').click()
    def test_case7(self):
        # 正常输入，编辑产品

        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)').click()
        self.driver.find_element_by_css_selector('.table > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(9) > a:nth-child(1)').click()
        self.driver.implicitly_wait(50)
        time.sleep(3)
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').clear()#清空
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').clear()
        self.driver.find_element_by_css_selector(
            'div.form-group:nth-child(4) > div:nth-child(2) > input:nth-child(1)').clear()
        for i in testdata:
            self.driver.find_element_by_css_selector(i).clear()
        time.sleep(1)

        # self.driver.find_element_by_css_selector('#cppic').clear()
        # self.driver.find_element_by_css_selector('#cppic2').clear()
        # self.driver.find_element_by_css_selector('#cppic3').clear()
        # self.driver.find_element_by_css_selector('#cppic4').clear()
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector('body').clear()
        self.driver.switch_to.default_content()
        # self.driver.find_element_by_class_name('ke-edit-iframe').clear()
        self.driver.find_element_by_css_selector('div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)').send_keys('blacktea2')#输入
        self.driver.find_element_by_css_selector('div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)').send_keys('2020-08-26-15_58_311')
        self.driver.find_element_by_css_selector('div.form-group:nth-child(4) > div:nth-child(2) > input:nth-child(1)').send_keys('2020-08-26-15_58_321')
        self.driver.find_element_by_css_selector('#cppic').send_keys('/upload/image/20200821/20200821093353_31848.jpg')
        self.driver.find_element_by_css_selector('#cppic2').send_keys('/upload/image/20200821/20200821093412_32792.jpg')
        self.driver.find_element_by_css_selector('#cppic3').send_keys('/upload/image/20200821/20200821093422_46277.jpg')
        self.driver.find_element_by_css_selector('#cppic4').send_keys('/upload/image/20200821/20200821093432_83600.jpg')
        self.driver.find_element_by_class_name('ke-edit-iframe').send_keys('是好茶')
        self.driver.find_element_by_css_selector('button.btn').click()
    def test_case8(self):
        self.driver.find_element_by_css_selector('li.sub-menu:nth-child(1) > a:nth-child(1) > span:nth-child(3)').click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_css_selector(
            'li.sub-menu:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)').click()

        self.driver.find_element_by_css_selector('')
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()


