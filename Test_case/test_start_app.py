#coding=utf-8
'''
启动APP
'''
from Thread_script.Driver_Operate import BaseOperate
import time
class Test():
    def __init__(self,udid,port,systemport):
        self.drivers = BaseOperate(udid,port,systemport)

    def start_app(self):
        self.drivers.lanuch_app()
        time.sleep(3)
        self.drivers.close_app()
        print('===结束===')


