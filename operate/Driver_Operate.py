#coding = utf-8
'''
create on 2020年2月18日
@author : Alvin_zhu
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import os
import re
import time
from Public.devices import appium_desired
from Public.devices_list import get_conn_dev

class BaseOperate():
    def __init__(self):
        self.driver = appium_desired()
        self.dev = get_conn_dev()

    def back(self):
        '''
        返回键
        :return:
        '''
        os.system('adb -s %s shell input keyevent 4' % (self.dev))

    def touch_X(self):
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        out = os.popen("adb -s %s shell wm size" % (self.dev[0])).read()
        m = re.search(r'(\d+)x(\d+)', out)
        # y = ("{height}".format(height=m.group(2)))
        x = ("{width}".format(width=m.group(1)))
        return int(x)

    def touch_Y(self):
        out = os.popen("adb -s %s shell wm size" % (self.dev[0])).read()
        m = re.search(r'(\d+)x(\d+)', out)
        y = ("{height}".format(height=m.group(2)))
        # x = ("{width}".format(width=m.group(1)))
        return int(y)

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

    def swip_move(self,start_x,start_y,end_x,end_y):
        '''
        根据提供的x、y坐标进行坐标滑动
        '''
        self.driver.swipe(int(start_x),int(start_y),int(end_x),int(end_y),duration=1000)

    def Long_Touche(self,El):
        '''
        控件长按
        '''
        TouchAction(self.driver).long_press(El,duration=2000).release().perform()

    def tap(self,x,y):
        '''
        坐标点击
        '''
        TouchAction(self.driver).tap(int(x),int(y)).perform()


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
        element = WebDriverWait(self.driver, 100).until(lambda x: self.driver.find_element_by_id(id))
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
        WebDriverWait(self.driver, 5).until(lambda x: self.driver.find_element_by_xpath(toast_element))
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

    def wait_sys(self,system):
        '''
        等待系统权限弹窗
        '''
        loc = ("xpath","//*[@text = '%s']"%(system))
        el = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(loc))
        el.click()

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

    def Background(self):
        self.driver.background_app(3)

    def Quit(self):
        self.driver.quit()


