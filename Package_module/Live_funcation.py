#coding=utf-8
from Public.Driver_Operate import BaseOperate,resource_id
import time
class Live_funcation():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #进入语聊间
    def Into_live_detail(self):
        self.driver.find_id(self.id + 'fram').click()
        self.driver.wait_id(self.id + 'name')

    #退出语聊间
    def out_live(self):
        self.driver.find_id(self.id + 'home_close').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'fram')
        time.sleep(1)


