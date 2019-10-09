import os
import time
from appium.webdriver.common.touch_action import TouchAction
from Peiyinxiu_Client.devices import device,dev
from Peiyinxiu_Client.Operate import BaseOperate

OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
touch = device()
D = dev

