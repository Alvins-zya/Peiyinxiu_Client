
import unittest
import random
import pytest
import time
import re
from Dubbing9_11.Front import Dubbing
sourced_id = 'com.happyteam.dubbingshow:id/'

class Test_a_Person_center(Dubbing):
    #首页进入“我的”界面
    def test_a(self):
        self.driver.wait_id(sourced_id + 'ivMineTab')
        self.driver.find_id(sourced_id + 'ivMineTab').click()
        self.driver.find_id(sourced_id + 'username')
        time.sleep(2)

    #我的界面点击头像进入个人空间
    def test_b(self):
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'followcount')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #我的界面点击关注进入关注列表
    def test_c(self):
        follow_count = self.driver.find_id(sourced_id +'followed_count').text
        time.sleep(1)
        self.driver.find_id(sourced_id + 'followed_count').click()
        self.driver.wait_id(sourced_id  + 'filter_edit')
        time.sleep(2)
        if follow_count >9:
            pass
        else:
            follow_count1 = self.driver.find_id(sourced_id + 'username')
            self.assertEqual(len(follow_count1),follow_count,msg='我的界面关注数与关注列表关注用户量不一致')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #我的界面点击粉丝进入粉丝列表
    def test_d(self):
        fan_count = self.driver.find_id(sourced_id + 'fans_count').text
        time.sleep(1)
        self.driver.find_id(sourced_id + 'fans_count').click()
        self.driver.wait_id(sourced_id + 'vip_tag')
        time.sleep(2)
        if fan_count > 8:
            pass
        else:
            fan_count1 = self.driver.find_id(sourced_id + 'username')
            self.assertEqual(len(fan_count1),fan_count,msg='我的界面粉丝数量与粉丝列表界面粉丝数量不一致')
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #用户ID
    def test_e(self):
        ID = self.driver.find_id(sourced_id + 'tv_uid').text
        check = 148556194
        self.assertIn(check,ID,msg='用户ID检验不一致')
        time.sleep(2)

