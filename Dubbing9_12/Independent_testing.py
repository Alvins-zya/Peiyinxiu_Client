# coding = utf-8
import time
import unittest
import random
import datetime
import pytest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Dubbing9_11.Front import Dubbing

soucred_id = 'com.happyteam.dubbingshow:id/'

#视频详情界面视频切换
class Test(Dubbing):
    def test1(self):
        while True:
            time.sleep(10)
            title = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
            self.driver.swip_up()
            time.sleep(2)
            self.driver.wait_id(soucred_id + 'tv_video_detail_title')
            time.sleep(10)
            title1 = self.driver.find_id(soucred_id + 'tv_video_detail_title').text
            if title == title1:
                self.driver.find_id(soucred_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(soucred_id + 'film_img2').click()
                self.driver.wait_id(soucred_id + 'tv_video_detail_title')
            time.sleep(2)

if __name__=='__main__':
    unittest.main()
