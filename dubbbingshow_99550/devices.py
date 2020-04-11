#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import os
from appium import webdriver
#获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


dev = 'd772f3d1'


def device():
    desired_caps = {}
    desired_caps['platformName'] ='Android'
    desired_caps['deviceName'] = dev
    desired_caps['udid'] = dev
    desired_caps['platformVersion'] = '8'
    desired_caps['appPackage'] = 'com.happyteam.dubbingshow'
    desired_caps['appActivity'] = 'ui.StartActivity'
    desired_caps['appWaitPackage'] = 'com.happyteam.dubbingshow'
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['ignoreUnimportantViews'] = True
    desired_caps['dontStopAppOnReset'] = True
    desired_caps['newCommandTimeout'] = 10000
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['systemPort'] = 8100

    try:
        driver = webdriver.Remote('http://localhost:4740/wd/hub', desired_caps)
        return driver
    except:
        print('NO driver!!')