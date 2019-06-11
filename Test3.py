#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import random,os
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
'''R11'''
#获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={
                'platformName': 'Android',
                'deviceName': '6c77030',
                'udid': '6c77030',
                'platformVersion': '7.1.1',
                'appPackage': 'com.happyteam.dubbingshow',
                'appActivity': 'ui.StartActivity',
                'noReset': True,
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'newCommandTimeout': 300,
                'dontStopAppOnReset': True,
                'automationName': 'UiAutomator2'
                # 'systemPort' : '8080'
              }

#启动APP
driver = webdriver.Remote('http://localhost:4790/wd/hub',desired_caps)

def result():
    driver.launch_app()
    try:
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('com.happyteam.dubbingshow:id/task_box'))
        os.system('adb -s 6c77030  shell am force-stop com.happyteam.dubbingshow')
        return True
    except(NoSuchElementException,TimeoutException):
        os.system('adb -s 6c77030 shell am force-stop com.happyteam.dubbingshow')
        return False
    time.sleep(1)

def Test():
    for i in range(200):
        print(i,result())



if __name__=="__main__":
    Test()