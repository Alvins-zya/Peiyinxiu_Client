#coding=utf-8
'''
Created on 2020年2月8日
@author:Alvin_zhu
appium 自动化测试-多进程并发测试
'''
from appium import webdriver
from time import ctime
import os

def appium_desired(udid,port,systemport):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = udid
    desired_caps['udid'] = udid
    # desired_caps['deviceName'] = 'b490dce3'
    # desired_caps['udid'] = 'b490dce3'
    desired_caps['appPackage'] = 'com.happyteam.dubbingshow'
    desired_caps['appActivity'] = 'ui.StartActivity'
    desired_caps['noReset'] = True
    desired_caps['ignoreUnimportantViews'] = True
    desired_caps['dontStopAppOnReset'] = True
    desired_caps['newCommandTimeout'] = 10000
    desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['unicodeKeyboard'] = True     #Android8.1系统不支持此项设置,运行是报错：io.appium.settings/.UnicodeIME' exited with code 137'; Stderr: ''; Code: '13
    desired_caps['resetKeyboard'] = True
    desired_caps['normalizeTagNames'] = True
    desired_caps['systemPort'] = systemport
    print('appium port: %s start run %s at %s' % (port, udid ,ctime()))
    driver = webdriver.Remote('http://localhost: %s /wd/hub'%(port), desired_caps )
    return driver

