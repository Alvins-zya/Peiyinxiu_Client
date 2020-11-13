#encoding: utf-8
'''
@author:alvin.zhu
@file:Person_center.py
@time:2020/11/2 18:08
@Description:

'''
from Public.Driver_Operate import BaseOperate,resource_id
import time
file = open('topic_words.txt','r',encoding='UTF-8')

class Person():
    def __init__(self):
        self.driver = BaseOperate()
        self.x = self.driver.touch_X()
        self.y = self.driver.touch_Y()
        self.id = resource_id

    #退出当前界面
    def Bcak(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
    #首页进入“我的”界面
    def Person_My(self):
        self.driver.wait_id(self.id + 'ivMineTab')
        self.driver.find_id(self.id + 'ivMineTab').click()
        self.driver.wait_id(self.id + 'username')
        time.sleep(2)

    #我的界面点击头像进入个人空间
    def Person_into_my_zoom(self):
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'followcount')
        time.sleep(2)

    #我的界面点击关注进入关注列表
    def Person_home_into_follow(self):
        follow_count = self.driver.find_id(self.id +'followed_count').text
        time.sleep(1)
        self.driver.find_id(self.id + 'followed_count').click()
        self.driver.wait_id(self.id  + 'filter_edit')
        time.sleep(2)
        if int(follow_count)>9:
            self.driver.back()
        else:
            follow_count1 = self.driver.find_ids(self.id + 'username')
            assert int(len(follow_count1)) == int(follow_count)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #我的界面点击粉丝进入粉丝列表
    def Person_home_into_fans(self):
        fan_count = self.driver.find_id(self.id + 'fans_count').text
        time.sleep(1)
        self.driver.find_id(self.id + 'fans_count').click()
        self.driver.wait_id(self.id + 'vip_tag')
        time.sleep(2)
        if int(fan_count) > 8:
            pass
        else:
            fan_count1 = self.driver.find_ids(self.id + 'username')
            assert int(len(fan_count1)) == int(fan_count)
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #用户ID
    def Person_copy_ID(self):
        self.driver.find_id(self.id + 'tv_uid').click()
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)

    #个人空间搜索-作品
    def Person_Zoom_works_search(self):
        search_title = self.driver.find_id(self.id + 'title').text
        time.sleep(2)
        self.driver.find_id(self.id +'photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys(search_title)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'photo').click()
        self.driver.wait_id(self.id + 'txtKeyword')
        try:
            self.driver.find_id(self.id + 'clear')
            time.sleep(2)
            self.driver.find_id(self.id + 'clear').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'clear')
                raise ('个人空间搜索作品后，点击清空搜索记录，依然显示有搜索记录')
            except:
                pass
        except:
            raise ('个人空间搜索作品后退出再进，未显示作品搜索历史记录')
        time.sleep(2)

        #个人空间搜索——作品搜索无结果显示
        self.driver.find_id(self.id + 'txtKeyword').send_keys('配音秀')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        try:
            self.driver.wait_xpath(self.id + 'll_noSearchResult')
        except:
            raise ('作品搜索无结果时未显示任何提示信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #个人空间—搜索-搜索个人素材
    def Person_Zoom_source_search(self):
        self.driver.find_id(self.id + 'source_text').click()
        time.sleep(2)
        search_title = self.driver.find_id(self.id + 'source_text').text
        time.sleep(2)
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'll_source').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('配音秀')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        try:
            self.driver.wait_xpath('没有搜到任何内容')
        except:
            raise ('素材搜索无结果时未显示任何提示信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'll_source').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys(search_title)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        time.sleep(4)
        try:
            self.driver.find_id(self.id + 'iv_source')
            name = self.driver.find_id(self.id + 'tv_source_title').text
            assert search_title in name
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_source_title').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #编辑资料
    def Person_Zoom_edit_info(self):
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5,self.y * 0.719)
        elif self.y > 2279:
            self.driver.tap(self.x * 0.5,self.y * 0.76)
        time.sleep(4)
        try:
            self.driver.find_xpath('个人资料')
        except:
            raise ('未跳转到个人资料界面')
        time.sleep(2)

    #更换头像
    def Person_Zoom_change_head(self):
        #点击头像-拍照
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x *0.5,self.y * 0.793)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'next')
            self.driver.find_id(self.id + 'next').click()
            try:
                self.driver.wait_sys('始终允许')
            except:
                try:
                    self.driver.wait_sys('允许')
                except:
                    pass
            self.driver.find_id(self.id + 'userhead').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.793)
            elif self.y == 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(2)
        except:
            pass
        time.sleep(3)
        try:
            '''
            以下操作只适用VIVOx9
            '''
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                '''
                oppo r11
                '''
                self.driver.find_id('com.oppo.camera:id/shutter_button')
                self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.oppo.camera:id/done_button').click()
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                except:
                    self.driver.back()
        time.sleep(4)
        self.driver.find_id(self.id + 'confirm').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '修改成功'
            assert toast == check
        except:
            raise ('拍照更换头像未检测到toast提示')
        time.sleep(2)
        # 更换相册图片
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.869)
        elif self.y == 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        time.sleep(2)
        self.driver.find_id(self.id + 'com.android.gallery3d:id/ic_public_arrow_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'top_frame').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'com.android.gallery3d:id/head_select_right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        try:
            toast1 = self.driver.wait_toast('//android.widget.Toast')
            check1 = '修改成功'
            self.assertEqual(toast1,check1,msg='相册替换头像toast提示内容校验不一致')
        except:
            raise ('相册更换头像未检测到toast提示')
        time.sleep(2)

    #输入个人简介
    def Person_Zoom_Introduction(self):
        self.driver.find_id(self.id + 'tv_sign').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_sign').send_keys('空空空')
        time.sleep(2)

    #修改性别
    def Person_Zoom_change_gender(self):
        gender = self.driver.find_id(self.id + 'gender').text
        if gender == '女':
            self.driver.find_id(self.id + 'tv_gender').click()
            time.sleep(2)
            if self.y ==1920:
                self.driver.tap(self.x * 0.5,self.y * 0.872)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(2)
        else:
            self.driver.find_id(self.id + 'tv_gender').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.872)
            elif self.y > 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.89)
            time.sleep(2)

    #修改地区
    def Person_Zoom_change_area(self):
        area = self.driver.find_id(self.id + 'tv_area').text
        self.driver.find_id(self.id + 'tv_area').click()
        self.driver.wait_id(self.id + 'name')
        areas = self.driver.find_ids(self.id + 'name')
        select = random.randint(0,len(areas))
        self.driver.find_ids(self.id + 'name')[select].click()
        time.sleep(2)
        area1 = self.driver.find_id(self.id + 'tv_area').text
        self.assertNotEqual(area,area1,msg='地区修改前后显示未刷新')
        time.sleep(2)

    #修改生日
    def Person_Zoom_change_birthday(self):
        self.driver.find_id(self.id + 'tv_time').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.763,self.y * 0.773)
        elif self.y == 2280:
            self.driver.tap(self.x * 0.75, self.y * 0.614)
        time.sleep(2)

    #用户名敏感词检测
    def Person_Zoom_username_check(self):
        self.driver.find_id(self.id + 'et_nickname').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_nickname').send_keys('政府')
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '敏感词'
            assert check in toast
        except:
            raise ('用户名包含有敏感词，点击保存未弹出敏感词toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'et_nickname').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id('android:id/button1').click()
        time.sleep(2)


    #会员头像挂件
    def Person_Zoom_Vip_headwear(self):
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5 ,self.y * 0.792)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.823)
        self.driver.wait_id(self.id + 'txtTitle')
        count = self.driver.find_ids(self.id + 'img')
        for i in range(len(count)-1,-1,-1):
            self.driver.find_ids(self.id + 'img')[i].click()
            time.sleep(1)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'txtContent')
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'renew')
                self.driver.find_id(self.id + 'btnBack').click()
            except:
                pass
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnCancel').click()
            time.sleep(2)
        except:
            pass

    #会员空间装扮
    def Person_Zoom_Vip_Dress(self):
        self.driver.find_id(self.id + 'userhead').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.867)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.89)
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        count = self.driver.find_ids(self.id + 'img')
        for i in range(len(count)-1,-1,-1):
            self.driver.find_ids(self.id + 'img')[i].click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #用户演绎等级
    def Person_Zoom_user_level(self):
        self.driver.find_id(self.id + 'source_level').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'img_vip').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'guize1').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    #身份认证
    def Person_Zoom_Authentication(self):
        self.driver.find_id(self.id + 'vip_description').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #粉丝列表
    def Person_Zoom_fans(self):
        self.driver.find_id(self.id + 'll_fan').click()
        self.driver.find_id(self.id + 'vip_tag')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_fan')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'iwant').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    #关注列表
    def Person_Zoom_follows(self):
        self.driver.find_id(self.id + 'll_follow').click()
        self.driver.wait_id(self.id + 'status_icon')
        self.driver.find_id(self.id + 'username').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #社团列表
    def Person_Zoom_Societies(self):
        self.driver.find_id(self.id + 'll_society').click()
        self.driver.wait_id(self.id + 'status_icon')
        time.sleep(2)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'status_icon').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'username').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #作品上榜列表
    def Person_Zoom_Crunchies_list(self):
        self.driver.find_id(self.id + 'll_rank').click()
        self.driver.wait_id(self.id + 'middle_img')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv_vip')
            self.driver.find_id(self.id + 'tv_vip').click()
            time.sleep(2)
            self.driver.wait_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)


    #作品列表
    def Person_Zoom_work_list(self):
        for i in range(10):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'filmBg1').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)

    #切换作品列表tab
    def Person_Zoom_work_switch_label(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        count = self.driver.find_ids(self.id + 'title')
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        for i in range(len(count)-1,-1,-1):
            self.driver.find_id(self.id + 'film_all_count').click()
            time.sleep(2)
            self.driver.find_ids(self.id + 'title')[i].click()
            time.sleep(2)

    #置顶作品
    def Person_Zoom_work_top(self):
        el = self.driver.find_ids(self.id + 'filmBg1')[0]
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.789)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.83)
        time.sleep(4)
        try:
            self.driver.find_id(self.id + 'img')
        except:
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.943)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.952)
            time.sleep(2)
            self.driver.find_ids(self.id + 'filmBg1')[0].click()
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'setting').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.703)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.75)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
            time.sleep(4)
            el = self.driver.find_ids(self.id + 'filmBg1')[0]
            self.driver.Long_Touche(el,3000)
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.789)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.83)
            time.sleep(4)
            try:
                self.driver.find_id(self.id + 'img')
            except:
                raise ('未显示置顶标签')
        time.sleep(2)

    #作品列表界面长按删除作品
    def Person_Zoom_work_delete(self):
        el = self.driver.find_ids(self.id + 'filmBg1')[0]
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.868)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(4)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(4)

    #个人空间-求合作
    def Person_Zoom_coors(self):
        self.driver.find_id(self.id + 'coor_text').click()
        self.driver.wait_id(self.id + 'btnCooperate')
        self.driver.find_id(self.id + 'islook').click()
        self.driver.wait_download(self.id + 'play')
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCooperate').click()
        self.driver.wait_download(self.id + 'action')
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        for i in range(5):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)

    #求合作-邀请好友
    def Person_Zoom_coor_invite(self):
        el = self.driver.find_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x* 0.5,self.y * 0.629)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.688)
        self.driver.wait_id(self.id + 'socialstatus')
        self.driver.find_id(self.id + 'socialstatus').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('给自己的合作！')
        time.sleep(2)
        self.driver.find_id(self.id + 'reprint').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '邀请成功'
            assert toast == check
        except:
            raise ('发送邀请后未检测到toast提示')
        time.sleep(2)

    #求合作-私密（公开）
    def Person_Zoom_coor_Private_public(self):
        el = self.driver.find_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.703)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.746)
        time.sleep(2)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = "公开成功"
            self.assertIn(check,toast,msg='求合作私密转公开toast校验不一致')
        except:
            try:
                self.driver.find_id(self.id + 'renew')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
                self.driver.back()
                time.sleep(2)
            except:
                pass
        time.sleep(2)

    #求合作删除
    def Person_Zoom_coor_delete(self):
        el = self.driver.find_id(self.id + 'item_sh_cooperate_article_image')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.857)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.877)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            self.assertIn(check,toast,msg='求合作删除失败')
        except:
            pass
        time.sleep(2)

    #素材-视频预览
    def Person_Zoom_source_preview(self):
        self.driver.find_id(self.id +'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'source_text')
        time.sleep(2)
        self.driver.find_id(self.id + 'source_text').click()
        self.driver.wait_id(self.id + 'imgSource')
        self.driver.find_id(self.id + 'imgSource').click()
        self.driver.wait_id(self.id + 'right_icon1')
        time.sleep(10)
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #素材配音
    def Person_Zoom_Source_dubbing(self):
        self.driver.find_id(self.id + 'imgSource').click()
        self.driver.wait_id(self.id + 'right_icon1')
        self.driver.Background()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'yinpin')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(self.id + 'roleall')
                    break
                except:
                    self.driver.find_id(self.id + 'btnSubmit')
                    time.sleep(1)
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    break
            self.driver.wait_id(self.id + 'roleall')
            self.driver.find_id(self.id +'roleall').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id +'btnSubmit').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'imgTip').click()
            while True:
                try:
                    self.driver.find_id(self.id + 'action')
                    break
                except:
                    self.driver.find_id(self.id + 'btnSubmit')
                    time.sleep(1)
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    break
                time.sleep(1)
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        time.sleep(2)

    #更多-点赞
    def Person_Zoom_goods_record(self):
        self.driver.find_id(self.id + 'more_text').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'filmBg')
        time.sleep(2)
        num = self.driver.find_id(self.id + 'look').text
        if num == '0':
            el =  self.driver.find_id(self.id + 'filmBg')
            self.driver.Long_Touche(el,3000)
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_good').click()
        good1 = self.driver.find_id(self.id + 'tv_good').text
        self.driver.find_id(self.id + 'tv_good').click()
        time.sleep(1)
        good2 = self.driver.find_id(self.id +'tv_good').text
        assert good1 != good2
        time.sleep(2)

    # 更多-转发
    def Person_Zoom_forward(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('转发').click()
        self.driver.wait_id(self.id + 'filmBg')
        name = self.driver.find_id(self.id + 'userName').text
        self.driver.find_id(self.id + 'filmBg').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.Background()
        time.sleep(2)
        detail_name = self.driver.find_id(self.id + 'textView').text
        assert name == detail_name
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #作品转发列表——删除作品
        title = self.driver.find_id(self.id + 'title').text
        count = self.driver.find_id(self.id + 'film_all_count').text
        el = self.driver.find_id(self.id + 'filmBg')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            self.driver.find_xpath(title)
            raise ('转发作品删除失败')
        except:
            pass
        time.sleep(2)
        count1 = self.driver.find_id(self.id + 'film_all_count').text
        assert count == count1
        time.sleep(2)

    #帖子列表
    def Person_Zoom_post_list(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('帖子').click()
        time.sleep(4)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'good').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tag').click()
        self.driver.wait_id(self.id + 'img_subscribe')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'comment').click()
        self.driver.wait_id(self.id + 'editContent')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)



    #帖子-转发私信-删除
    def Person_Zoom_forword_and_delete(self):
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5 , self.y * 0.793)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5 ,self.y * 0.829)
        time.sleep(2)
        self.driver.find_id(self.id +'group_chat').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'name').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'action').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast
        except:
            raise ('帖子删除未检测到toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'username').click()
        self.driver.wait_id(self.id + 'film_all_count')
        self.driver.find_id(self.id + 'more_text').click()
        time.sleep(2)

    #语聊列表
    def Person_chat_list(self):
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('语聊').click()
        time.sleep(4)

    #创建合辑
    def Person_Zoom_create_compilation(self):
        self.driver.find_id(self.id + 'btnRight').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(2)
        self.driver.find_id(self.id + 'content').send_keys('合辑')
        time.sleep(2)
        self.driver.find_id(self.id + 'ok').click()
        time.sleep(3)
        try:
            self.driver.find_id(self.id + 'choice')
            self.driver.find_id(self.id + 'choice').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_right').click()
            try:
                toast = self.driver.wait_toast('//android.widget.Toast')
                check = '创建成功'
                assert toast == check
                time.sleep(2)
            except:
                pass
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)

    #合辑删除
    def Person_Zoom_delete_compilation(self):
        self.driver.find_id(self.id + 'single_text').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'film_all_count').click()
        time.sleep(2)
        self.driver.find_xpath('合辑').click()
        self.driver.wait_id(self.id + 'filmBg')
        el = self.driver.find_id(self.id + 'filmBg')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.871)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.895)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check in toast
        except:
            pass
        time.sleep(2)

    #退出个人空间
    def Person_Zoom_quit(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)


    #我的界面VIP入口
    def Person_Vip_enter(self):
        # 会员首次购买优惠入口
        try:
            self.driver.find_id(self.id + 'right_huiyuan').click()
            self.driver.wait_id(self.id + 'renew')
            self.driver.find_id(self.id + 'btnBack').click()
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'img_vip').click()
        self.driver.wait_id(self.id + 'renew')
        time.sleep(2)



    #会员权益计算
    def Person_Vip_Equity(self):
        self.driver.find_id(self.id + 'img_right').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'price')
        except:
            raise ('会员权益计算弹窗中未检测到相关控件')
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

    #会员价格
    def Person_Vip_Price(self):
        price = self.driver.find_ids(self.id + 'tv_now_money')
        for i in range(len(price)):
            Price = self.driver.find_ids(self.id + 'tv_now_money')[i].text
            self.driver.find_ids(self.id + 'rl_all')[i].click()
            time.sleep(1)
            self.driver.find_id(self.id + 'renew').click()
            time.sleep(2)
            Price_buy = self.driver.find_id(self.id + 'tv_money').text
            assert Price in Price_buy
            time.sleep(2)
            self.driver.find_id(self.id + 'close_icon').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'cancel').click()
            time.sleep(2)

    #会员赠送
    def Person_Vip_Give(self):
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'user_head')
        self.driver.find_id(self.id + 'user_head').click()
        self.driver.wait_id(self.id + 'll_follow')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'send').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'renew')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #会员特权
    def Person_Vip_Privileges(self):
        try:
            self.driver.find_xpath('作品编辑')
        except:
            if self.y <=2280:
                self.driver.swip_move(self.x * 0.5 ,self.y * 0.818,self.x * 0.5, self.y * 0.585)
        time.sleep(2)
        Member_privileges_page1 =self.driver.find_ids(self.id + 'name')
        privileges_list = []
        for i in range(len(Member_privileges_page1)):
            Name = self.driver.find_ids(self.id + 'name')[i].text
            privileges_list.append(Name)
        time.sleep(2)
        Start_Locat = self.driver.find_ids(self.id + 'name')[-1].location
        End_Locat = self.driver.find_ids(self.id + 'name')[-4].location
        start_swip_x = Start_Locat['x']
        start_swip_y = Start_Locat['y']
        end_swip_x = End_Locat['x']
        end_swip_y = End_Locat['y']
        if self.y >= 2280:
            self.driver.swip_move(start_swip_x, start_swip_y, end_swip_x, end_swip_y)
        time.sleep(2)
        Member_privileges_page2 = self.driver.find_ids(self.id + 'name')
        for i in range(len(Member_privileges_page2)):
            Name1 = self.driver.find_ids(self.id + 'name')[i].text
            privileges_list.append(Name1)
        privileges_chck_list = ['双倍金币','免费曝光','推荐涨粉','升级加速','上榜历史','作品下载','评论置顶',
                                '作品编辑','云端存储','语聊麦位','专属挂件','空间装扮']
        assert sorted(privileges_list) == sorted(privileges_chck_list)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #系统消息
    def Person_System_Notices(self):
        self.driver.find_id(self.id + 'system_notice').click()
        self.driver.wait_id(self.id + 'userhead')
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'benCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #点赞消息
    def Person_Good_Notices(self):
        try:
            self.driver.find_id(self.id + 'gift_point')
            self.driver.find_id(self.id + 'gift').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'gift_point')
                raise ('点赞红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'gift').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'userhead')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'content').click()
        try:
            self.driver.wait_toast('//android.widget.Toast')
            time.sleep(2)
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

        #回赞
        self.driver.find_id(self.id + 'guanzhu').click()
        self.driver.wait_id(self.id + 'tv_video_detail_title')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #合作消息
    def Person_Coor_Notices(self):
        try:
            self.driver.find_id(self.id + 'cooper_count')
            self.driver.find_id(self.id + 'textView15').click()
            self.driver.wait_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'cooper_count')
                raise ('合作消息红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'textView15').click()
        self.driver.wait_id(self.id + 'more')
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #合作配音
    def Person_Coor_Dubbing(self):
        try:
            self.driver.find_xpaths('合作配音')[1].click()
            self.driver.wait_download(self.id + 'action')
            time.sleep(2)
            self.driver.find_id(self.id + 'back').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'play').click()
            self.driver.back()
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    #删除合作消息
    def Person_Coor_delete(self):
        for i in range(4):
            self.driver.swip_up()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'more').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.882)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5 ,self.y * 0.903)
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除合作消息成功'
            self.assertIn(check,toast,msg='合作消息删除失败')
        except:
            raise ('未检测到合作消息删除toast提示')
        time.sleep(2)

    #生成作品
    def Person_Coor_Generate_works(self):
        self.driver.find_id(self.id + 'rl_tag2').click()
        time.sleep(2)
        self.driver.find_xpaths('生成作品')[1].click()
        time.sleep(2)
        self.driver.find_id(self.id + 'head_name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_take_photo').click()
        time.sleep(5)
        try:
            '''
            以下操作只适用VIVOx9
            '''
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(4)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                '''
                oppo r11/r15
                '''
                self.driver.find_id('com.oppo.camera:id/shutter_button')
                self.driver.find_id('com.oppo.camera:id/shutter_button').click()
                time.sleep(4)
                self.driver.find_id('com.oppo.camera:id/done_button').click()
            except:
                try:
                    self.driver.find_id('com.huawei.camera:id/shutter_button')
                    self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                    time.sleep(4)
                    self.driver.find_id('com.huawei.camera:id/done_button').click()
                except:
                    self.driver.back()
        time.sleep(4)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'head_name').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_photo').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'photo_wall_item_photo').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'confirm').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'title').send_keys('功能测试')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'tv')
            self.driver.find_id(self.id + 'tv').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_close').click()
        time.sleep(2)

    #生成作品tab界面预览视频
    def Person_Coor_video_play(self):
        self.driver.find_id(self.id + 'play').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            self.assertIn(check,toast,msg='视频详情界面进入失败')
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    #合作消息设置
    def Person_Coor_Notice_setting(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(4)
        #获取当前界面所有resourceId,但部分ID不可用，因此无法区分筛选出真正可以点击的ID
        # count = self.driver.search_id()
        # print(count)
        # self.id = re.findall(r'resource-id="com.happyteam.dubbingshow:id/(.*?)"',count)
        # print(self.id)
        self.driver.find_id(self.id + 'acceptAll').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'acceptFirends').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'acceptNone').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'clearAllInviter').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnCancel').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #评论消息-跳转个人空间
    def Person_Comment_Notices(self):
        try:
            self.driver.find_id(self.id + 'comment_count')
            self.driver.find_id(self.id + 'textView16').click()
            self.driver.wait_id(self.id + 'reply')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'comment_count')
                raise ('评论消息红点未消失')
            except:
                pass
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'textView16').click()
        self.driver.wait_id(self.id + 'reply')
        time.sleep(2)
        name = self.driver.find_id(self.id + 'textView').text
        time.sleep(2)
        self.driver.find_id(self.id + 'userhead').click()
        self.driver.wait_id(self.id + 'll_follow')
        time.sleep(2)
        Zoom_name = self.driver.find_id(self.id +'username').text
        assert name == Zoom_name
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #评论消息-关注
    def Person_Comment_follows(self):
        self.driver.find_id(self.id + 'guanzhu').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'editContent')
            time.sleep(2)
            self.driver.find_id(self.id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.854)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.877)
            self.driver.wait_id(self.id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(self.id + 'follow_status').click()
            time.sleep(3)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
        except:
            self.driver.find_id(self.id + 'guanzhu').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'right_icon1').click()
            time.sleep(2)
            if self.y == 1920:
                self.driver.tap(self.x * 0.5, self.y * 0.854)
            elif self.y >= 2280:
                self.driver.tap(self.x * 0.5, self.y * 0.877)
            self.driver.wait_id(self.id + 'll_follow')
            time.sleep(2)
            self.driver.find_id(self.id + 'follow_status').click()
            time.sleep(3)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.swip_down()
        time.sleep(2)
        self.driver.find_id(self.id + 'guanzhu').click()
        time.sleep(2)

    #评论消息-进入作品详情
    def Person_Comment_video_detail(self):
        self.driver.find_id(self.id + 'content').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check in toast
        except:
            self.driver.wait_id(self.id + 'tv_video_detail_title')
            self.driver.Background()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)

    #评论消息-回复评论
    def Person_Comment_Reply(self):
        self.driver.find_id(self.id + 'reply_btn').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('哈哈哈')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_toast('//android.widget.Toast')
        try:
            self.driver.find_id(self.id + 'editContent')
            self.driver.back()
        except:
            pass

    #评论消息-帖子消息
    def Person_Comment_Post_Notices(self):
        self.driver.find_id(self.id + 'tab2').click()
        self.driver.wait_id(self.id +'content')
        self.driver.find_id(self.id + 'content').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除'
            assert check == toast,'帖子跳转失败'
        except:
            self.driver.wait_id(self.id + 'editContent')
            self.driver.find_id(self.id + 'editContent').send_keys('hhh')
            time.sleep(2)
            self.driver.find_id(self.id + 'btn_send').click()
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            assert check == toast,'帖子发布评论失败'
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)

    #聊天消息
    def Person_Chat_Notices(self):
        try:
            self.driver.find_id(self.id + 'chat_count')
            self.driver.find_id(self.id + 'chat').click()
            self.driver.wait_id(self.id + 'right_icon1')
            while True:
                try:
                    self.driver.find_id(self.id + 'txtCount')
                    self.driver.find_id(self.id + 'txtCount').click()
                    self.driver.wait_id(self.id + 'editContent')
                    self.driver.find_id(self.id + 'btnBack').click()
                    time.sleep(2)
                except:
                    break
                time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'chat_count')
                raise ('私信消息红点未消失')
            except:
                pass
        except:
            pass
        self.driver.find_id(self.id + 'chat').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'right_icon1')
        time.sleep(2)

    #聊天列表界面用户
    def Person_chat_user_list(self):
        try:
            self.driver.find_id(self.id + 'userhead')
            count = self.driver.find_ids(self.id + 'userhead')
            for i in range(len(count)):
                self.driver.find_ids(self.id + 'userhead')[i].click()
                self.driver.wait_id(self.id + 'editContent')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
        except:
            pass
        time.sleep(2)

    #用户聊天
    def Person_User_Chat(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'filter_edit').send_keys('16685645')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSearch').click()
        self.driver.wait_xpath('撸串')
        self.driver.find_id(self.id + 'name').click()
        time.sleep(2)

        #清除聊天记录
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送文字
        self.driver.find_id(self.id + 'editContent').send_keys('功能测试')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'content')
        try:
            self.driver.find_xpath('功能测试')
        except:
            raise ('聊天内容区域未找到发送的文案')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送表情
        self.driver.find_id(self.id + 'btn_send_smile').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'emojicon_icon').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        self.driver.wait_id(self.id + 'content')
        try:
            self.driver.find_id(self.id + 'content')
        except:
            raise ('聊天内容区域未找到发送的表情')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送语音
        self.driver.find_id(self.id + 'btn_change_input_mode').click()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'btn_record_voice')
        self.driver.Long_Touche(el,3000)
        self.driver.wait_id(self.id + 'btn_play_sound_content_layout')
        self.driver.find_id(self.id + 'btn_play_sound_content_layout').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送图片
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'photo').click()
        time.sleep(4)
        self.driver.find_id(self.id + 'cb_select_tag').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next_step_tv').click()
        self.driver.wait_id(self.id + 'chat_image')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #拍照发送私信信息
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'camera').click()
        time.sleep(4)
        try:
            self.driver.find_id('com.android.camera:id/shutter_button')
            self.driver.find_id('com.android.camera:id/shutter_button').click()
            time.sleep(3)
            self.driver.find_id('com.android.camera:id/done_button').click()
        except:
            try:
                self.driver.find_id('com.huawei.camera:id/shutter_button')
                self.driver.find_id('com.huawei.camera:id/shutter_button').click()
                time.sleep(3)
                self.driver.find_id('com.huawei.camera:id/done_button').click()
            except:
                pass
        self.driver.wait_id(self.id + 'chat_image')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送作品
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'film').click()
        time.sleep(4)
        self.driver.find_id('filmBg').click()
        time.sleep(3)
        self.driver.find_id(self.id + 'btnSelect').click()
        self.driver.wait_id(self.id + 'chat_film_title')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送红包
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'redpacket').click()
        time.sleep(2)
        self.driver.find_id(self.id +'cash_num').send_keys('0.1')
        time.sleep(3)
        self.driver.find_id(self.id + 'generate_red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_id(self.id + 'red_packet')
        time.sleep(2)
        self.driver.find_id(self.id + 'red_packet').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'open_red_packet_btn').click()
        self.driver.wait_id(self.id + 'diamond')
        time.sleep(2)
        self.driver.find_id(self.id + 'red_packet_detail_close_btn').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

        #发送社团邀请
        self.driver.find_id(self.id + 'show_action').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'union_inviter').click()
        time.sleep(4)
        self.driver.find_id('userName').click()
        self.driver.wait_id(self.id + 'union_inviter_apply')
        self.driver.find_id(self.id + 'union_inviter_apply').click()
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.697)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.754)
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.662, self.y * 0.558)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.67, self.y * 0.546)
        time.sleep(2)

    #私信聊天界面举报用户-其它原因
    def Person_Chat_Report(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.619)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.689)
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_action_other').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').clear()
        time.sleep(2)
        self.driver.find_id(self.id + 'txtKeyword').send_keys('功能测试，可忽略此举报信息')
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '举报成功'
            assert check == toast,'私信聊天用户举报toast校验不一致'
        except:
            raise ('未检测到举报成功toast')
        time.sleep(2)

    #私信聊天界面-进入对方空间
    def Person_Chat_Zoom(self):
        try:
            self.driver.find_id(self.id + 'txtKeyword')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.5, self.y * 0.859)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.5, self.y * 0.877)
        self.driver.wait_id(self.id + 'll_fan')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #私信列表界面长按删除
    def Person_Chat_list_delete(self):
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        el = self.driver.find_xpath('撸串')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'delete').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('撸串')
            raise ('列表中长按用户删除失败')
        except:
            pass
        time.sleep(2)

    #私信消息-未关注
    def Person_Chat_Not_follow(self):
        self.driver.find_id(self.id + 'tab2').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userhead')
            self.driver.find_id(self.id + 'userhead').click()
            time.sleep(3)
            try:
                self.driver.find_id(self.id + 'tishi')
            except:
                raise ('私信未关注界面，私信详情界面未显示谨防诈骗信息')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            el = self.driver.find_id(self.id + 'userhead')
            self.driver.Long_Touche(el,3000)
            time.sleep(2)
            self.driver.find_id(self.id + 'delete').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btnSubmit').click()
            time.sleep(2)
        except:
            pass
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)


    #草稿箱-会员同步
    def Person_Vip_Draft_synchronous(self):
        self.driver.find_id(self.id + 'draft').click()
        time.sleep(2)
        self.driver.find_xpath('同步').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'renew')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.wait_xpath('同步')
        time.sleep(2)

    #草稿箱作品断网后删除再重新同步下载
    def Person_Draft_reload(self):
        date_before = self.driver.find_id(self.id + 'date').text
        self.driver.Disconnect_network()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'date')
        self.driver.Long_Touche(el,3000)
        if self.y == 1920:
            self.driver.tap(self.x * 0.656, self.y * 0.552)
        elif self.y >= 2280:
            self.driver.tap(self.x * 0.657, self.y * 0.546)
        else:
            pass
        time.sleep(2)
        self.driver.Only_wifi()
        time.sleep(15)
        self.driver.find_xpath('同步').click()
        time.sleep(2)
        self.driver.wait_xpath('同步')
        date_after = self.driver.find_id(self.id + 'date').text
        assert date_before == date_after, '草稿箱断网情况删除以后联网再同步，作品时间校验不一致'
        time.sleep(2)

    #草稿箱-草稿箱作品视频预览
    def Person_Draft_Video_Preview(self):
        self.driver.find_id(self.id + 'imgSource').click()
        time.sleep(2)
        self.driver.wait_download(self.id + 'play')
        time.sleep(2)
        self.driver.back()
        time.sleep(3)

    #草稿箱作品时间重复性检查
    def Person_Draft_Repeat(self):
        date  = self.driver.find_ids(self.id + 'date')
        list = []
        for i in range(len(date)):
            times = self.driver.find_ids(self.id + 'date')[i].text
            list.append(times)
            time.sleep(1)
        set_list = set(list)#set会生成一个元素无序且不重复的可迭代对象，也就是我们常说的去重
        if len(list) == len(set_list):
            pass
        else:
            Dic = dict(Counter(list))
            print([key for key , value in Dic.items() if value >1])#展示重复元素
        time.sleep(2)

    #草稿箱作品重配
    def Person_Draft_Reassignment(self):
        count = self.driver.find_ids(self.id + 'imgSource')
        for i in range(len(count)):
            self.driver.find_ids(self.id + 'upload')[i].click()
            time.sleep(2)
            try:
                self.driver.find_id(self.id + 'reDubbing')
                self.driver.find_id(self.id + 'reDubbing').click()
                break
            except:
                self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        time.sleep(2)
        while True:
            try:
                self.driver.find_id(self.id + 'roleall')
                self.driver.find_id(self.id + 'roleall').click()
                break
            except:
                try:
                    self.driver.find_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                        break
                    except:
                        pass
                    break
                except:
                    break
            time.sleep(2)
        self.driver.wait_id(self.id + 'action')
        self.driver.find_id(self.id + 'action').click()
        self.driver.wait_download(self.id + 'title')
        self.driver.Background()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        self.driver.wait_id(self.id + 'txtTitle')
        time.sleep(2)
        self.driver.find_id(self.id + 'pri_switch_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'saveToDraft').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.wait_xpath('退出配音')
        self.driver.find_xpath('退出配音').click()
        time.sleep(2)
        self.Bcak()



    #已配素材列表
    def Person_Already_source_list(self):
        self.driver.find_id(self.id + 'source').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'iv_source')

    #已配素材列表界面点击配音
    def Person_Already_source_dubbing(self):
        self.driver.find_id(self.id + 'iv_dub').click()
        while True:
            try:
                self.driver.find_id(self.id + 'roleall')
                self.driver.find_id(self.id + 'roleall').click()
                break
            except:
                try:
                    self.driver.find_id(self.id + 'btnSubmit')
                    self.driver.find_id(self.id + 'btnSubmit').click()
                    try:
                        self.driver.find_id(self.id + 'roleall')
                        self.driver.find_id(self.id + 'roleall').click()
                        break
                    except:
                        pass
                    break
                except:
                    break
            time.sleep(2)
        self.driver.wait_id(self.id + 'action')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)



    #已配素材列表界面删除已配素材
    def Person_Alread_Source_delete(self):
        source = self.driver.find_id(self.id + 'iv_source')
        self.driver.Long_Touche(source,3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '删除成功'
            self.assertEqual(toast,check,msg='已配素材长按删除toast提示检验不一致')
            time.sleep(2)
        except:
            raise ('未检测到素材删除toast提示')
        time.sleep(2)

    #断网环境下删除已配素材，联网后再刷新
    def Person_Alread_Source_delete_network(self):
        delete_before = self.driver.find_id(self.id + 'tv_source_title').text
        self.driver.Disconnect_network()
        time.sleep(2)
        el = self.driver.find_id(self.id + 'tv_source_title')
        self.driver.Long_Touche(el,3000)
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_toast('//android.widget.Toast')
        self.driver.Only_wifi()
        time.sleep(10)
        self.driver.swip_down()
        time.sleep(2)
        Refresh_after = self.driver.find_id(self.id +'tv_source_title').text
        assert delete_before == Refresh_after,'断网情况下删除已配素材再联网刷新列表，未显示之前删除的素材'
        time.sleep(2)

    #已配素材批量删除
    def Person_Alread_Source_Bulk_deletion(self):
        self.driver.find_id(self.id +'delete').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'choice').click()
        time.sleep(2)
        delete = self.driver.find_id(self.id + 'tv_source_title').text
        time.sleep(2)
        self.driver.find_id(self.id + 'toDelete').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        self.driver.wait_toast('//android.widget.Toast')
        delete_after = self.driver.find_id(self.id + 'tv_source_title').text
        assert delete != delete_after,'批量删除未成功删除'
        time.sleep(2)
        self.driver.find_id(self.id + 'cancel').click()
        time.sleep(2)
        self.Bcak()

    #素材收藏
    def Person_Source_collection(self):
        self.driver.find_id(self.id + 'collect').click()
        time.sleep(2)
        try:
            self.driver.find_xpath('您还没有收藏任何素材哦~')
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'btn_more').click()
            self.driver.wait_id(self.id + 'iv_source')
            self.driver.swip_up()
            time.sleep(2)
            count = self.driver.find_ids(self.id + 'iv_source')
            for i in range(len(count)):
                self.driver.find_ids(self.id + 'iv_source')[i].click()
                self.driver.wait_id(self.id + 'btn_video_detail_follow')
                self.driver.Background()
                time.sleep(2)
                self.driver.find_id(self.id + 'shouchang_tv_fake').click()
                self.driver.wait_toast('//android.widget.Toast')
                time.sleep(2)
                self.driver.find_id(self.id + 'btnBack').click()
                time.sleep(2)
            time.sleep(2)
            self.driver.find_id(self.id + 'ivMineTab').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'collect').click()
            self.driver.wait_id(self.id + 'iv_source')
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    #素材预览界面取消收藏后刷新收藏列表
    def Person_Source_collection_refresh(self):
        self.driver.find_id(self.id + 'iv_source').click()
        self.driver.wait_id(self.id + 'userhead')
        self.driver.Background()
        time.sleep(2)
        cancel_before = self.driver.find_id(self.id + 'source_title').text
        self.driver.find_id(self.id + 'shouchang_tv_fake').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '取消收藏成功'
            assert check in toast,'素材取消收藏失败'
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            raise ("未检测到取消收藏的toast提示")
        time.sleep(2)
        self.driver.swip_down()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'source_title')
            cancel_after = self.driver.find_id(self.id + 'source_title').text
            assert cancel_before != cancel_after,'素材取消收藏，收藏列表刷新依然显示有该素材'
            time.sleep(2)
        except:
            pass
        time.sleep(2)

    #自制素材列表
    def Person_Self_control_source(self):
        self.driver.find_id(self.id + 'upload_source').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'middle').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'titlebar')
            time.sleep(2)
            self.driver.find_id(self.id + 'btnBack').click()
            time.sleep(2)
        except:
            self.driver.find_id(self.id + 'btnBack').click()
            raise ('未加载出素材收录标准文案')
        time.sleep(2)


    #上传自制素材
    def Person_Self_Control_Video_Select(self):
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'll_upload').click()
        time.sleep(2)
        self.driver.find_id('android:id/title').click()
        self.driver.wait_id(self.id + 'next')

    #视频剪辑
    def Person_Self_Control_Video_Clip(self):
        self.driver.find_id(self.id + 'play_button').click()
        time.sleep(5)
        self.driver.Background()
        time.sleep(2)
        self.driver.wait_id(self.id + 'play_button')
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'cant_clip_tip')
        except:
            if self.y == 1920:
                self.driver.swip_move(self.x * 0.124, self.y * 0.385, self.x * 0.688, self.y * 0.385)
            elif self.y >= 2280:
                self.driver.swip_move(self.x * 0.903, self.y * 0.472, self.x * 0.5, self.y * 0.472)
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        self.driver.wait_id(self.id + 'et_content')
        time.sleep(2)

        # 素材添加角色名称
        self.driver.find_id(self.id + 'et_content').send_keys('角色1')
        time.sleep(2)
        self.driver.find_id(self.id + 'rl_role2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'add_role_tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'et_content2').send_keys('角色2')
        self.driver.find_id(self.id + 'rl_role3').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'sure').click()
        time.sleep(2)

        #添加字幕
        self.driver.find_id(self.id + 'tv_add_zimu').click()
        self.driver.wait_id(self.id + 'et')
        self.driver.find_id(self.id + 'close_zimu').click()
        time.sleep(2)
        roles = ['tv_role1','tv_role2']
        words = ['角色1的台词','角色2的台词']
        for i in range(len(roles)):
            self.driver.find_id(self.id + 'tv_add_zimu').click()
            self.driver.wait_id(self.id + 'et')
            self.driver.find_id(self.id + roles[i]).click()
            self.driver.find_id(self.id + 'et').send_keys(words[i])
            time.sleep(2)
            self.driver.find_id(self.id + 'complete_zimu').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'rl_bottom').click()
            time.sleep(2)
        content = ['tv_content2','tv_content2']
        for i in range(len(content)):
            try:
                self.driver.find_id(self.id + content[i])
            except:
                raise ('字幕显示错误')
        time.sleep(2)

        #编辑字幕
        self.driver.find_id(self.id + 'linear_view2').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_delete_zimu').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)


        # 裁剪视频预览
        self.driver.find_id(self.id + 'play_button').click()
        time.sleep()
        self.driver.wait_id(self.id + 'play_button')
        time.sleep(2)

        #存草稿
        self.driver.find_id(self.id + 'save').click()
        time.sleep(2)

        #退出素材制作再进
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'right_icon1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'll_upload').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnSubmit').click()
        time.sleep(2)

        #进入上传素材界面
        self.driver.find_id(self.id + 'next').click()
        time.sleep(2)

        #素材上传封面中添加文字
        self.driver.find_id(self.id + 'add_text').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'editContent').send_keys('素材封面图')
        time.sleep(2)
        self.driver.find_id(self.id + 'btn_send').click()
        time.sleep(2)

        #素材封面更换
        self.driver.find_xpath('更换封面').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'next').click()
        time.sleep(2)

        #素材名称
        self.driver.find_id(self.id + 'et_title').send_keys('素材上传测试')
        time.sleep(2)

        #添加素材音乐
        self.driver.find_id(self.id + 'addMusic').click()
        self.driver.wait_id(self.id + 'title')
        self.driver.find_id(self.id + 'title').click()
        time.sleep(2)
        self.driver.find_id(self.id +'local_music').click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_id(self.id + 'local_video_music').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'icon_thumb').click()
        self.driver.wait_id(self.id +'complete')
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)
        self.driver.find_id(self.id +'btnDownload').click()
        self.driver.wait_id(self.id +'tv_use')
        self.driver.find_id(self.id + 'tv_use').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'complete').click()
        time.sleep(2)

        #添加素材标签
        self.driver.find_id(self.id + 'tv1').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'edit_text').send_keys('测试')
        self.driver.find_id(self.id + 'btn_search').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)

        #上传素材
        self.driver.find_id(self.id + 'next').click()
        while True:
            try:
                self.driver.find_id(self.id + 'iv_dub')
                break
            except:
                self.driver.find_id(self.id +'linear_biaoqian').click()
            time.sleep(10)
        time.sleep(2)


    #个人中心-我的财富
    def Person_My_Wealth(self):
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'money').click()
        self.driver.wait_id(self.id + 'diamond_count_tv')
        time.sleep(2)

        #个人中心-我的账单
        self.driver.find_id(self.id + 'toBill').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        # ids = self.driver.search_id()
        # print(ids)
        # list = re.findall('content-desc="(.*?)"', ids)
        # print(list)
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)

        #点击购买钻石
        for i in range(6):
            price = self.driver.find_ids(self.id + 'price_tv')[i].text
            time.sleep(1)
            self.driver.find_ids(self.id + 'price_tv')[i].click()
            time.sleep(2)
            self.driver.find_id(self.id + 'tv_pay').click()
            self.driver.wait_id('android:id/text1')
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dn').click()
            time.sleep(2)
            self.driver.find_id('com.tencent.mm:id/dm3').click()
            time.sleep(2)
            self.driver.find_id(self.id + 'close_icon').click()
            time.sleep(2)
        time.sleep(2)
        self.driver.find_id(self.id + 'back').click()
        time.sleep(2)

    #个人中心-我的收益
    def Person_My_earnings(self):
        self.driver.find_id(self.id + 'gold').click()
        self.driver.wait_id(self.id + 'gold_count')

        #常见问题
        self.driver.find_id(self.id + 'tv_right').click()
        self.driver.wait_id(self.id + 'btnClose')
        time.sleep(2)
        ids = self.driver.search_id()
        # print(ids)
        # list = re.findall('content-desc="(.*?)"', ids)
        # print(list)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

        #绑定支付宝
        self.driver.find_id(self.id + 'right').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'send_code').click()
        try:
            toast = self.driver.wait_toast('//android.widget.Toast')
            check = '成功'
            self.assertIn(check,toast,msg='验证码发送失败')
        except:
            raise ('未检测到验证码发送toast提示')
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)
        try:
            self.driver.find_id(self.id + 'userhead')
            self.driver.find_id(self.id +'userhead').click()
            self.driver.wait_id(self.id + 'll_fan')
            self.driver.find_id(self.id +'btnBack').click()
            time.sleep(2)
        except:
            pass
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #我的成就
    def Person_My_achievements(self):
        self.driver.find_id(self.id + 'achievement').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #邀请好友
    def Person_Invite_friend(self):
        self.driver.find_id(self.id + 'addfriend').click()
        time.sleep(2)

        #规则
        self.driver.find_id(self.id + 'tv_right').click()
        time.sleep(2)
        self.driver.wait_id(self.id + 'btnClose')
        self.driver.find_id(self.id + 'btnClose').click()
        time.sleep(2)
        
        #邀请好友
        self.driver.find_id(self.id + 'tv_invite').click()
        time.sleep(2)

        # 朋友圈
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mm:id/dn').click()
        time.sleep(3)

        # QQ空间
        self.driver.find_id(self.id + 'tv_invite').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.49, self.y * 0.68)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.712)
        self.driver.wait_xpath('发表')
        self.driver.find_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        time.sleep(3)


        # 点击复制链接
        self.driver.find_id(self.id + 'tv_invite').click()
        time.sleep(2)
        if self.y == 1920:
            self.driver.tap(self.x * 0.12, self.y * 0.83)
        elif self.y > 2280:
            self.driver.tap(self.x * 0.126, self.y * 0.833)
        self.driver.wait_toast('//android.widget.Toast')
        time.sleep(2)

    #积分商城
    def Person_Points_Mall(self):
        self.driver.find_id(self.id + 'exchange').click()
        time.sleep(2)
        self.driver.find_id(self.id + 'btnBack').click()
        time.sleep(2)

    #夜间模式
    def Person_Mode_switch(self):
        self.driver.find_id(self.id + 'tvChange').click()
        time.sleep(5)
        self.driver.swip_up()
        time.sleep(2)
        self.driver.find_id(self.id + 'tvChange').click()
        time.sleep(5)

