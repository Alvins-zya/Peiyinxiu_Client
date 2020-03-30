#coding = utf-8
from Dubbing_910.operate.Driver_Operate import BaseOperate
import time
ID = 'com.happyteam.dubbingshow:id/'
class Login():
    def __init__(self,udid,port,systemport):
        self.D = BaseOperate(udid,port,systemport)

    def start_app(self):
        self.D.wait_id(ID+'task_box')
        print("==开始==")

    def login(self):
        self.D.find_id(ID+'ivMineTab').click()
        time.sleep(2)
        self.D.find_id(ID+'username').click()
        time.sleep(2)
        self.D.find_xpath('配音秀登录')
        time.sleep(2)
        # 点击地区进入国家列表
        self.D.find_id(ID + 'zone_tv').click()
        time.sleep(2)
        try:
            self.D.wait_id(ID + 'code')
        except:
            self.D.find_id(ID + 'btnReload')
            time.sleep(2)
            self.D.find_id(ID + 'btnReload').click()
            time.sleep(2)
        self.D.find_id(ID + 'edit_text').click()
        self.D.find_id(ID + 'edit_text').send_keys('zg')
        time.sleep(1)
        self.D.find_id(ID + 'btn_search').click()
        self.D.wait_xpath('中国')
        self.D.find_id(ID + 'code').click()
        time.sleep(2)
        



