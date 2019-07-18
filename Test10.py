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