class Test_b_Person_Zoom(Dubbing):
    #点击头像进入个人空间
    def test_a(self):
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'followcount')
        time.sleep(2)

    #个人空间搜索-作品
    def test_b(self):
        self.driver.find_id(sourced_id +'photo').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'txtKeyword').send_keys('白居易')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSearch').click()
        self.driver.wait_id(sourced_id + 'filmBg')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'filmBg').click()
        self.driver.wait_id(sourced_id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #个人空间搜索——作品搜索记录
    def test_c(self):
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'photo').click()
        self.driver.wait_id(sourced_id + 'txtKeyword')
        try:
            self.driver.find_id(sourced_id + 'clear')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'clear').click()
            time.sleep(2)
            try:
                self.driver.find_id(sourced_id + 'clear')
                raise ('个人空间搜索作品后，点击清空搜索记录，依然显示有搜索记录')
            except:
                pass
        except:
            raise ('个人空间搜索作品后退出再进，未显示作品搜索历史记录')
        time.sleep(2)

    #个人空间搜索——作品搜索无结果显示
    def test_d(self):
        self.driver.find_id(sourced_id + 'txtKeyword').send_keys('配音秀')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSearch').click()
        try:
            self.driver.wait_xpath('没有搜到任何内容')
        except:
            raise ('作品搜索无结果时未显示任何提示信息')
        time.sleep(2)

    #个人空间搜索-素材
    def test_e(self):
        self.driver.find_id(sourced_id + 'll_source').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'txtKeyword').send_keys('配音秀')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSearch').click()
        try:
            self.driver.wait_xpath('没有搜到任何内容')
        except:
            raise ('素材搜索无结果时未显示任何提示信息')
        time.sleep(2)

    #个人空间—搜索-搜索个人素材
    def test_f(self):
        self.driver.find_id(sourced_id + 'll_source').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'txtKeyword').send_keys('基督教')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSearch').click()
        self.driver.wait_id(sourced_id + 'iv_source')
        name = self.driver.find_id(sourced_id + 'tv_source_title').text
        check = '基督教'
        self.assertIn(check,name,msg='搜索结果的素材标题中未包含有搜索关键字')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tv_source_title').click()
        self.driver.wait_id(sourced_id + 'userhead')
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #编辑资料
    def test_g(self):
        self.driver.find_id(sourced_id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.719)
        else:
            pass
        time.sleep(4)
        try:
            self.driver.find_xpath('个人资料')
        except:
            raise ('未跳转到个人资料界面')
        time.sleep(2)
    #更换头像
    def test_h(self):
        #点击头像-拍照
        self.driver.find_id(sourced_id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x *0.5,self.y * 0.793)
        else:
            pass
        time.sleep(2)
        '''
        以下操作只适用VIVOx9
        '''
        self.driver.wait_id('com.android.camera:id/shutter_button')
        self.driver.find_id('com.android.camera:id/shutter_button').click()
        time.sleep(4)
        self.driver.find_id('com.android.camera:id/done_button').click()
        time.sleep(4)
        self.driver.find_id(sourced_id + 'confirm').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '修改成功'
            self.assertEqual(toast,check,msg='拍照替换头像toast提示内容校验不一致')
        except:
            raise ('拍照更换头像未检测到toast提示')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.869)
        else:
            pass
        time.sleep(2)
        self.driver.find_xpath('阅图').click()
        time.sleep(4)
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.182)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'confirm').click()
        try:
            toast1 = self.driver.wait_toast('//android.widget.Toast')
            check1 = '修改成功'
            self.assertEqual(toast1,check1,msg='相册替换头像toast提示内容校验不一致')
        except:
            raise ('相册更换头像未检测到toast提示')
        time.sleep(2)

    #输入个人简介
    def test_i(self):
        self.driver.find_id(sourced_id + 'tv_sign').clear()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tv_sign').send_keys('空空空')
        time.sleep(2)

    #修改性别
    def test_j(self):
        self.driver.find_id(sourced_id + 'tv_gender').click()
        time.sleep(2)
        if self.y ==1920:
            self.driver.tap(self.x * 0.5,self.y * 0.872)
        else:
            pass
        time.sleep(2)

    #修改地区
    def test_k(self):
        area = self.driver.find_id(sourced_id + 'tv_area').text
        self.driver.find_id(sourced_id + 'tv_area').click()
        self.driver.wait_id(sourced_id + 'name')
        areas = self.driver.find_ids(sourced_id + 'name')
        select = random.randint(0,len(areas))
        self.driver.find_ids(sourced_id + 'name')[select].click()
        time.sleep(2)
        area1 = self.driver.find_id(sourced_id + 'tv_area').text
        self.assertNotEqual(area,area1,msg='地区修改前后显示未刷新')
        time.sleep(2)

    #修改生日
    def test_l(self):
        self.driver.find_id(sourced_id + 'tv_time').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.763,self.y * 0.773)
        else:
            pass
        time.sleep(2)

    #用户名敏感词检测
    def test_m(self):
        self.driver.find_id(sourced_id + 'et_nickname').clear()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'et_nickname').send_keys('政府')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tv_right').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '敏感词'
            self.assertIn(check,toast,msg='名称中输入敏感词，toast提示中未包含敏感词提示')
        except:
            raise ('用户名包含有敏感词，点击保存未弹出敏感词toast提示')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'et_nickname').clear()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'et_nickname').send_keys('遗忘的真心伤不起')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'tv_right').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='个人资料保存成功')
        except:
            raise ('未检测到个人资料保存成功的toast提示')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #会员头像挂件
    def test_n(self):
        self.driver.find_id(sourced_id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5 ,self.y * 0.792)
        else:
            pass
        self.driver.wait_id(sourced_id + 'txtTitle')
        count = self.driver.find_ids(sourced_id + 'img')
        for i in reversed(len(count)):
            self.driver.find_ids(sourced_id + 'img')[i].click()
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #会员空间装扮
    def test_o(self):
        self.driver.find_id(sourced_id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.867)
        else:
            pass
        self.driver.wait_id(sourced_id + 'txtTitle')
        time.sleep(2)
        count = self.driver.find_ids(sourced_id + 'img')
        for i in reversed(len(count)):
            self.driver.find_ids(sourced_id + 'img')[i].click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #用户演绎等级
    def test_p(self):
        self.driver.find_id(sourced_id + 'source_level').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'img_vip').click()
        self.driver.wait_id(sourced_id + 'renew')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'guize1').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #身份认证
    def test_q(self):
        self.driver.find_id(sourced_id + 'vip_description').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #粉丝列表
    def test_r(self):
        self.driver.find_id(sourced_id + 'll_fan').click()
        self.driver.find_id(sourced_id + 'vip_tag')
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(sourced_id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(sourced_id + 'iwant').click()
        self.driver.wait_id(sourced_id + 'renew')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #关注列表
    def test_s(self):
        self.driver.find_id(sourced_id + 'll_follow').click()
        self.driver.wait_id(sourced_id + 'status_icon')
        self.driver.find_id(sourced_id + 'username').click()
        self.driver.wait_id(sourced_id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #社团列表
    def test_t(self):
        self.driver.find_id(sourced_id + 'll_society').click()
        self.driver.wait_id(sourced_id + 'status_icon')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(sourced_id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(sourced_id + 'username').click()
        self.driver.wait_id(sourced_id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #作品上榜列表
    def test_u(self):
        self.driver.find_id(sourced_id + 'll_rank').click()
        self.driver.wait_id(sourced_id + 'middle_img')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)

class Test_c_Person_works(Dubbing):
    #作品列表
    def test_a(self):
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'filmBg1').click()
        self.driver.wait_id(sourced_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_follow')
        time.sleep(2)

    #切换作品列表tab
    def test_b(self):
        self.driver.find_id(sourced_id + 'film_all_count').click()
        time.sleep(2)
        count = self.driver.find_ids(sourced_id + 'title')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        for i in range(len(count)-1,-1,-1):
            self.driver.find_id(sourced_id + 'film_all_count').click()
            time.sleep(2)
            self.driver.find_ids(sourced_id + 'title')[i].click()
            time.sleep(2)

    #置顶作品
    def test_b_a(self):
        el = self.driver.find_ids(sourced_id + 'filmBg1')[0]
        self.driver.Long_Touche(el)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.789)
        else:
            pass
        time.sleep(4)
        try:
            self.driver.find_id(sourced_id + 'img')
        except:
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.943)
            else:
                pass
            time.sleep(2)
            self.driver.find_ids(sourced_id + 'filmBg1')[0].click()
            self.driver.wait_id(sourced_id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'setting').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.703)
            else:
                pass
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnSubmit').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
            time.sleep(4)
            el = self.driver.find_ids(sourced_id + 'filmBg1')[0]
            self.driver.Long_Touche(el)
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.789)
            else:
                pass
            time.sleep(4)
            try:
                self.driver.find_id(sourced_id + 'img')
            except:
                raise ('未显示置顶标签')
        time.sleep(2)

    #作品列表界面长按删除作品
    def test_b_b(self):
        el = self.driver.find_ids(sourced_id + 'filmBg1')[0]
        self.driver.Long_Touche(el)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.868)
        else:
            pass
        time.sleep(4)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(4)


    #个人空间-求合作
    def test_c(self):
        self.driver.find_id(sourced_id + 'coor_text').click()
        self.driver.wait_id(sourced_id + 'btnCooperate')
        self.driver.find_id(sourced_id + 'islook').click()
        self.driver.wait_download(sourced_id + 'play')
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnCooperate').click()
        self.driver.wait_download(sourced_id + 'action')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'back').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    #求合作-邀请好友
    def test_d(self):
        el = self.driver.find_id(sourced_id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x* 0.5,self.y * 0.629)
        else:
            self.driver.back()
        self.driver.wait_id(sourced_id + 'socialstatus')
        self.driver.find_id(sourced_id + 'socialstatus').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content').send_keys('给自己的合作！')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'reprint').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '邀请成功'
            self.assertEqual(toast,check,msg='发送邀请后toast内容校验不一致')
        except:
            raise ('发送邀请后未检测到toast提示')
        time.sleep(2)



    #求合作-私密（公开）
    def test_e(self):
        el = self.driver.find_id(sourced_id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.703)
        else:
            self.driver.back()
        time.sleep(2)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = "公开成功"
            self.assertIn(check,toast,msg='求合作私密转公开toast校验不一致')
        except:
            try:
                self.driver.find_id(sourced_id + 'renew')
                time.sleep(2)
                self.driver.find_id(sourced_id + 'btnBack').click()
                time.sleep(2)
                self.driver.back()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    #求合作删除
    def test_f(self):
        el = self.driver.find_id(sourced_id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.857)
        else:
            self.driver.back()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            self.assertIn(check,toast,msg='求合作删除失败')
        except:
            pass
        time.sleep(2)


    #素材-视频预览
    def test_g(self):
        self.driver.find_id(sourced_id +'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'source_text')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'source_text').click()
        self.driver.wait_id(sourced_id + 'imgSource')
        self.driver.find_id(sourced_id + 'imgSource').click()
        self.driver.wait_id(sourced_id + 'right_icon1')
        time.sleep(30)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #素材配音
    def test_h(self):
        self.driver.find_id(sourced_id + 'imgSource').click()
        self.driver.wait_id(sourced_id + 'right_icon1')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'yinpin')
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(sourced_id + 'roleall')
                    break
                except:
                    self.driver.find_id(sourced_id + 'btnSubmit')
                    time.sleep(1)
                    self.driver.find_id(sourced_id + 'btnSubmit').click()
                    break
            self.driver.wait_id(sourced_id + 'roleall')
            self.driver.find_id(sourced_id +'roleall').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(sourced_id +'btnSubmit').click()
            time.sleep(2)
        except:
            self.driver.find_id(sourced_id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(sourced_id + 'action')
                    break
                except:
                    self.driver.find_id(sourced_id + 'btnSubmit')
                    time.sleep(1)
                    self.driver.find_id(sourced_id + 'btnSubmit').click()
                    break
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnSubmit').click()
            time.sleep(2)
        time.sleep(2)

    #更多-转发
    def test_i(self):
        self.driver.find_id(sourced_id + 'more_text').click()
        self.driver.wait_id(sourced_id + 'filmBg')
        name = self.driver.find_id(sourced_id + 'userName').text
        self.driver.find_id(sourced_id + 'filmBg').click()
        self.driver.wait_id(sourced_id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        detail_name = self.driver.find_id(sourced_id + 'textView').text
        self.assertEqual(name,detail_name,msg='转发列表中用户名称与视频详情用户名称不一致')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #作品转发列表——删除作品
    def test_j(self):
        title = self.driver.find_id(sourced_id + 'title').text
        count = self.driver.find_id(sourced_id + 'film_all_count').text
        el = self.driver.find_id(sourced_id + 'filmBg')
        self.driver.Long_Touche(el)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        try:
            self.driver.find_xpath(title)
            raise ('转发作品删除失败')
        except:
            pass
        time.sleep(2)
        count1 = self.driver.find_id(sourced_id + 'film_all_count').text
        self.assertNotEqual(count,count1,msg='转发数量校验失败')
        time.sleep(2)

    #帖子列表
    def test_k(self):
        self.driver.find_id(sourced_id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('帖子').click()
        time.sleep(4)
        self.driver.swip_up()
        time.sleep(2)

    #圈子标签
    def test_l(self):
        try:
            self.driver.find_id(sourced_id + 'tag')
            self.driver.find_id(sourced_id + 'tag').click()
            self.driver.wait_id(sourced_id + 'img_subscribe')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
        except:
            pass

    #帖子详情
    def test_m(self):
        self.driver.find_id(sourced_id + 'content').click()
        self.driver.wait_id(sourced_id + 'right_icon1')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #帖子-转发私信-删除
    def test_n(self):
        self.driver.find_id(sourced_id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5 , self.y * 0.793)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id +'group_chat').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'name').click()
        time.sleep(4)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='帖子删除toast提示校验失败')
        except:
            raise ('帖子删除未检测到toast提示')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'username').click()
        self.driver.wait_id(sourced_id + 'film_all_count')
        self.driver.find_id(sourced_id + 'more_text').click()
        time.sleep(2)

    #语聊列表
    def test_o(self):
        self.driver.find_id(sourced_id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        time.sleep(4)

    #创建合辑
    def test_p(self):
        self.driver.find_id(sourced_id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'content').send_keys('合辑')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'ok').click()
        time.sleep(3)
        try:
            self.driver.find_id(sourced_id + 'choice')
            self.driver.find_id(sourced_id + 'choice').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'tv_right').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '创建成功'
                self.assertEqual(toast,check,msg='合辑创建失败')
                time.sleep(2)
            except:
                pass
        except:
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnSubmit').click()
            time.sleep(2)

    #合辑删除
    def test_q(self):
        self.driver.find_id(sourced_id + 'single_text').click()
        time.sleep(4)
        self.driver.find_id(sourced_id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('合辑').click()
        self.driver.wait_id(sourced_id + 'filmBg')
        el = self.driver.find_id(sourced_id + 'filmBg')
        self.driver.Long_Touche(el)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        else:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='合辑删除失败')
        except:
            pass
        time.sleep(2)

    #退出个人空间
    def test_r(self):
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)


