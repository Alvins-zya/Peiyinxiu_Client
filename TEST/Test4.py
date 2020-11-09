# coding: utf-8
import os,sys
from appium.webdriver.common.touch_action import TouchAction
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Public.Driver_Operate import BaseOperate,resource_id
class Test():
    def __init__(self):
        self.D = BaseOperate()
        self.ID = resource_id
    def test_a(self):
        els = self.D.find_id(self.ID + 'filmBg1')
        TouchAction(self.D.driver).long_press(els,3000).release().perform()

if __name__ == '__main__':
    Test().test_a()