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

    def test1_touche_dubbing(self):
        try:
            self.driver.find_id(soucred_id + 'yinpin')
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_id(soucred_id + 'roleall')
            self.driver.find_id(soucred_id + 'roleall').click()
        except:
            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            self.driver.wait_id(soucred_id + 'living')

    def test2_guidance(self):
        try:
            self.driver.find_id(soucred_id + 'subtitleView').click()
        except:
            pass

    def test3_jurisdiction(self):
        #录音权限
        self.driver.find_id(soucred_id + 'action').click()
        time.sleep(2)
        try:
            self.driver.find_id(soucred_id + 'next')
            self.driver.find_id(soucred_id + 'next').click()
            time.sleep(2)
            try:
                self.driver.wait_sys('始终允许')
            except:
                self.driver.wait_sys('允许')
        except:
            pass
        time.sleep(2)

    def test4_action(self):
        try:
            self.driver.find_id(soucred_id + 'play')
            self.driver.find_id(soucred_id + 'action').click()
        except:
            pass

    def test5_preview(self):
        #配音预览界面
        self.driver.wait_download(soucred_id + 'title')
        self.driver.Background()
        time.sleep(2)

    def test6_complete(self):
        self.driver.find_xpath('完成').click()
        self.driver.wait_id(soucred_id + 'txtTitle')
        time.sleep(2)

    def test7_privacy(self):
        #私密开关
        self.driver.find_id(soucred_id + 'pri_switch_tv').click()
        time.sleep(2)

    def test8_upload(self):
        self.driver.find_id(soucred_id + 'uploadbtn').click()
        time.sleep(2)
    def test9_over(self):
        self.driver.wait_id(soucred_id + 'down')
        print('上传成功')

    @classmethod
    def tearDownClass(self):
        print('===测试结束===')



if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(Dubbing))
    runner = unittest.TextTestRunner()
    runner.run(suite)