class Test_d_my(Dubbing):
    #我的界面VIP入口
    def test_a(self):
        self.driver.find_id(sourced_id + 'img_vip').click()
        self.driver.wait_id(sourced_id + 'renew')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'right_huiyuan').click()
        self.driver.wait_id(sourced_id + 'renew')
        time.sleep(2)

    #会员权益计算
    def test_b(self):
        self.driver.find_id(sourced_id + 'img_right').click()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'price')
        except:
            raise ('会员权益计算弹窗中未检测到相关控件')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'complete').click()
        time.sleep(2)

    #会员价格
    def test_c(self):
        price = self.driver.find_ids(sourced_id + 'tv_now_money')
        for i in range(len(price)):
            Price = self.driver.find_ids(sourced_id + 'tv_now_money')[i].text
            self.driver.find_ids(sourced_id + 'rl_all')[i].click()
            time.sleep(1)
            self.driver.find_id(sourced_id + 'renew').click()
            time.sleep(2)
            Price_buy = self.driver.find_id(sourced_id + 'tv_money').text
            self.assertIn(Price,Price_buy,msg='价格列表中的价格与确认购买弹窗中的价格校验不一致')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'close_icon').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'cancel').click()
            time.sleep(2)

    # #会员特权
    # def test_d(self):
    #
    # #会员装扮-头饰-空间
    # def test_e(self):


