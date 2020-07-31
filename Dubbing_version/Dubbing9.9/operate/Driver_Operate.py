#coding = utf-8
'''
create on 2020年2月18日
@author : Alvin_zhu
'''
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import re
import time
from dubbbingshow_99550.Public.devices import appium_desired

class BaseOperate():
    def __init__(self,udid,port,systemport):
        self.driver = appium_desired(udid,port,systemport)
        self.dev = udid

    def back(self):
        '''
        返回键
        :return:
        '''
        os.system('adb -s %s shell input keyevent 4' % (self.dev))

    def touch(self):
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        out = os.popen("adb -s %s shell wm size" % (self.dev)).read()
        m = re.search(r'(\d+)x(\d+)', out)
        y = ("{height}".format(height=m.group(2)))
        x = ("{width}".format(width=m.group(1)))
        return int(x), int(y)

    def swip_up(self):
        '''
        手机屏幕大小
        屏幕上滑
        :return: Windowsize
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(0.5 * x, 0.8 * y, 0.5 * x, 0.4 * y, 300)

    def swip_down(self):
        '''
        屏幕下滑
        :return:
        '''

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(0.5 * x, 0.3 * y, 0.5 * x, 0.8 * y, 500)

    def swip_left(self):
        '''
        屏幕左滑
        :return:
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(0.7 * x, 0.5 * y, 0.3 * x, 0.5 * y, 300)

    def swip_right(self):
        '''
        屏幕右滑
        :return:
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(0.4 * x, 0.8 * y, 0.8 * x, 0.4 * y, 300)

    def find_id(self, id):
        '''
        定位元素(单数）
        :param id:
        :return:
        '''
        el = self.driver.find_element_by_id(id)
        return el

    def find_xpath(self, xpath):
        '''
        xpath元素
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//*[@* = '%s']" % xpath)
        el = self.driver.find_element_by_xpath(xpath_elemnt)
        return el

    def find_class(self, id):
        '''
        class name id
        :param id:
        :return:
        '''
        el = self.driver.find_element_by_class_name(id)
        return el

    def finds_class(self, classes):
        '''
        查找复数的class
        :return:
        '''
        el = self.driver.find_elements_by_class_name(classes)
        return el

    def wait_id(self, id):
        '''
        等待元素
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 50, 0.1).until(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_not_id(self, id):
        '''
        等待元素消失
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 30).until_not(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_xpath(self, xpath):
        '''
        等待元素
        :param id:
        :return:
        '''
        xpath_elemnt = ("//*[@* = '%s']" % xpath)
        element = WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_element_by_xpath(xpath_elemnt))
        return element

    def wait_toast(self, xpath):
        '''
        toast获取
        :return:
        '''
        toast_element = '%s' % xpath
        WebDriverWait(self.driver, 10, 0.05).until(lambda x: self.driver.find_element_by_xpath(toast_element))
        toast = self.driver.find_element_by_xpath(toast_element)
        return toast.text

    def wait_download(self, id):
        '''
        视频下载
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 299).until(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_load(self, xpath):
        '''
        长时间等待获取xpath信息
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//*[@text = '%s']" % xpath)
        element = WebDriverWait(self.driver, 60).until(lambda x: self.driver.find_element_by_xpath(xpath_elemnt))
        return element

    def find_ids(self, id):
        '''
        获取元素列表
        :param id:
        :return:
        '''
        el = self.driver.find_elements_by_id(id)
        return el

    def find_xpaths(self, xpath):
        '''
        获取xpath列表
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//android.widget.TextView[@text = '%s']" % xpath)
        el = self.driver.find_elements_by_xpath(xpath_elemnt)
        return el

    def find_xpaths_class(self, xpath):
        '''
        获取原生的xpath控件列表
        :param xpath:
        :return:
        '''
        xpath_elemnts = self.driver.find_elements_by_xpath(xpath)
        return xpath_elemnts

    def find_xpath_class(self, xpath):
        '''
        使用原生的单个xpath控件
        :param xpath:
        :return:
        '''
        xpath_element = self.driver.find_element_by_xpath(xpath)
        return xpath_element

    def wait_ids(self, id):
        '''
        等待获取id列表
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_elements_by_id(id))
        return element

    def screenshot(self):
        '''
        获取屏幕截图，检查UI显示
        :return:
        '''
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        type = '.png'
        self.driver.get_screenshot_as_file("E:\\screenshots\\" + tm + type)

    def search_id(self, id):
        '''
        查找当前界面是否存在某个ID控件
        :return:
        '''
        elemets = self.driver.page_source
        if id in elemets:
            return True
        else:
            return False


