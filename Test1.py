#coding = utf-8
#防止中文显示乱码
#coding = gb18030

import random,os
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoAlertPresentException,TimeoutException,NoSuchElementException
'''MI8'''
#获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

from devices import devices_test
# from Operate import BaseOperate
# OP = BaseOperate()
# device().launch_app()
dev = devices_test()
dev.launch_app()
time.sleep(2)
i = 1
while i ==True:
    dev.find_element_by_id('com.happyteam.dubbingshow:id/editContent').send_keys('ha')
    time.sleep(2)
    dev.find_element_by_id('com.happyteam.dubbingshow:id/btn_send').click()
    WebDriverWait(dev,30).until_not(lambda x:dev.find_element_by_id('com.happyteam.dubbingshow:id/btn_send'))
    time.sleep(3)





