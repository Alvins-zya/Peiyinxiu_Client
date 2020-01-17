#coding = utf-8
#防止中文显示乱码
#coding = gb18030

from selenium.webdriver.support.ui import WebDriverWait
import os
from Peiyinxiu_Client.devices import device,dev
class BaseOperate():
    def __init__(self):
        self.driver = device()
    def back(self):
        '''
        返回键
        :return:
        '''
        os.system('adb -s %s shell input keyevent 4'%dev)
    def touch(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y

    def swip_up(self):
        '''
        手机屏幕大小
        屏幕上滑
        :return: Windowsize
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(0.5*x,0.8*y,0.5*x,0.4*y,300)

    def swip_down(self):
        '''
        屏幕下滑
        :return:
        '''

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(0.5 * x, 0.3 * y, 0.5 * x, 0.8 * y, 300)

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

    def find_id(self,id):
        '''
        定位元素(单数）
        :param id:
        :return:
        '''
        el = self.driver.find_element_by_id(id)
        return el

    def find_xpath(self,xpath):
        '''
        xpath元素
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//*[@* = '%s']"%xpath)
        el = self.driver.find_element_by_xpath(xpath_elemnt)
        return el
    def find_class(self,id):
        '''
        class name id
        :param id:
        :return:
        '''
        el = self.driver.find_element_by_class_name(id)
        return el

    def wait_id(self,id):
        '''
        等待元素
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_not_id(self,id):
        '''
        等待元素消失
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver,50).until_not(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_xpath(self,xpath):
        '''
        等待元素
        :param id:
        :return:
        '''
        xpath_elemnt = ("//*[@* = '%s']"%xpath)
        element = WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_element_by_xpath(xpath_elemnt))
        return element
    def wait_toast(self,xpath):
        '''
        toast获取
        :return:
        '''
        toast_element = '%s'%xpath
        WebDriverWait(self.driver, 10,0.01).until(lambda x: self.driver.find_element_by_xpath(toast_element))
        toast = self.driver.find_element_by_xpath(toast_element).text
        return toast

    def wait_download(self,id):
        '''
        视频下载
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 299).until(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_load(self,xpath):
        '''
        长时间等待获取xpath信息
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//*[@text = '%s']" % xpath)
        element = WebDriverWait(self.driver, 60).until(lambda x: self.driver.find_element_by_xpath(xpath_elemnt))
        return element


    def find_ids(self,id):
        '''
        获取元素列表
        :param id:
        :return:
        '''
        el = self.driver.find_elements_by_id(id)
        return el

    def find_xpaths(self,xpath):
        '''
        获取xpath列表
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//android.widget.TextView[@text = '%s']" % xpath)
        el =  self.driver.find_elements_by_xpath(xpath_elemnt)
        return el

    def wait_ids(self,id):
        '''
        等待获取id列表
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_elements_by_id(id))
        return element
