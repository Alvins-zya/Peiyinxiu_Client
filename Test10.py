# -*- coding:utf-8 -*-
from appium import webdriver
import subprocess
import time
import os
import re
import yaml
# import login_Activity
import threading
from selenium.webdriver.support.ui import WebDriverWait


PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'h'
# desired_caps['app'] = PATH('C:\\Users\\butel\\Desktop\\hvs_s175_v2.6.68.310-201709111846.apk')
desired_caps['appPackage'] = 'com.happyteam.dubbingshow'
desired_caps['appActivity'] = 'ui.StartActivity'
desired_caps['appWaitPackage'] = 'com.happyteam.dubbingshow'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'


def get_conn_dev():
    p = os.popen('adb devices')
    outstr = p.read()
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid

subprocess.call('start /b taskkill /f /t /im node.exe', shell=True, stdout=open('E:\log', 'w'), stderr=subprocess.STDOUT)
ip = get_conn_dev()
tt = []


def sever(ip):
    for i in range(len(ip)):
        host = '127.0.0.1'
        cmd = 'appium -a ' + host + ' -p ' + str(4723 + 2 * i) + ' -U ' + ip[i]
        print (cmd)
        time.sleep(2)
        # 注释掉的
        # subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.call(cmd, shell=True, stdout=open('E:\log', 'w'), stderr=subprocess.STDOUT)
        time.sleep(5)
        driver = webdriver.Remote('http://localhost:' + str(4723 + 2 * i) + '/wd/hub', desired_caps)
        hh = Ni(driver)
        t = threading.Thread(target=hh.login)
        tt.append(t)




class Ni():
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        time.sleep(5)
        print(111111111)
        self.driver.quit()


if __name__ == '__main__':
    sever(ip)
    time.sleep(2)
    for i in tt:
        i.start()

