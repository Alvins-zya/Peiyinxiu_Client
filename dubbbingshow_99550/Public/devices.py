#coding=utf-8
'''
Created on 2020年2月8日
@author:Alvin_zhu
appium 自动化测试-多进程并发测试
'''
from appium import webdriver
import yaml
from time import ctime

with open('D:\GIT\Peiyinxiu_Client\dubbbingshow_99550\Public\devices_caps.yaml', 'r')as file:
    data = yaml.load(file,Loader=yaml.FullLoader)


def appium_desired(udid,port):
    desired_caps = {}

    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = udid
    desired_caps['udid'] = udid
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['ignoreUnimportantViews'] = True
    desired_caps['dontStopAppOnReset'] = True
    desired_caps['newCommandTimeout'] = 10000
    desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['systemPort'] = 8100
    print('appium port: %s start run %s at %s' % (port, udid ,ctime()))

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) +'/wd/hub', desired_caps)
    return driver


