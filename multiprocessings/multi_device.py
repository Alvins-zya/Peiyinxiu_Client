#coding=utf-8
'''
Created on 2020年2月8日
@author:Alvin_zhu
appium 自动化测试-多进程并发测试
'''
from appium import webdriver
import yaml
import multiprocessing

from time import ctime

with open('devices_caps.yaml', 'r')as file:
    data = yaml.load(file,Loader=yaml.FullLoader)
    print(data)

devices_list = ['4ebc78fd', 'f249f9f2']
#
# def appium_desired(udid,port):
#     desired_caps = {}
#
#     desired_caps['platformName'] = data['platformName']
#     desired_caps['platformVersion'] = data['platformVersion']
#     desired_caps['deviceName'] = data['deviceName']
#     desired_caps['udid'] = udid
#     desired_caps['appPackage'] = data['appPackage']
#     desired_caps['appActivity'] = data['appActivity']
#     desired_caps['noReset'] = data['noReset']
#     desired_caps['ignoreUnimportantViews'] = True
#     desired_caps['dontStopAppOnReset'] = True
#     desired_caps['newCommandTimeout'] = 10000
#     desired_caps['automationName'] = 'Uiautomator2'
#     desired_caps['systemPort'] = 8100
#     print('appium port: %s start run %s at %s' % (port, udid ,ctime()))
#
#     driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) +'/wd/hub', desired_caps)
#
#     return driver

# desired_process = []
#
# for i in range(len(devices_list)):
#     port = 4723 + 2 *i
#
#     desired = multiprocessing.Process(target= appium_desired, args= (devices_list[i],port))
#
#     desired_process.append(desired)
#
#
# if __name__=="__main__":
#     for desired in desired_process:
#         desired.start()
#
#     for desired in desired_process:
#         desired.join()