#coding = utf-8
#防止中文显示乱码
#coding = gb18030
import random
import os
from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException
#获取当前项目的根路径
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
from pprint import pprint
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()

time.sleep(2)
local = OP.find_id('com.happyteam.dubbingshow:id/periscope_view').location
loc_x = int (local['x'])
loc_y = int (local['y'])+100
for i in range(200):
    TouchAction(devc).press(x=loc_x,y=loc_y).release().perform()
    time.sleep(0.1)
time.sleep(2)