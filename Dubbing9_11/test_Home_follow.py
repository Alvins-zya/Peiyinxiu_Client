#coding=utf-8
import unittest
import random
import pytest
import time
import re
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from collections import Counter
from Dubbing9_11.Front import Dubbing
sourced_id = 'com.happyteam.dubbingshow:id/'

class Test_a_Follow(Dubbing):
    #首页关注主界面中的语聊通知
    def test_a(self):
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(sourced_id + 'task_box')
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
        self.driver.find_id(sourced_id + 'ivDubbingTab').click()
        time.sleep(2)
        while True:
            try:
                self.driver.find_xpath('语聊')
                break
            except:
                if self.y == 1920:
                    self.driver.swip_move(self.x * 0.854 ,self.y * 0.189,self.x * 0.249,self.y *0.197)
                    time.sleep(2)
                else:
                    pass
        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tab2').click()
        time.sleep(2)
        self.driver.wait_id(sourced_id + 'item_title1')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'item_title1').click()
        self.driver.wait_id(sourced_id + 'user_list')
        time.sleep(2)
        try:
            self.driver.find_xpath('拒绝')
            self.driver.find_xpath('拒绝').click()
        except:
            pass
        time.sleep(2)
        el = self.driver.find_id(sourced_id + 'userhead')
        self.driver.Long_Touche(el)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btn_follow').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'icon_close').click()
        time.sleep(2)
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(sourced_id + 'tvCirclesTab')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tvCirclesTab').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'musicPlayView').click()
        time.sleep(2)
        self.driver.wait_download(sourced_id + 'live_icon')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'rl').click()
        self.driver.wait_download(sourced_id + 'linear_rank')
        time.sleep(2)
        try:
            self.driver.find_xpath('拒绝')
            self.driver.find_xpath('拒绝').click()
        except:
            pass
        time.sleep(2)
        el = self.driver.find_id(sourced_id + 'userhead')
        self.driver.Long_Touche(el)
        time.sleep(2)
        text = self.driver.find_id(sourced_id +'btn_follow').text
        check = '取消关注'
        if text == check:
            self.driver.find_id(sourced_id + 'btn_follow').click()
            time.sleep(2)
        else:
            pass
        self.driver.find_id(sourced_id + 'icon_close').click()
        time.sleep(2)
        self.driver.close_app()
        time.sleep(2)
        self.driver.lanuch_app()
        self.driver.wait_id(sourced_id + 'ivDubbingTab')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'ivCirclesTab').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'musicPlayView').click()
        time.sleep(4)
        try:
            self.driver.find_id(sourced_id + 'live_icon')
            raise ('取消主播关注后依然显示该主播的关注状态')
        except:
            pass
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    #首页关注列表
    def test_c(self):
        name = self.driver.find_id(sourced_id + 'textView').text
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_follow')
        Name = self.driver.find_id(sourced_id + 'username').text
        self.assertEqual(name,Name,msg='关注列表用户名称与空间用户名称不一致')
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
    #视频播放
    def test_d(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'play')
                self.driver.find_id(sourced_id + 'play').click()
                self.driver.wait_download(sourced_id + 'play')
                time.sleep(2)
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        while True:
            try:
                self.driver.find_id(sourced_id + 'content').click()
                try:
                    self.driver.wait_id(sourced_id + 'tv_video_detail_title')
                    self.driver.find_id(sourced_id + 'btnBack').click()
                    time.sleep(2)
                    break
                except:
                    self.driver.find_id(sourced_id + 'btnBack').click()
                    time.sleep(2)
                    self.driver.swip_up()
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)

    #关注界面作品分享
    def test_e(self):
        count =  self.driver.find_id(sourced_id + 'item_attention_share_num').text
        self.driver.find_id(sourced_id + 'item_attention_share_num').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x *0.129,self.y * 0.664)
        else:
            pass
        time.sleep(2)
        self.driver.wait_id('com.tencent.mm:id/ch')
        self.driver.find_id('com.tencent.mm:id/ch').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
        except:
            raise ('未检测到分享后的toast提示')
        time.sleep(2)
        count1 = self.driver.find_id(sourced_id + 'item_attention_share_num').text
        self.assertNotEqual(count,count1,msg='分享成功后分享数量未变化')
        time.sleep(2)

    # 转发作品
    def test_f(self):
        self.driver.find_id(sourced_id + 'ivDubbingTab').click()
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'film_img2').click()
        self.driver.wait_id(sourced_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'share').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.873, self.y * 0.812)
        else:
            pass
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'reprint')
        except:
            if self.y == 1920:
                self.driver.tap(self.x * 0.685, self.y * 0.812)
            else:
                pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content').send_keys('日常转发')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'reprint').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check, toast, msg='转发失败')
        except:
            raise ('未检测到转发toast提示')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tvCirclesTab').click()
        time.sleep(2)
        while True:
            self.driver.swip_down()
            time.sleep(2)
            try:
                self.driver.find_xpath('日常转发')
                break
            except:
                pass
        time.sleep(2)

    #作品下载本地
    def test_g(self):
        while True:
            while True:
                try:
                    self.driver.find_id(sourced_id + 'item_attention_share_num')
                    self.driver.find_id(sourced_id + 'item_attention_share_num').click()
                    break
                except:
                    self.driver.swip_up()
                    time.sleep(2)
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.31,self.y * 0.807)
            else:
                pass
            #先判断点击是否为下载按钮，若是复制按钮则会toast提示，不是复制按钮则判断是否有非会员弹窗，不是则直接等待作品下载完成
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '存在'
                if check in toast:
                    break
                else:
                    pass
            except:
                try:
                    self.driver.find_xpath('直接下载')
                    self.driver.find_xpath('直接下载').click()
                    self.driver.wait_id(sourced_id + 'btnSubmit')
                    self.driver.find_id(sourced_id + 'btnSubmit').click()
                    break
                except:
                   try:
                        self.driver.wait_id(sourced_id + 'btnSubmit')
                        self.driver.find_id(sourced_id + 'btnSubmit').click()
                        break
                   except:
                       pass
            self.driver.swip_up()
            time.sleep(2)

    #关注界面送礼
    def test_h(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'item_attention_praise')
                self.driver.find_id(sourced_id + 'item_attention_praise').click()
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(4)
        self.driver.find_id(sourced_id + 'confirm').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.swip_up()
        time.sleep(2)

    #关注界面评论作品
    def test_i(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'item_attention_comment_count')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'item_attention_comment_count').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'editContent').send_keys('日常评论下！^.^')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btn_send').click()
        try:
            toast =  self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='关注界面发送评论提示校验不一致')
        except:
            raise ('未检测到评论发送toast提示')
        time.sleep(2)

    #关注界面素材预览-配音
    def test_j(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'action')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'play')
            self.driver.find_id(sourced_id + 'play').click()
            self.driver.wait_download(sourced_id + 'play')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'action').click()
        while True:
            try:
                self.driver.find_id(sourced_id + 'btnSubmit')
                self.driver.find_id(sourced_id + 'btnSubmit').click()
                try:
                    self.driver.find_id(sourced_id + 'roleall')
                    self.driver.find_id(sourced_id + 'roleall').click()
                except:
                    pass
                break
            except:
                try:
                    self.driver.find_id(sourced_id + 'roleall')
                    self.driver.find_id(sourced_id + 'roleall').click()
                    break
                except:
                    pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)

    #关注界面特别关注
    def test_k(self):
        while True:
            try:
                self.driver.find_id(sourced_id + 'more')
                break
            except:
                self.driver.swip_up()
                time.sleep(2)
        time.sleep(2)
        #用户动态开关
        self.driver.find_id(sourced_id + 'more').click()
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x *0.5,self.y *0.794)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'check').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        #特别关注
        self.driver.find_id(sourced_id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        else:
            pass
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='特别关注toast提示检验失败')
        except:
            raise ('未检测到特别关注toast提示')
        time.sleep(2)
        while True:
            self.driver.swip_down()
            time.sleep(2)
            try:
                self.driver.find_id(sourced_id +'rl')
                break
            except:
                pass
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'rl').click()
        time.sleep(2)
        self.driver.wait_id(sourced_id + 'userhead')
        time.sleep(2)
        name = self.driver.find_id(sourced_id +'textView').text
        time.sleep(2)
        self.driver.find_id(sourced_id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.864)
        else:
            pass
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '取消'
            self.assertIn(check, toast, msg='取消特别关注toast提示检验失败')
        except:
            raise ('未检测到特别关注toast提示')
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_xpath(name)
            raise ('特别关注取消特别关注后刷新界面依然显示用户信息')
        except:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
