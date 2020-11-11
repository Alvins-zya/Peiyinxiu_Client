# coding: utf-8
import os,sys,unittest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Public.devices import appium_desired
class Test():
    def __init__(self):
        self.driver = appium_desired()
    def test_a(self):
        el = self.driver.find_element_by_id('com.happyteam.dubbingshow:id/filmBg1').rect
        print(el)
        el_x = int(el['x'] + el['width']/2.0)
        el_y = int(el['y'] + el['height']/2.0)
        print(el_x,el_y)
        TouchAction(self.driver).long_press(x=el_x,y=el_y,duration=3000).perform()
        # self.driver.tap(el,duration=3000)
if __name__ == '__main__':
    Test().test_a()