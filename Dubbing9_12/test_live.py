# coding = utf-8
import time
import unittest
import random
import datetime
import pytest
import sys
import os,threading
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Dubbing9_11.Front import Dubbing

soucred_id = 'com.happyteam.dubbingshow:id/'


class Test_a_Dub(Dubbing):
    #进入素材库
    def test0(self):
        while True:
            self.driver.wait_id(soucred_id + 'btn_more')
            self.driver.find_id(soucred_id + 'btn_more').click()
            self.driver.wait_id(soucred_id + 'coor')
            self.driver.find_id(soucred_id + 'coor').click()
            time.sleep(2)
            self.driver.swip_down()
            time.sleep(2)
            try:
                self.driver.wait_id(soucred_id + 'iv_source')
            except:
                self.driver.swip_down()
            time.sleep(3)
            while True:
                self.driver.find_id(soucred_id + 'iv_source').click()
                try:
                    self.driver.wait_id(soucred_id + 'userhead')
                    self.driver.Background()
                    time.sleep(2)
                    break
                except:
                    self.driver.back()
                    time.sleep(2)
            time.sleep(4)

            self.driver.find_id(soucred_id + 'dubbing_fake').click()
            time.sleep(2)
            try:
                self.driver.find_id(soucred_id + 'next')
                tip = self.driver.find_id(soucred_id + 'txtTitle').text
                check = '为了您正常使用配音秀 需获得以下权限'
                self.assertEqual(tip, check, msg='内存权限文案不一致')
                self.driver.find_id(soucred_id + 'close').click()
                time.sleep(2)
                try:
                    self.driver.find_id(soucred_id + 'dubbing_fake')
                    self.driver.find_id(soucred_id + 'dubbing_fake').click()
                    time.sleep(3)
                    self.driver.find_id(soucred_id + 'next')
                    self.driver.find_id(soucred_id + 'next').click()
                    time.sleep(2)
                    try:
                        self.driver.wait_sys('始终允许')
                    except:
                        self.driver.wait_sys('允许')
                except:
                    print('未返回到素材预览界面')
                    self.driver.Quit()
            except:
                pass
            self.driver.wait_id(soucred_id + 'roleall')
            self.driver.find_id(soucred_id + 'roleall').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'action').click()
            self.driver.wait_download(soucred_id + 'title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_xpath('完成').click()
            self.driver.wait_id(soucred_id + 'txtTitle')
            time.sleep(2)
            self.driver.find_id(soucred_id + 'pri_switch_tv').click()
            time.sleep(2)
            self.driver.find_id(soucred_id + 'uploadbtn').click()
            time.sleep(2)
            while True:
                try:
                    toast = self.driver.wait_toast('//android.widget.Toast')
                    print(toast)
                    break
                except:
                    try:
                        self.driver.find_id(soucred_id + 'wx')
                        self.driver.find_id(soucred_id + 'img_url').click()
                        self.driver.wait_id(soucred_id + 'btnBack')
                        time.sleep(10)
                        self.driver.Background()
                        time.sleep(2)
                        self.driver.find_id(soucred_id + 'btnBack').click()
                        time.sleep(2)
                        break
                    except:
                        try:
                            self.driver.find_id(soucred_id + 're_update')
                            break
                        except:
                            pass
            time.sleep(2)


if __name__ == "__main__":
    unittest.main()
