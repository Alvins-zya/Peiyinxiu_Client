#coding = utf-8
'''
create on 2020年8月26日
@author : Alvin_zhu
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType
import os
import re
import time
from client.Thread_script.devices import appium_desired
from client.Thread_script.devices_list import get_conn_dev
class BaseOperate():
    def __init__(self,udid,port,systemport):
        self.driver = appium_desired(udid,port,systemport)
        self.dev = get_conn_dev()

    def lanuch_app(self):
        '''
        启动APP
        '''
        self.driver.launch_app()
        time.sleep(2)

    def back(self):
        '''
        返回键
        :return:
        '''
        os.system('adb -s %s shell input keyevent 4' % (dev))

    def touch_X(self):
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        out = os.popen("adb -s %s shell wm size" % (dev)).read()
        m = re.search(r'(\d+)x(\d+)', out)
        # y = ("{height}".format(height=m.group(2)))
        x = ("{width}".format(width=m.group(1)))
        return int(x)

    def touch_Y(self):
        out = os.popen("adb -s %s shell wm size" % (dev)).read()
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
        self.driver.swipe(0.5 * x, 0.9 * y, 0.5 * x, 0.3 * y, 300)

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
        self.driver.swipe(0.9 * x, 0.5 * y, 0.2 * x, 0.5 * y, 300)

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
        self.driver.swipe(int(start_x),int(start_y),int(end_x),int(end_y),duration=1500)

    def Long_Touche(self,El,time):
        '''
        控件长按
        '''
        TouchAction(self.driver).long_press(El,duration=time).release().perform()

    def Long_press_move(self,el,pointx,pointy):
        '''
        长按控件后移动
        '''
        TouchAction(self.driver).press(el).wait(2000).move_to(x=int(pointx),y=int(pointy)).wait(2000).release().perform()

    def press_move(self,start_x,start_y,end_x,end_y):
        '''
        点击坐标移动到另一个坐标
        :return:
        '''
        TouchAction(self.driver).press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def tap(self,X,Y):
        '''
        坐标点击
        '''
        TouchAction(self.driver).tap(x=int(X),y=int(Y)).perform()


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
    def find_Xpath(self,Xpath):
        '''
        使用绝对路径获取元素
        '''
        el = self.driver.find_element_by_xpath(Xpath)
        return el

    def find_desc(self,desc):
        '''
        空间没有ID信息，显示的是content—desc
        可使用此方法
        '''
        el = self.driver.find_element_by_accessibility_id(desc)
        return el

    def find_descs(self,descs):
        '''
        空间没有ID信息，显示的是content—desc
        定位当前界面下所有content-desc
        '''
        el = self.driver.find_elements_by_accessibility_id(descs)
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

    def find_text(self,text):
        text = self.driver.find_element_by_id(text).text
        return text

    def wait_id(self, id):
        '''
        等待元素
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 60).until(lambda x: self.driver.find_element_by_id(id))
        return element

    def wait_not_id(self, id):
        '''
        等待元素消失
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver).until_not(lambda x: self.driver.find_element_by_id(id))
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
        WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_element_by_xpath(toast_element))
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

    def search_id(self):
        '''
        查找当前界面所有ID控件
        :return:
        '''
        els = self.driver.page_source
        return els

    def getnetworkstate(self):
        '''
        获取当前手机网络状态
        '''
        info = {0: "NO_CONNECTION（没网络）",

                1: "AIRPLANE_MODE（飞行模式）",

                2: "WIFI_ONLY（仅wifi）",

                4: "DATA_ONLY（仅数据）",

                6: "ALL_NETWORK_ON（所有网络都打开）"}

        state = self.driver.network_connection
        return info.get(state)

    def Only_wifi(self):
        '''
        仅开启WiFi
        '''
        self.driver.set_network_connection(ConnectionType.WIFI_ONLY)

    def Disconnect_network(self):
        '''
        断开网络
        '''
        self.driver.set_network_connection(ConnectionType.NO_CONNECTION)

    def Only_4G(self):
        '''
        仅开启4G网络
        '''
        self.driver.set_network_connection(ConnectionType.DATA_ONLY)

    def all_network_open(self):
        '''
        开启WiFi、4G所有网络
        '''
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

    def Background(self):
        self.driver.background_app(3)

    def hide_Keyboard(self):
        '''
        隐藏输出法键盘
        :return:
        '''
        self.driver.hide_keyboard()


    def close_app(self):
        '''
        退出应用
        '''
        self.driver.close_app()

    def Quit(self):
        self.driver.quit()


