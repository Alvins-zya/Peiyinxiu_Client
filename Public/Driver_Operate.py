#coding = utf-8
'''
create on 2020年2月18日
@author : Alvin_zhu
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType
import os,sys
import re
import time
from Public.devices import appium_desired
from Public.devices_list import get_connect_device_id
import yaml
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
filePath = os.path.dirname(__file__)
with open(filePath+'\\devices_caps.yaml', 'r')as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
dev = data['deviceName']
resource_id = 'com.happyteam.dubbingshow:id/'
class BaseOperate():
    def __init__(self):
        self.driver = appium_desired()
        self.dev = get_connect_device_id()
        self.id = resource_id

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
        默认点击位置在元素的左上角，会导致长按等操作无法触发。
        可将其改为中心后，问题解决
        '''
        # element = self.driver.find_element_by_id(El)
        # element = EL.rect
        el = self.driver.find_element_by_id(self.id + El).rect
        el_x = int(el['x'] + el['width'] / 2.0)
        el_y = int(el['y'] + el['height'] / 2.0)
        TouchAction(self.driver).long_press(x=el_x, y=el_y, duration=time).perform()
        # TouchAction(self.driver).long_press(x=El_x,y=El_y,duration=time).perform()
        # el = self.driver.find_element_by_id(element)
        # el_x = el.location.get('x')
        # el_y = el.location.get('y')
        # TouchAction(self.driver).long_press(x=int(el_x), y=int(el_y), duration=3000).release().perform()
        # time.sleep(2)

    def Long_Touches(self,El,num,time):
        '''
        控件list中选择一个
        :return:
        '''
        el = self.driver.find_elements_by_id(self.id + El)[num].rect
        el_x = int(el['x'] + el['width'] / 2.0)
        el_y = int(el['y'] + el['height'] / 2.0)
        TouchAction(self.driver).long_press(x=el_x, y=el_y, duration=time).perform()

    def Long_press_move(self,El,point_x,point_y):
        '''
        :param El:获取控件的坐标位置
        :param point_x: 需要移动到的坐标位置X
        :param point_y: 需要移动到的坐标位置Y
        :return:
        '''
        el = self.driver.find_element_by_id(self.id + El).rect
        el_x = int(el['x'] + el['width'] / 2.0)
        el_y = int(el['y'] + el['height'] / 2.0)
        TouchAction(self.driver).press(x=el_x,y=el_y).wait(2000).move_to(x=int(point_x),y=int(point_y)).wait(2000).release().perform()

    def Double_touche(self,X,Y):
        '''
        屏幕双击
        :return:
        '''
        TouchAction(self.driver).press(x= int(X), y= int(Y)).release().perform().press(x=int(X), y=int(Y)).release().perform()

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

    def tap_el(self,El):
        '''
        获取控件按钮后点击控件居中坐标位置
        :return:
        '''
        el = self.driver.find_element_by_id(self.id + El).rect
        el_x = int(el['x'] + el['width'] / 2.0)
        el_y = int(el['y'] + el['height'] / 2.0)
        TouchAction(self.driver).tap(x=el_x,y=el_y).perform()

    def find_id(self,id):
        el = self.driver.find_element_by_id(self.id + id)
        return el
    def find_id_clear(self,id):
        '''
        清楚输入框内容
        '''
        self.driver.find_element_by_id(self.id + id).clear()

    def find_id_send(self,id,value):
        el = self.driver.find_element_by_id(self.id + id).send_keys(value)
        return el

    def find_ids_send(self,id,num,value):
        el = self.driver.find_elements_by_id(self.id + id)[num].send_keys(value)
        return el

    def find_id_click(self, id):
        '''
        点击元素(单数）
        :param id:
        :return:
        '''
        el = self.driver.find_element_by_id(self.id + id).click()
        return el

    def find_id_third_part(self,id):
        '''
        第三方控件点击
        '''
        el = self.driver.find_element_by_id(id).click()
        return el

    def find_id_state(self,id):
        '''
        获取控件的状态：true or false
        '''
        el = self.driver.find_element_by_id(self.id + id).get_attribute('checked')
        return el

    def find_id_text(self,id):
        '''
        获取元素ID文案内容
        :param id:
        :return:
        '''
        el = self.driver.find_element_by_id(self.id + id).text
        return el

    def find_xpath(self, xpath):
        '''
        xpath元素
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//*[@text='%s']" % xpath)
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

    def wait_id_click(self, id):
        '''
        :param id:显示选择的ID
        :return:点击元素ID
        '''
        el = WebDriverWait(self.driver,60).until(EC.element_to_be_clickable((By.ID,self.id + id))).click()
        return el
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='u1']/a[8]"))).click()

    def wait_id(self,id):
        '''
        等待选择ID
        :param id:
        :return:
        '''
        WebDriverWait(self.driver, 60,).until(
            lambda x: self.driver.find_element_by_id(self.id + id))

    def wait_id_three_party(self,id):
        '''
        第三方空间识别等待
        '''
        WebDriverWait(self.driver, 60, ).until(lambda x: self.driver.find_element_by_id(id))
    def wait_not_id(self, id):
        '''
        等待元素消失
        :param id:
        :return:
        '''
        WebDriverWait(self.driver,30).until_not(lambda x: self.driver.find_element_by_id(self.id + id))

    def wait_xpath(self, xpath):
        '''
        等待元素
        :param xpath:
        :return:
        '''
        xpath_element = ("//*[@text = '%s']" % xpath)
        WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_element_by_xpath(xpath_element))
        time.sleep(2)

    def wait_toast(self, xpath):
        '''
        toast获取
        :return:
        '''
        toast_element = '%s' % xpath
        WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_element_by_xpath(toast_element))
        toast = self.driver.find_element_by_xpath(toast_element).text
        return toast

    def wait_download(self, id):
        '''
        视频下载
        :param id:
        :return:
        '''
        element = WebDriverWait(self.driver, 299).until(lambda x: self.driver.find_element_by_id(self.id + id))
        return element

    def wait_load(self, xpath):
        '''
        长时间等待获取xpath信息
        :param xpath:
        :return:
        '''
        xpath_elemnt = ("//*[@text = '%s']" % xpath)
        element = WebDriverWait(self.driver, 120).until(lambda x: self.driver.find_element_by_xpath(xpath_elemnt))
        return element

    def wait_sys(self,system):
        '''
        等待系统权限弹窗
        '''
        loc = ("xpath","//*[@text = '%s']"%(system))
        el = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(loc))
        el.click()

    def find_ids_click(self, id, i):
        '''
        获取元素列表
        :param id:
        :return:
        '''
        self.driver.find_elements_by_id(self.id + id)[i].click()

    def find_ids_text(self, id, i):
        '''
        获取元素列表
        :param id:
        :return:
        '''
        content = self.driver.find_elements_by_id(self.id + id)[i].text
        return content
    def find_ids(self, id):
        '''
        获取元素列表
        :param id:
        :return:
        '''
        el = self.driver.find_elements_by_id(self.id + id)
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
        element = WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_elements_by_id(self.id + id))
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
        self.driver.background_app(2)
        time.sleep(2)

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


