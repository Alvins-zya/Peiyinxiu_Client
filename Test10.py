# coding = utf-8
# 防止中文显示乱码
# coding = gb18030

# import random
import os
import re
import subprocess
from appium import webdriver
from Peiyinxiu_Client import Test3
# import time
# from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

# from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
# 获取当前项目的根路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

devs = Test3.get_conn_dev()

def get_version():
    version = []
    for i in range(len(devs)):
        platformVersion = os.popen('adb -s %s shell getprop ro.build.version.release'%devs[i]).read()
        PV = re.sub('\r|\n','',platformVersion)
        version.append(PV)
    return version



def start_APP():
    for dev in range(len(devs)):
        D = devs[dev]
        PV = get_version()[dev]
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = D
        desired_caps['udid'] = D
        desired_caps['platformVersion'] = PV
        desired_caps['appPackage'] = 'com.happyteam.dubbingshow'
        desired_caps['appActivity'] = 'ui.StartActivity'
        desired_caps['appWaitPackage'] = 'com.happyteam.dubbingshow'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['ignoreUnimportantViews'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['newCommandTimeout'] = 10000
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['systemPort'] = 8200
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.launch_app()


# def devices_test():
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['deviceName'] = '6c77030'
#     desired_caps['udid'] = '6c77030'
#     desired_caps['platformVersion'] = '7.1.1'
#     desired_caps['appPackage'] = 'com.happyteam.dubbingshow'
#     desired_caps['appActivity'] = 'ui.StartActivity'
#     desired_caps['appWaitPackage'] = 'com.happyteam.dubbingshow'
#     desired_caps['noReset'] = True
#     desired_caps['unicodeKeyboard'] = True
#     desired_caps['ignoreUnimportantViews'] = True
#     desired_caps['dontStopAppOnReset'] = True
#     desired_caps['newCommandTimeout'] = 10000
#     desired_caps['automationName'] = 'UiAutomator2'
#     desired_caps['systemPort'] = 8112
#     try:
#         driver = webdriver.Remote('http://localhost:4720/wd/hub', desired_caps)
#         return driver
#     except:
#         print('NO driver!!')

if __name__=="__main__":
    Test3.start_server()
    start_APP()