class Test_e_Notices(Dubbing):
    #系统消息
    def test_a(self):
        self.driver.find_id(sourced_id + 'system_notice').click()
        self.driver.wait_id(sourced_id + 'userhead')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_follow')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #礼物消息
    def test_b(self):
        self.driver.find_id(sourced_id + 'gift').click()
        self.driver.wait_id(sourced_id + 'tab1')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_follow')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'head_container').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
            time.sleep(2)
        except:
            self.driver.wait_id(sourced_id + 'tv_video_detail_title')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)


    #礼物消息列表点击关注
    def test_e(self):
        text = self.driver.find_id(sourced_id + 'guanzhu').text
        state = '发私信'
        if text == state:
            self.driver.find_id(sourced_id + 'guanzhu').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.856)
            else:
                pass
            self.driver.wait_id(sourced_id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'follow_status').click()
            time.sleep(4)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
        else:
            self.driver.find_id(sourced_id + 'guanzhu').click()
            time.sleep(2)
        time.sleep(2)

    #上滑礼物消息列表
    def test_f(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)

    #钻石礼物
    def test_g(self):
        self.driver.find_id(sourced_id + 'rl_tag2').click()
        time.sleep(2)

    #礼物消息通知开关
    def test_h(self):
        try:
            self.driver.find_id(sourced_id + 'setPush')
            self.driver.find_id(sourced_id + 'setPush').click()
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #合作消息
    def test_i(self):
        self.driver.find_id(sourced_id + 'textView15').click()
        self.driver.wait_id(sourced_id + 'more')
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_follow')
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)


    #合作配音
    def test_j(self):
        try:
            self.driver.find_xpaths('合作配音')[1].click()
            self.driver.wait_download(sourced_id + 'action')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'back').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnSubmit').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'play').click()
            self.driver.wait_download(sourced_id + 'play')
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)


    #删除合作消息
    def test_k(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(sourced_id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.882)
        else:
            pass
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除合作消息成功'
            self.assertIn(check,toast,msg='合作消息删除失败')
        except:
            raise ('未检测到合作消息删除toast提示')
        time.sleep(2)

    #生成作品
    def test_l(self):
        self.driver.find_id(sourced_id + 'rl_tag2').click()
        time.sleep(2)
        state = self.driver.find_id(sourced_id + 'btnAccept').text
        check = '生成作品'
        if state == check:
            self.driver.find_id(sourced_id + 'btnAccept').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'head_name').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.793)
            else:
                pass
            self.driver.wait_id(sourced_id + 'com.android.camera:id/shutter_button')
            self.driver.find_id(sourced_id + 'com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id(sourced_id + 'com.android.camera:id/done_button').click()
            time.sleep(4)
            self.driver.find_id(sourced_id + 'confirm').click()
            time.sleep(3)
            self.driver.find_id(sourced_id + 'head_name').click()
            time.sleep(2)
            self.driver.tap(self.x * 0.5, self.y * 0.864)
            time.sleep(2)
            self.driver.find_id(sourced_id + 'photo_wall_item_photo').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'confirm').click()
            time.sleep(3)
            self.driver.find_id(sourced_id + 'title').send_keys('功能测试')
            time.sleep(2)
            try:
                self.driver.find_id(sourced_id + 'tv')
                self.driver.find_id(sourced_id + 'tv').click()
                time.sleep(2)
            except:
                pass
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btn_close').click()
            time.sleep(2)
        else:
            pass

    #生成作品tab界面预览视频
    def test_m(self):
        self.driver.find_id(sourced_id + 'play').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            self.assertIn(check,toast,msg='视频详情界面进入失败')
        except:
            self.driver.wait_id(sourced_id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)

    #合作消息设置
    def test_n(self):
        self.driver.find_id(sourced_id + 'right_icon1').click()
        time.sleep(4)
        #获取当前界面所有resourceId,但部分ID不可用，因此无法区分筛选出真正可以点击的ID
        # count = self.driver.search_id()
        # print(count)
        # self.id = re.findall(r'resource-id="com.happyteam.dubbingshow:id/(.*?)"',count)
        # print(self.id)
        self.driver.find_id(sourced_id + 'acceptAll').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'acceptFirends').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'acceptNone').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'clearAllInviter').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)


        for i in count:
            i.click()

    #评论消息-跳转个人空间
    def test_o(self):
        self.driver.find_id(sourced_id + 'textView16').click()
        self.driver.wait_id(sourced_id + 'reply')
        time.sleep(2)
        name = self.driver.find_id(sourced_id + 'textView').text
        time.sleep(2)
        self.driver.find_id(sourced_id + 'userhead').click()
        self.driver.wait_id(sourced_id + 'll_follow')
        time.sleep(2)
        Zoom_name = self.driver.find_id(sourced_id +'username').text
        self.assertEqual(name,Zoom_name,msg='消息中心用户名称与空间用户名称校验不一致')
        time.sleep(2)
        self.driver.find_id(sourced_id + 'btnBack').click()
        time.sleep(2)

    #评论消息-关注
    def test_o_a(self):
        self.driver.find_id(sourced_id + 'guanzhu').click()
        time.sleep(2)
        try:
            self.driver.find_id(sourced_id + 'editContent')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.854)
            else:
                pass
            self.driver.wait_id(sourced_id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'follow_status').click()
            time.sleep(3)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
        except:
            self.driver.find_id(sourced_id + 'guanzhu').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.854)
            else:
                pass
            self.driver.wait_id(sourced_id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'follow_status').click()
            time.sleep(3)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(sourced_id + 'guanzhu').click()
        time.sleep(2)

    #评论消息-进入作品详情
    def test_o_b(self):
        count = self.driver.find_ids(sourced_id + 'content')
        for i in range(len(count)):
            self.driver.find_ids(sourced_id + 'content')[i].click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '删除'
                self.assertIn(check,toast,msg='点击评论跳转视频详情失败')
            except:
                self.driver.wait_id(sourced_id + 'tv_video_detail_title')
                self.driver.Background()
                time.sleep(2)
                self.driver.find_id(sourced_id + 'btnBack').click()
                time.sleep(2)
            time.sleep(2)
        time.sleep(2)

    #评论消息-回复评论
    def test_o_c(self):
        comment = self.driver.find_ids(sourced_id + 'reply_btn')
        for i in range(len(comment)):
            self.driver.find_ids(sourced_id + 'reply_btn')[i].click()
            time.sleep(2)
            self.driver.find_id(sourced_id + 'editContent').send_keys('哈哈哈')
            time.sleep(2)
            self.driver.find_id(sourced_id + 'btn_send').click()
            self.driver.wait_toast('//android.widget.Toast')
            try:
                self.driver.find_id(sourced_id + 'editContent')
                self.driver.back()
            except:
                pass
            time.sleep(2)
    #评论消息-帖子消息
    def test_o_d(self):
        self.driver.find_id(sourced_id + 'tab2').click()
        self.driver.wait_id(sourced_id +'content')
        count = self.driver.find_ids(sourced_id + 'content')
        for i in range(len(count)):
            self.driver.find_ids(sourced_id + 'content')[i].click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '删除'
                self.assertIn(check, toast, msg='点击帖子评论跳转帖子详情失败')
            except:
                self.driver.wait_id(sourced_id + 'good')
                self.driver.find_id(sourced_id + 'editContent').send_keys('hhh')
                time.sleep(2)
                self.driver.find_id(sourced_id + 'btn_send').click()
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '成功'
                self.assertIn(check, toast, msg='帖子发布评论失败')
                time.sleep(2)
                self.driver.find_id(sourced_id + 'tv_right').click()
                self.driver.wait_id(sourced_id + 'tv_right')
                time.sleep(2)
                self.driver.find_id(sourced_id + 'btnBack').click()
                time.sleep(2)
                self.driver.find_id(sourced_id + 'btnBack').click()
                time.sleep(2)
            time.sleep(2)

    #退出评论消息列表返回‘我的’界面
    def test_o_e(self):
        try:
            self.driver.find_id(sourced_id + 'content')
            self.driver.find_id(sourced_id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    #聊天消息
    def test_p(self):
        self.driver.find_id(sourced_id + 'chat').click()
        time.sleep(2)












if __name__ == '__main__':
    unittest.main()
