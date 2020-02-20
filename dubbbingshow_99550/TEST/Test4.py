#coding = utf-8
import yaml
from dubbbingshow_99550.Public.devices import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from dubbbingshow_99550.operate.Driver_Operate import BaseOperate

class Dubbing():
    def __init__(self,udid,port):
        self.D = BaseOperate(udid,port)

    def dubbing(self):
        try:
            WebDriverWait(self.D,30).until(lambda x:self.D.find_id('com.happyteam.dubbingshow:id/task_box'))
            print('===开始===')
        except:
            print('应用启动失败')
        self.D.find_id('com.happyteam.dubbingshow:id/btn_more').click()

    def start(self):
        self.dubbing()