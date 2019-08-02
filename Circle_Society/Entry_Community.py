#coding = utf-8
#防止中文显示乱码
#coding = gb18030
import time
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from Peiyinxiu_Client.Operate import BaseOperate
from Peiyinxiu_Client.devices import device
from pprint import pprint
OP = BaseOperate()
x = OP.touch()[0]
y = OP.touch()[1]
devc = device()


'''社区'''
def Communitys():
    OP.wait_id('com.happyteam.dubbingshow:id/newsTab')
    print("点击首页-社区")
    OP.find_id('com.happyteam.dubbingshow:id/newsTab').click()
    try:
        OP.wait_id('com.happyteam.dubbingshow:id/userhead')
    except(TimeoutException,NoSuchElementException):
        try:
            OP.find_id('com.happyteam.dubbingshow:id/btnReload')
            time.sleep(1)
            OP.find_id('com.happyteam.dubbingshow:id/btnReload').click()
            OP.wait_id('com.happyteam.dubbingshow:id/userhead')
            try:
                OP.find_id('com.happyteam.dubbingshow:id/btnReload')
                print('圈子主界面重载失败')
                devc.close_app()
            except:
                pass
        except:
            pass
    time.sleep(2)