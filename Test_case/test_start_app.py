#coding=utf-8
'''
启动APP
'''
from Thread_script.Driver_Operate import BaseOperate
import time
class Test():
    def __init__():
        self.driver = BaseOperate()

    def start_app():
        self.driver.lanuch_app()
        time.sleep(3)
        self.driver.close_app()
        print('===结束===')

