#coding=utf-8
import unittest
import random
import pytest
import time
import re
from collections import Counter
from Dubbing9_11.Front import Dubbing
sourced_id = 'com.happyteam.dubbingshow:id/'

class Test_a_Live_notice(Dubbing):
    #首页关注主界面中的语聊通知
    def test_a(self):
        self.driver.wait_id(soucred_id + 'task_box')
        self.driver.find_id(sourced_id + 'ivCirclesTab').click()
        self.driver.wait_id(sourced_id + 'musicPlayView')
        self.driver.find_id(sourced_id + 'musicPlayView').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('你关注的秀友都还没有创建房间哦')
        except:
            pass
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
    #关注主播后查看通知列表
    def test_b(self):
        self.driver.find_id(sourced_id + '')




if __name__ == '__main__':
    unittest.main()
