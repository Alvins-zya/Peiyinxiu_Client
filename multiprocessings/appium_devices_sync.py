#coding=utf-8
'''
create on 2020年2月9日
@author: Alvin_zhu
'''
from multiprocessings.mulit_appium import appium_start
from multiprocessings.multi_devices_sync import appium_desired
from multiprocessings.check_port import *
from time import sleep
import multiprocessing

devices_list = ['4ebc78fd', 'f249f9f2']

def start_appium_action(host,port,udid):


    if check_port(host,port):

        appium_start(host,port,udid)

        return True

    else:

        print('appium %s start failed!' % port)

        return False

def appium_start_sync():

    appium_process = []

    for i in range(len(devices_list)):
        host = '127.0.0.1'

        port = 4723 +2*i

        appium = multiprocessing.Process(target=start_appium_action,args=(host,port,devices_list[i]))

        appium_process.append(appium)

    for appium in appium_process:
        appium.start()

    for appium in appium_process:
        appium.join()

    sleep(2)

def start_devices_action(udid,port):

    appium_desired(udid,port)

def devices_start_sync():

    print('==devices_start==')

    desiried_process = []

    for i in range(len(devices_list)):

        port = 4723 + 2 * i

        desired = multiprocessing.Process(target= start_devices_action, args=(devices_list[i],port))

        desiried_process.append(desired)

    for desired in desiried_process:
        desired.start()

    for desired in desiried_process:
        desired.join()


if __name__=='__main__':
    # appium_start_sync()

    devices_start_sync()

