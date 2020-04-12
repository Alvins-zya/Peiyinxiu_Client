import time
import os
import unittest
import HTMLTestRunner
import warnings

from operate.Driver_Operate import BaseOperate
import logging
from time import sleep
soucred_id = 'com.happyteam.dubbingshow:id/'
class Dubbing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = BaseOperate()
        self.driver.wait_id(soucred_id + 'task_box')
        self.driver.find_id(soucred_id + 'btn_more').click()
        self.driver.wait_id(soucred_id + 'unlimited')
        self.driver.find_id(soucred_id + 'unlimited').click()
        time.sleep(2)
        self.driver.find_xpath('推荐').click()
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.wait_id(soucred_id + 'iv_source')
        except:
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(soucred_id + 'iv_source').click()
        self.driver.wait_id(soucred_id + 'userhead')
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        print('===测试结束===')


